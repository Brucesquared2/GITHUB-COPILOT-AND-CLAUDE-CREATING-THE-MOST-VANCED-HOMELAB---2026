#!/bin/bash
set -e
echo "[QS] Building all images..."
docker-compose build
echo "[QS] Starting core infrastructure..."
docker-compose up -d
echo "[QS] Running TUI CLI --"
make tui