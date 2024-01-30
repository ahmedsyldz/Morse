import os
import re
import numpy as np
import json
from scipy.io.wavfile import write

with open('morse_dict.json', 'r', encoding='utf-8') as file:
    MORSE_DICT = json.load(file)

def text_to_morse(text):
    cleaned_text = re.sub('[^A-Z0-9 ÇŞÜÖ._@?=;:/,+\(\)\'&$\"!-]', '', text.upper().replace('İ', 'I').replace('Ğ', 'G'))
    cleaned_text = re.sub('\s+', ' ', cleaned_text).strip()

    try: return [(i, MORSE_DICT[i]) for i in cleaned_text]
    except:
        print("Bir hata oluştu!")
        raise

def create_sound(morse_list, frequency=1000, unit_duration=0.1):
    fs = 44100
    sound = np.array([])
    
    for character, morse_code in morse_list:
        for signal in morse_code:
            if signal == '.':
                t = np.arange(0, unit_duration, 1/fs)
                sound = np.concatenate([sound, 0.5 * np.sin(2 * np.pi * frequency * t)])
                sound = np.concatenate([sound, np.zeros(int(fs * unit_duration))])
            elif signal == '-':
                t = np.arange(0, unit_duration*3, 1/fs)
                sound = np.concatenate([sound, 0.5 * np.sin(2 * np.pi * frequency * t)])
                sound = np.concatenate([sound, np.zeros(int(fs * unit_duration))])

        if character != ' ':
            sound = np.concatenate([sound, np.zeros(int(fs * unit_duration * 3))])
        else: 
            sound = np.concatenate([sound, np.zeros(int(fs * unit_duration * 6))])
            print()

    return sound, fs

def save_sound(sound, fs, file_name):
    file_name = f"{file_name}.wav"
    write(file_name, fs, (sound * 32767).astype(np.int16))
    return os.path.abspath(file_name)