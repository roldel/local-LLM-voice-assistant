- Project overview
- Fine tune steps

## STEP 1 PAROT

1. Evaluate speech to text models options and set up selected one

2. Create web interface to collect user audio sample and push it within request to server

3. Django server side request with file management processing, saves the file temporarily

4. Process user audio sample into STT model, print out audio sample to text

5. Render the input audio text as audio, text to speech

6. Return server response containing response audio

7. Play the audio response in the browser

Docker compose packaging as needed