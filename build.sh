#!/bin/bash
SRC_DIR=`pwd`

DEST_DIR=`pwd`

protoc -I=$SRC_DIR --python_out=$DEST_DIR $SRC_DIR/config.proto