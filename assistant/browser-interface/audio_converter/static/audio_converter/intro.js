let mediaRecorder;
let chunks = [];

const startRecordButton = document.getElementById('startRecord');
const stopRecordButton = document.getElementById('stopRecord');
const serverFeedback = document.getElementById('serverFeedback');
const audioFeedback = document.getElementById('audioFeedback');

const transcription = document.getElementById('transcription');
const llmfeedback = document.getElementById('llmfeedback');

startRecordButton.addEventListener('click', function() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(stream) {
      mediaRecorder = new MediaRecorder(stream);
      chunks = [];

      mediaRecorder.ondataavailable = function(event) {
        chunks.push(event.data);
      };

      mediaRecorder.onstop = function() {
        const audioBlob = new Blob(chunks, { type: 'audio/wav' });

        const uploadURL = '/upload-audio';
        const formData = new FormData();
        formData.append('audio', audioBlob, 'audio_recording.wav');

        fetch(uploadURL, {
          method: 'POST',
          body: formData
        })
        .then(function(response) {
          console.log('Audio sent to server:', response);
          return response.json();
        })
        .then(function(data) {
          console.log(data);
          // Display the returned JSON message in <p> elements
          serverFeedback.textContent = data.message;
          transcription.textContent = data.transcription;
          llmfeedback.textContent = data.llmfeedback;
          audioFeedback.textContent = data.audio_filename;

          // Construct the download URL
          const audioDownloadURL = `http://localhost:8000/media/output_audio/${data.audio_filename}`;
          
          // Automatically download the audio file
          const downloadLink = document.createElement('a');
          downloadLink.href = audioDownloadURL;
          downloadLink.download = data.audio_filename;
          document.body.appendChild(downloadLink);
          downloadLink.click();
          document.body.removeChild(downloadLink);

          // Play the audio automatically in the browser
          const audioElement = new Audio(audioDownloadURL);
          audioElement.play();
        })
        .catch(function(error) {
          console.error('Error sending audio:', error);
        });
      };

      mediaRecorder.start();
      startRecordButton.disabled = true;
      stopRecordButton.disabled = false;
    })
    .catch(function(error) {
      console.error('Error accessing microphone:', error);
    });
});

stopRecordButton.addEventListener('click', function() {
  mediaRecorder.stop();
  startRecordButton.disabled = false;
  stopRecordButton.disabled = true;
});
