import sounddevice as sd
from morse import *

if __name__ == "__main__":
    while True:
        user_text = input("Lütfen bir metin giriniz (Çıkış için 'q'): ")
        if user_text.lower() == "q":
            break
        
        morse_list = text_to_morse(user_text)
        morse_code = " ".join([i[1] if i[1] != " " else "|" for i in morse_list])
        
        print(f"\nGirilen metin: {user_text}\nMorse kodu: {morse_code}\n")
        sound, fs = create_sound(morse_list)
        sd.play(sound, fs)
        sd.wait()
        
        save = input(f"Ses çalındı. Kaydetmek ister misiniz? (e, h): ") == "e"

        if save:
            path = save_sound(sound, fs, user_text)
            print(f"Başarıyla kaydedildi.\nKonum: {path}\n")
        print("*"*100)