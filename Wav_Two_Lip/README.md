# Wave2Lip

## Description
This GitHub repository utilizes Wave2Lip and a speech recognition library. Wave2Lip takes audio and an image of an avatar and creates a video in which the avatar speaks the voice. The speech recognition library recognizes words pronounced by a patient. When a patient speaks a word, the system checks if the word is pronounced accurately. If the patient struggles with pronunciation, an avatar is generated, and the avatar will pronounce the word until the patient successfully pronounces it. Once the word is pronounced accurately, the system proceeds to the next word.

- python 3.9.13
## Weights
- Download `wav2lip_gan.pth` from [Drive Link](https://drive.google.com/file/d/1Zi1e9A54rs_vq9gZgKV6SDQ1s-W-Lvw0/view?usp=sharing) and place it in `checkpoint/wav2lip_gan.pth` folder.
- Download `s3fd.pth` from [Drive Link](https://drive.google.com/file/d/1Hf3W1KMmdNhumBNTrZFeXZK53ATcU8tS/view?usp=sharing) and place it in `face_detection/detection/sfd/s3fd.pth`.

## Command
To run the program, execute the following command:
```bash
python speech_recognition_with_avatar.py
```
