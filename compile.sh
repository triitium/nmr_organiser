#!/bin/bash
pyinstaller \
    --name NMRorganiser \
    --add-data "data:./data" \
    --icon=accessory/favicon.ico \
    __main__.py