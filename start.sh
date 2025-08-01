#!/bin/bash

echo "Starting Virtual Patient Generator..."

OS="$(uname)"
IS_WINDOWS=false

if [[ "$OS" == "Darwin" ]]; then
  PLATFORM="macOS"
elif [[ "$OS" == "Linux" ]]; then
  PLATFORM="Linux"
elif grep -qi "mingw" <<< "$OS" || grep -qi "msys" <<< "$OS"; then
  PLATFORM="Windows"
  IS_WINDOWS=true
else
  PLATFORM="Unknown"
fi

echo "Detected OS: $PLATFORM"

if $IS_WINDOWS; then
  source venv/Scripts/activate
else
  source venv/bin/activate
fi

export GOOGLE_API_KEY="your_real_api_key_here"

echo "Starting backend..."
python app.py &
FLASK_PID=$!

sleep 3

echo "Opening frontend interface..."
if [[ "$PLATFORM" == "macOS" ]]; then
  open index.html
elif [[ "$PLATFORM" == "Linux" ]]; then
  xdg-open index.html
elif $IS_WINDOWS; then
  cmd.exe /C start index.html
else
  echo "Unsupported OS for auto browser launch."
fi

echo "System started"
echo "Flask backend running at: http://127.0.0.1:5001"
echo "Press Ctrl+C to stop server"

wait $FLASK_PID
