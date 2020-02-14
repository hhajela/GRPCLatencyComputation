import socket
import sys
from datetime import datetime, timedelta
import time
import csv
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('same-server', 10000)
message = 'MST'
send_time=[]
rec_time=[]
server_time=[]

try:

    # Send data
    print(sys.stderr, 'sending "%s"' % message)
    start_time=datetime.now()
    while (start_time+timedelta(hours=2))>=datetime.now():

        send_time.append(datetime.utcnow().timestamp())
        sent = sock.sendto(message.encode("utf-8"), server_address)
        # Receive response
        print(sys.stderr, 'waiting to receive')
        data, server = sock.recvfrom(4096)
        rec_time.append(datetime.utcnow().timestamp())
        server_time.append(float(data.decode()))
        print(send_time,server_time,rec_time)
        time.sleep(60)
    """
    with open("udp_same_client.csv","w") as udp_file:
        udp_writer = csv.writer(udp_file,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        for i in range(len(send_time)):
            udp_writer.writerow([send_time[i],server_time[i],rec_time[i]])
    """
finally:
    print(sys.stderr, 'closing socket')
    sock.close()
