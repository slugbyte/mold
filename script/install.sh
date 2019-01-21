#!/usr/bin/env bash
echo 'Compressing asset/mold_root'
tar -vczf ./mold/asset/mold_root.tar.gz ./mold/asset/mold_root

echo 'Running installer'
python3 ./setup.py install
