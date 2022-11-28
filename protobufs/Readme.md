# Protobuf 

## Generation
```
python3 -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. mtg_card.proto 
```

```bash
poetry run python3 -m grpc_tools.protoc -I ../protobufs  --python_out=. --grpc_python_out=. ../protobufs/mtg_card.proto
```