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

        while True:
            q = input("Yapmak istediğiniz işlem?\nd(Sesi dinle) - k(Sesi kaydet) - q(Geri) -> ").lower()
            if q == "d":
                print(f"\n{'*'*41} Ses çalınıyor... {'*'*41}\n")
                sd.play(sound, fs)
                sd.wait()
            elif q == "k":
                save = input("\nDosya kaydediliyor.. Dosya adı (Boş bırakırsanız, dosya otomatik olarak girdiğiniz metin olarak adlandırılacaktır): ") == ""
                if save:
                    path = save_sound(sound, fs, user_text)
                else:
                    path = save_sound(sound, fs, save)
                print(f"\nBaşarıyla kaydedildi.\nKonum: {path}\n")
            elif q == "q":
                break
            else:
                print("\nHatalı giriş!\n")
        print(f"\n{'*'*100}\n")