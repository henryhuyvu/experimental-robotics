import io
import socketserver
from http.server import BaseHTTPRequestHandler
from picamera2 import Picamera2
from picamera2.encoders import MJPEGEncoder
from picamera2.outputs import FileOutput
from threading import Condition
from uart_sender import UARTSender

# Initialize UART Sender
uart = UARTSender()

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()
        return len(buf)

class StreamingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('static/index.html', 'rb') as f:
                self.wfile.write(f.read())
                
        elif self.path == '/script.js':
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            with open('static/script.js', 'rb') as f:
                self.wfile.write(f.read())
                
        elif self.path == '/stream':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.wfile.write(b'Content-Type: image/jpeg\r\n')
                    self.wfile.write(b'Content-Length: ' + str(len(frame)).encode() + b'\r\n\r\n')
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                print(f'Client disconnected from stream: {self.client_address[0]}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/command':
            content_length = int(self.headers['Content-Length'])
            command = self.rfile.read(content_length).decode('utf-8')
            
            # Send the received command directly to the Pico via UART
            uart.send_command(command)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Command received")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress standard HTTP logging to keep console clean
        pass

# Use ThreadingHTTPServer so stream holds don't block motor commands
class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    from libcamera import Transform  # Import Transform from libcamera

    cam_dimensions_min = (640, 480)
    cam_dimensions_max = (3280, 2464)
    picam2 = Picamera2()
    config = picam2.create_video_configuration(
        main={"size": cam_dimensions_min}, 
        transform=Transform(),
    )
    picam2.configure(config)
    
    output = StreamingOutput()
    encoder = MJPEGEncoder()
    picam2.start_recording(encoder, FileOutput(output))
    
    try:
        server_address = ('', 8000)
        httpd = ThreadedHTTPServer(server_address, StreamingHandler)
        print("Server running on port 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        picam2.stop_recording()
        picam2.close()
        print("Camera recording stopped and closed.")

