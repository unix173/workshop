import socket
import sys


# TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding socket to port
server_address = ('172.18.50.32', 10000)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >> sys.stderr, 'wait for a connection'
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address
        while True:
            data = connection.recv(20)
            if data == 'mtrack_start':
                # start video tracking
                print("Started")
            elif data == 'mtrack_stop':
                # stop video recording
                print("Stopped")
            elif data == 'stream_start':
                # start video streaming
                print("Stream started")
            elif data == 'stream_stop':
                # stop video streaming
                print("Streaming stopped")
    except Exception as e:
        print("Error {}".format(e.message))
    finally:
        connection.close()
