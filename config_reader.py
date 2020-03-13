import config_pb2

config = config_pb2.Config()

with open("exported.config") as f:
    config.ParseFromString(f.read())

print( config.accounts[0].username )
