'''
main.py is executed automatically after boot.py. 

It contains the primary logic for controlling the robot's motors using the TB6612FNG motor driver.
'''

from machine import Pin, PWM, UART
import time

class TB6612FNG:
    def __init__(self, stby_a=0, stby_b=7 ,ain1=2, ain2=3, bin1=4, bin2=5, pwma=1, pwmb=6, pwm_freq=1000):
        # Enable / Standby Pin
        self.stby_a = Pin(stby_a, Pin.OUT)
        self.stby_b = Pin(stby_b, Pin.OUT)

        # Direction Control Pins
        self.ain1 = Pin(ain1, Pin.OUT)
        self.ain2 = Pin(ain2, Pin.OUT)
        self.bin1 = Pin(bin1, Pin.OUT)
        self.bin2 = Pin(bin2, Pin.OUT)
        
        # PWM Speed Pins
        self.pwma = PWM(Pin(pwma))
        self.pwmb = PWM(Pin(pwmb))
        
        self.pwma.freq(pwm_freq)
        self.pwmb.freq(pwm_freq)
        
        # Enable driver active state
        self.enable('AB')

    def enable(self, motor):
        """Enable motor driver (Exit Standby)."""
        if motor in ['A', 'AB']:
            self.stby_a.value(1)
        if motor in ['B', 'AB']:
            self.stby_b.value(1)

    def disable(self, motor):
        """Disable motor driver (Enter Low-Power Standby)."""
        if motor in ['A', 'AB']:
            self.stby_a.value(0)
        if motor in ['B', 'AB']:
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
            self.ain1.value(0)
            self.ain2.value(1)
        elif speed < 0:
            self.ain1.value(1)
            self.ain2.value(0)
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
        FLIP_ORIENTATION = True  # Flip orientation of motor B to match motor A
        if FLIP_ORIENTATION:
            speed = -speed
        speed = max(-100, min(100, speed))
        duty = int((abs(speed) / 100) * 65535)

        if speed > 0:
            self.bin1.value(0)
            self.bin2.value(1)
        elif speed < 0:
            self.bin1.value(1)
            self.bin2.value(0)
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

#%% Movement functions for operation
def test_loop(driver):
    speedtests = [15,30]
    testduration = 1
    try:
        for i in range(len(speedtests)):
            print(f"Moving at {speedtests[i]}%")
            driver.motor_a(speedtests[i])
            driver.motor_b(-speedtests[i])
            time.sleep(testduration)

            driver.motor_a(-speedtests[i])
            driver.motor_b(speedtests[i])
            time.sleep(testduration)

        # Stop
        driver.stop()
        print("\nTest loop completed")

    except KeyboardInterrupt:
        driver.stop()
        driver.disable('AB')

def execute_command(cmd, driver, speed=40):
    """Map single character commands to motor movements."""
    if cmd == 'F': # or cmd == 'Forward':
        driver.motor_a(speed)
        driver.motor_b(speed)
    elif cmd == 'B': # or cmd == 'Backward':
        driver.motor_a(-speed)
        driver.motor_b(-speed)
    elif cmd == 'L': # or cmd == 'Left':
        # Pivot left: Motor A backward, Motor B forward
        driver.motor_a(-speed)
        driver.motor_b(speed)
    elif cmd == 'R': # or cmd == 'Right':
        # Pivot right: Motor A forward, Motor B backward
        driver.motor_a(speed)
        driver.motor_b(-speed)
    elif cmd == 'S': # or cmd == 'Stop':
        driver.stop()
    else:
        print(f"Unknown command: {cmd}")


def main():
    driver = TB6612FNG()

    # Test loop to verify motor functionality
    TEST_LOOP_ENABLED = False  # Set to False to skip the test loop
    if TEST_LOOP_ENABLED:
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

    # Manual control loop for receiving commands via UART
    UART_ID = 1
    TX_PIN = 20 
    RX_PIN = 21 

    uart = UART(UART_ID, baudrate=115200, tx=Pin(TX_PIN), rx=Pin(RX_PIN))
    print("Motors initialized for UART communication. Listening on UART...")
    driver.enable('AB')  # Ensure motors are enabled for manual control
    
    try:
        while True:
            # Non-blocking check for available UART data
            if uart.any():
                # Read the line, decode it, and strip the newline character
                data = uart.readline().decode('utf-8').strip()
                if data:
                    print(f"Received: {data}")
                    execute_command(data, driver)
            
            # Small delay to prevent the loop from maxing out the CPU
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
    finally:
        driver.stop()
        driver.disable('AB')
        print("Motors safely stopped.")



main()

