from django.http import JsonResponse
from django.shortcuts import render
from .models import AudioRecording
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import os
from django.conf import settings


def intro(request):
    return render(request,'audio_converter/intro.html')


@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"audio_{current_datetime}.wav"

        # upload_path = os.path.join('media', 'audio', audio_file.name)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb') as file:
            for chunk in audio_file.chunks():
                file.write(chunk)

        server_feedback_message = 'Audio file uploaded successfully ! File save as : '+file_name
        return JsonResponse({'message': server_feedback_message })
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