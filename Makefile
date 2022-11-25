.PHONY = pb2

SHELL := /bin/bash

VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

pb2:
	python3 -m venv env
	$(PIP) install grpcio grpcio-tools
	
	$(PYTHON) -m grpc_tools.protoc -I protobufs --python_out=srv_mtga_be --grpc_python_out=srv_mtga_be protobufs/mtg_card.proto
	$(PYTHON) -m grpc_tools.protoc -I protobufs --python_out=srv_mtga_fe --grpc_python_out=srv_mtga_fe protobufs/mtg_card.proto

	rm -r $(VENV)