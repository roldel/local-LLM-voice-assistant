from flask import Flask, jsonify
import whisper
import os

# Initialize the Flask app
app = Flask(__name__)
app.config['TESTING'] = True

# Load the Whisper model once when the server starts
model = whisper.load_model("base.en")

# Define the base directory for audio files
BASE_DIR = "/shared/input_audio/"

# Define the endpoint
@app.route('/transcribe/<filename>', methods=['GET'])
def transcribe_audio(filename):
    # Construct the full file path
    file_path = os.path.join(BASE_DIR, filename)
    
    try:
        # Run the Whisper model on the provided file path
        result = model.transcribe(file_path)
        # Return the transcribed text as a JSON response
        print(result["text"])
        return jsonify({"text": result["text"]})
    except Exception as e:
        # Handle errors (e.g., file not found, transcription error)
        return jsonify({"error": str(e)}), 400


# Define a separate health check endpoint
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200



# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
