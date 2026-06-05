from gtts import gTTS
import os

os.makedirs("suara", exist_ok=True)

# List file yang dibutuhin
files = {
    "ding": "Ding dong",
    "antrian": "Nomor antrian",
    "silakan-ke": "silakan menuju ke",
    "a": "A",
    "b": "B", 
    "c": "C",
    "loket1": "loket satu",
    "loket2": "loket dua", 
    "loket3": "loket tiga",
    "loket4": "loket empat",
    "loket5": "loket lima"
}

# Generate file dasar
for nama, teks in files.items():
    tts = gTTS(text=teks, lang='id', slow=False)
    tts.save(f"suara/{nama}.mp3")
    print(f"Done: {nama}.mp3")

# Generate nomor 1-200
for i in range(1, 201):
    teks = str(i)
    if i == 1: teks = "satu"
    elif i == 11: teks = "sebelas"
    elif i == 12: teks = "dua belas"
    elif i < 20: teks = f"{i-10} belas"
    elif i % 10 == 0: teks = f"{int(i/10)} puluh"
    
    tts = gTTS(text=teks, lang='id', slow=False)
    tts.save(f"suara/nomor-{i}.mp3")
    if i % 20 == 0: print(f"Done sampai nomor-{i}.mp3")

print("\nSELESAI! Semua file ada di folder /suara")