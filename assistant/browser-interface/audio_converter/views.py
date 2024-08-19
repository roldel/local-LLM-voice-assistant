from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import os
from django.conf import settings

import requests
import ollama

from ollama import Client


# Main page
def intro(request):
    return render(request,'audio_converter/intro.html')


# Endpoint
#
# EXPECT POST request with audio file
# RETURNS LLM text answer + audio answer .wav file location for client download initiation
#
@csrf_exempt
def upload_audio(request):
    # CHECK valid request
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']

        # SAVE request audio file in /shared/input_audio/

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"audio_{timestamp}.wav"

        file_path = os.path.join(settings.MEDIA_ROOT,'input_audio', file_name)
        with open(file_path, 'wb') as file:
            for chunk in audio_file.chunks():
                file.write(chunk)
        server_feedback_message = 'Audio file uploaded successfully ! File save as : '+file_name

        # STT operation
        stt_url = f"http://speech-to-text:5000/transcribe/{file_name}"
        response = requests.get(stt_url)

        # FEED client text request to local LLM
        if response.status_code == 200:
            stt_response = response.json()
            transcription_text = stt_response.get('text', '')

            client = Client(host='http://local-llm:11434')
            llm_response = client.chat(model='gemma:2b', messages=[{'role': 'user','content': transcription_text}])
            llm_feedback = (llm_response['message']['content'])

            # TTS step
            tts_url = "http://text-to-speech:6000/tts"
            data = {'text': llm_feedback }

            try:
                tts_feedback = requests.post(tts_url, json = data)

                if tts_feedback.status_code == 200:
                # Get the filename from the response
                    result = tts_feedback.json()
                    print(result)
                    tts_filename = result.get('filename')
                    print("the filename result from TTS is : "+ str(tts_filename))
                    #return JsonResponse({"filename": result.get('filename')}, status=200)

                else:
                    return JsonResponse({"error": "Failed to process text-to-speech"}, status=response.status_code)

            except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
                return JsonResponse({"error": str(e)}, status=500)



        else:
            server_feedback_message += " Error: Failed to retrieve data from the Flask app."

        return JsonResponse({'message': server_feedback_message, 'transcription': transcription_text, 'llmfeedback' : llm_feedback, 'audio_filename' : tts_filename })
    else:
        return JsonResponse({'message': 'No audio file found'}, status=400)
