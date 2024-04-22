import socket
import time

HOST = "10.0.0.1"
PORT = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    message = ""
    pings = 0
    min = 1.0
    max = 0.0
    total = 0

    for x in range(10):
        s.settimeout(1.0)
        message = "Ping " + str(x + 1)
        byte_msg = message.encode('utf-8')
        
        start = time.time()
        s.sendall(byte_msg)
        
        try:
            data = s.recvfrom(1024)
            end = time.time()
            diff = round((end - start), 5)
            print(str(data[0].decode('utf-8')) + ": rtt = " + str(diff) + " ms")
            
            pings += 1
            if diff < min:
                min = diff

            if diff > max:
                max = diff

            total += diff
        except socket.timeout:
            print("Ping " + str(x+1) + ': REQUEST TIMED OUT')
    
    print("Summary values:")
    print("min_rtt = " + str(min) + " ms")
    print("max_rtt = " + str(max) + " ms")
    print("avg_rtt = " + str(round((total/pings), 5)) + " ms")
    print("Packet loss: " + str(10 - pings) + "0.00%")
