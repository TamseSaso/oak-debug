#!/bin/sh
echo "Starting Backend (debugpy on :5678, waiting for client)"
exec python3.12 -m debugpy --listen 0.0.0.0:5678 /app/main.py