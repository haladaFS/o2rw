#!/bin/bash

./get_changes.sh
python read.py
./translate.sh
./update_refs.sh
./build.sh

