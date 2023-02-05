import time
import socket
import itertools
import sys
import threading
import pyfiglet
HOST = input("Enter the target url : ")
PORT = range(1024)
DONE = False

title = pyfiglet.figlet_format("Scanner")
print(title)
 
print("-"*50)
print("Scanning Target : " , socket.gethostbyname(HOST))
print("-"*50)

def animate():
    for i in itertools.cycle(['|', '/', '-']):
        if DONE:
            break
        sys.stdout.write("\r scanning..." + i)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r Done')
        
def scan(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)

        try:
            s.connect((host, port))
            return True
        except:
            return False

def start(host, ports):
    for port in ports:
        if scan(host, port):
            print(f'port {port} is open')
    DONE = True

t = threading.Thread(target=animate)
t.start()
start(HOST, PORT)
