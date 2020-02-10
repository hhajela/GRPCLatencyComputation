
import grpc_pb2_grpc
import grpc_pb2
import grpc
from concurrent import futures
from datetime import datetime, timezone
import logging
import io


class GRPCServiceServicer(grpc_pb2_grpc.GRPCServiceServicer):

    def GetServerTime(self, request, context):

        # return current UTC Time
        response = grpc_pb2.Timestamp()
        response.timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_GRPCServiceServicer_to_server(GRPCServiceServicer(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()