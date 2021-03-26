#!/bin/sh
install -Cdvm755 ~/.local/lib/python3.8/site-packages/stack-calc
install -Cv ./*.py ~/.local/lib/python3.8/site-packages/stack-calc
install -Cdvm777 ~/.local/bin
ln -svf ~/.local/lib/python3.8/site-packages/stack-calc/app.py ~/.local/bin/stack-calc
