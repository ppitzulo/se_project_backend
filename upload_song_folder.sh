#!/bin/bash

# Check if the audio file argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./upload_audio.sh <audio_file_path>"
    exit 1
fi

song_folder="$1"
csrftoken="2ZMY4PQm6Onw0cgvEW3ZrybfBdhzaUOm"

for SONG_FILE in "${song_folder}"/*; do
	if [ -f "${SONG_FILE}" ]; then
    echo "Uploading ${SONG_FILE}..."
    curl -X POST \
      -F "files=@${SONG_FILE}" \
      --cookie "csrftoken=${csrftoken}" \
      -H "X-CSRFToken: ${csrftoken}" \
      localhost:8000/songs/upload/
  fi
done
