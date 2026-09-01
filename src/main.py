from machine import Pin, PWM
import time

class TB6612FNG:
    def __init__(self, stby_a=0, stby_b=7 ,ain1=2, ain2=3, bin1=4, bin2=5, pwma=1, pwmb=6, pwm_freq=1000):
        # Enable / Standby Pin
        self.stby_a = Pin(stby_a, Pin.OUT)
        self.stby_b = Pin(stby_b, Pin.OUT)

        # Direction Control Pins
        self.ain2 = Pin(ain2, Pin.OUT)
        self.ain1 = Pin(ain1, Pin.OUT)
        self.bin1 = Pin(bin1, Pin.OUT)
        self.bin2 = Pin(bin2, Pin.OUT)
        
        # PWM Speed Pins
        self.pwma = PWM(Pin(pwma))
        self.pwmb = PWM(Pin(pwmb))
        
        self.pwma.freq(pwm_freq)
        self.pwmb.freq(pwm_freq)
        
        # Enable driver active state
        self.enable('A')
        self.enable('B')

    def enable(self,motor):
        """Enable driver (Exit Standby)."""
        if motor == 'A':
            self.stby_a.value(1)
        elif motor == 'B':
            self.stby_b.value(1)
        elif motor == 'AB':
            self.stby_a.value(1)
            self.stby_b.value(1)

    def disable(self,motor):
        """Disable driver (Enter Low-Power Standby)."""
        if motor == 'A':
            self.stby_a.value(0)
        elif motor == 'B':
            self.stby_b.value(0)
        elif motor == 'AB':
            self.stby_a.value(0)
            self.stby_b.value(0)

    def motor_a(self, speed):
        """
        Set Motor A speed and direction.
        speed: Range from -100 (Full Reverse) to 100 (Full Forward).
               0 applies a short brake.
        """
        speed = max(-100, min(100, speed))
        # Scale speed % to MicroPython 16-bit PWM duty cycle (0..65535)
        duty = int((abs(speed) / 100) * 65535)
        
        if speed > 0:
            self.ain1.value(1)
            self.ain2.value(0)
        elif speed < 0:
            self.ain1.value(0)
            self.ain2.value(1)
        else:
            self.ain1.value(0)
            self.ain2.value(0)  # Brake
            
        self.pwma.duty_u16(duty)

    def motor_b(self, speed):
        """
        Set Motor B speed and direction.
        speed: Range from -100 (Full Reverse) to 100 (Full Forward).
               0 applies a short brake.
        """
        speed = max(-100, min(100, speed))
        duty = int((abs(speed) / 100) * 65535)
        
        if speed > 0:
            self.bin1.value(1)
            self.bin2.value(0)
        elif speed < 0:
            self.bin1.value(0)
            self.bin2.value(1)
        else:
            self.bin1.value(0)
            self.bin2.value(0)  # Brake

        # From machine.PWM, get or set the current duty cycle of the PWM output,
        # as an unsigned 16-bit value in the range 0 to 65535 inclusive.
        self.pwmb.duty_u16(duty)

    def stop(self):
        """Brake both motors."""
        self.motor_a(0)
        self.motor_b(0)

def test_loop(driver):
    speedtests = [30]
    testduration = 10
    try:
        for i in range(len(speedtests)):
            print(f"\nMoving at {speedtests[i]}%")
            driver.motor_a(speedtests[i])
            driver.motor_b(speedtests[i])
            time.sleep(testduration)

        # Stop
        driver.stop()
        print("\nTest loop completed")

    except KeyboardInterrupt:
        driver.stop()
        driver.disable('AB')


# --- Usage Example ---
if __name__ == "__main__":
    driver = TB6612FNG()

    count = 0
    try:
        while count < 1:
            print(f"\nTest loop iteration {count + 1}")
            test_loop(driver)
            count += 1
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nUser interrupted execution.")
    finally:
        driver.stop()
        driver.disable('AB')
        print("Motors safely stopped and motor driver on STBY.")
