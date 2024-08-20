from flask import Flask, jsonify, request
import subprocess
import os
from datetime import datetime

app = Flask(__name__)
app.config['TESTING'] = True


# Define a separate health check endpoint
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200


@app.route('/tts', methods=['POST'])
def tts():

    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']

    # Directory to save the output audio files
    OUTPUT_DIR = "/shared/output_audio/"

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"audio_{timestamp}.wav"
    output_file = os.path.join(OUTPUT_DIR, filename)


    command = ["espeak", text, "-w", output_file]

    subprocess.run(command, check=True)
    print("File has been saved here : " + str (output_file))


    return jsonify({"filename": filename }), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
