import logging
import grpc
from datetime import datetime, timezone
import csv
import grpc_pb2_grpc
import grpc_pb2
import argparse
from time import perf_counter,sleep


def run(ip):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    address = '{0}:5000'.format(ip)
    counter = 0
    with grpc.insecure_channel(address) as channel:
        stub = grpc_pb2_grpc.GRPCServiceStub(channel)

        while counter < 120:
            GetInfoFromServer(stub)
            counter += 1
            sleep(60)


def GetInfoFromServer(stub):
    
    sendTime = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    req  = grpc_pb2.Null()
    resp = None
    serverTime = stub.GetServerTime(req).timestamp

    recvTime = datetime.now().replace(tzinfo=timezone.utc).timestamp()

    with open('times.csv', 'a', newline='') as csvfile:
        writerObj = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writerObj.writerow([sendTime,serverTime,recvTime])
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('Hostname', nargs='?', default='localhost', help='IP address of server')

    args = parser.parse_args()
    logging.basicConfig()
    run(args.Hostname)