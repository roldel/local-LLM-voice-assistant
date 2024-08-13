from django.http import JsonResponse
from django.shortcuts import render
from .models import AudioRecording
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import os
from django.conf import settings

import requests
import ollama

from ollama import Client


def intro(request):
    return render(request,'audio_converter/intro.html')


@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"audio_{current_datetime}.wav"

        # upload_path = os.path.join('media', 'audio', audio_file.name)
        file_path = os.path.join(settings.MEDIA_ROOT,'input_audio', file_name)
        with open(file_path, 'wb') as file:
            for chunk in audio_file.chunks():
                file.write(chunk)

        server_feedback_message = 'Audio file uploaded successfully ! File save as : '+file_name

        stt_url = f"http://speech-to-text:5000/transcribe/{file_name}"
        response = requests.get(stt_url)

        if response.status_code == 200:
            stt_response = response.json()
            transcription_text = stt_response.get('text', '')
            #server_feedback_message += f" Transcription: {transcription_text}"



            client = Client(host='http://local-llm:11434')
            llm_response = client.chat(model='gemma:2b', messages=[{'role': 'user','content': transcription_text}])
            #llm_response = ollama.generate(model='gemma:2b', prompt='Why is the sky blue?')
            llm_feedback = (llm_response['message']['content'])


        else:
            server_feedback_message += " Error: Failed to retrieve data from the Flask app."

        return JsonResponse({'message': server_feedback_message, 'transcription': transcription_text, 'llmfeedback' : llm_feedback })
    else:
        return JsonResponse({'message': 'No audio file found'}, status=400)


'''
@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES['audio']:
        audio = request.FILES['audio']
        AudioRecording.objects.create(audio=audio)
        return JsonResponse({'message': 'File uploaded successfully'})
    return JsonResponse({'error': 'No file part'})
'''