#!/bin/bash

# Check if the audio file argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./upload_audio.sh <audio_file_path>"
    exit 1
fi

audio_file_path="$1"
csrftoken="2ZMY4PQm6Onw0cgvEW3ZrybfBdhzaUOm"

curl -X POST \
  -F "files=@${audio_file_path}" \
  --cookie "csrftoken=${csrftoken}" \
  -H "X-CSRFToken: ${csrftoken}" \
  localhost:8000/songs/api/upload/
