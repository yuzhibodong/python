#!/bin/bash

# 如果非空/非0
if [ -n "$1" ]; then
    ./manage.py makemigrations $1
else
    ./manage.py makemigrations
fi
