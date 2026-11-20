import serial
import threading

class UARTSender:
    def __init__(self):
        # [PLACEHOLDER] Set your Pi Zero UART port and baudrate here.
        # /dev/serial0 is the default hardware serial port on Pi Zero.
        # Ensure you have enabled serial hardware in raspi-config.
        self.port = '/dev/serial0'
        self.baudrate = 115200
        self.lock = threading.Lock()
        
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"UART initialized on {self.port} at {self.baudrate} baud.")
        except Exception as e:
            print(f"Failed to initialize UART: {e}")
            self.ser = None

    def send_command(self, cmd):
        with self.lock:
            if self.ser and self.ser.is_open:
                try:
                    message = f"{cmd}\n".encode('utf-8')
                    self.ser.write(message)
                    self.ser.flush()
                    print(f"Sent via UART: {cmd}")  # Added for debugging
                except Exception as e:
                    print(f"UART Write Error: {e}")
            else:
                print(f"UART not connected. Simulated sending: {cmd}")
