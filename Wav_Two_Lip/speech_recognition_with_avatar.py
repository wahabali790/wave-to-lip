import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
import pygame
import cv2

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio_data = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio_data).lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
        return None

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    # Use pydub to convert the mp3 to wav format
    sound = AudioSegment.from_mp3("output.mp3")
    sound.export("output.wav", format="wav")
    # Use pygame.mixer to play the wav file
    pygame.mixer.init()
    pygame.mixer.music.load("output.wav")
    #pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Ensure that the pygame mixer has finished playing before removing the file
    pygame.mixer.quit()
    # Remove the file
    os.remove("output.mp3")
    #os.remove("output.wav")
    
    
    

    # Specify the result directory
    result_dir = "./result6666"

    # Delete .mp4 files from the result directory
    mp4_files = [f for f in os.listdir(result_dir) if f.endswith(".mp4")]
    for mp4_file in mp4_files:
        file_path = os.path.join(result_dir, mp4_file)
        os.remove(file_path)

    # Construct the inference command
    inference_command = f"python inference.py --checkpoint_path ./checkpoints/wav2lip_gan.pth --face E:/lipnet_project/Wav2Lip/women_face.jpg --audio E:/lipnet_project/Wav2Lip/output.wav "

    # Run the inference command
    os.system(inference_command)

    
    
import csv
import datetime

def main():
    paragraph = "apple testing sample"  # Replace with your paragraph
    word_list = paragraph.split()
    current_index = 0
    with open("word_accuracy.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Time', 'Word', 'Accuracy'])  # Added 'Time' column
        while current_index < len(word_list):
            word = word_list[current_index]
            print(f"Avatar: Say the word '{word}'.")
            user_response = recognize_speech()
            if user_response and word in user_response:
                print("Avatar: Well done! You pronounced it correctly.")
                csv_writer.writerow([datetime.datetime.now(), word, 'Correct'])  # Added current time
                current_index += 1
            else:
                print(f"Avatar: Please repeat the word '{word}'.")
                csv_writer.writerow([datetime.datetime.now(), word, 'Incorrect'])  # Added current time
                prompt = f"Repeat '{word}'."
                text_to_speech(prompt)



if __name__ == "__main__":
    main()



