from flask import Flask, request, jsonify
import subprocess
import os
from datetime import datetime

app = Flask(__name__)

# Directory to save the output audio files
OUTPUT_DIR = "/shared/output_audio"

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def text_to_speech(text):
    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"audio_{timestamp}.wav")
    
    # Use espeak to generate speech and save it to the WAV file
    command = ["espeak", text, "--stdout", "-w", output_file]
    subprocess.run(command, check=True)
    
    return output_file

@app.route('/tts', methods=['POST'])
def tts():
    # Get the text from the POST request
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    
    try:
        # Generate the audio file
        audio_file = text_to_speech(text)
        
        # Return the filename in the response
        filename = os.path.basename(audio_file)
        return jsonify({"filename": filename}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)





'''
import subprocess

def text_to_speech(text):
    # Define the output WAV file
    output_file = "audio.wav"
    
    # Use espeak to generate speech and save it to the WAV file
    command = ["espeak", text, "--stdout", "-w", output_file]
    subprocess.run(command, check=True)
    
    print(f"Saved the speech to {output_file}")

text = "This text is gonna be a longer paragraph and we will see how the processor can manage it, reasonable expectations, let's just see how it behaves"
text_to_speech(text)
'''