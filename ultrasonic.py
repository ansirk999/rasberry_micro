import RPi.GPIO as GPIO
import time

# Konfigurasi penomoran pin BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23  # Pin Fisik 16
ECHO = 24  # Pin Fisik 18 (melalui pembagi tegangan 1k & 2k Ohm)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def ukur_jarak():
    # Pastikan pin TRIG rendah terlebih dahulu
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Kirim pulsa pemicu selama 10 mikrodetik
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    batas_waktu = time.time() + 0.04  # Timeout 40 ms (~6.8 meter)
    waktu_mulai = time.time()
    waktu_selesai = time.time()

    # Tunggu pin ECHO berubah menjadi HIGH
    while GPIO.input(ECHO) == 0:
        waktu_mulai = time.time()
        if waktu_mulai > batas_waktu:
            return None

    # Tunggu pin ECHO kembali menjadi LOW
    while GPIO.input(ECHO) == 1:
        waktu_selesai = time.time()
        if waktu_selesai > batas_waktu:
            return None

    durasi = waktu_selesai - waktu_mulai
    # Kecepatan suara = 34300 cm/s, dibagi 2 karena bolak-balik
    jarak_cm = (durasi * 34300) / 2
    return round(jarak_cm, 2)

try:
    print("Memulai pembacaan sensor HC-SR04... Tekan Ctrl+C untuk berhenti.")
    while True:
        hasil = ukur_jarak()
        if hasil is not None and 2 <= hasil <= 400:
            print(f"Jarak terukur: {hasil} cm")
        else:
            print("Di luar jangkauan atau periksa sambungan kabel ECHO/TRIG.")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nPengujian dihentikan oleh pengguna.")
finally:
    GPIO.cleanup()