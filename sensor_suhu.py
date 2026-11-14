import board
import adafruit_dht
import time

# Gunakan GPIO04 (pin fisik 7)
dht = adafruit_dht.DHT11(board.D4)

print("Pembacaan Sensor DHT11 (Suhu dan Kelembapan)")
print("Tekan Ctrl+C untuk berhenti")

try:
    while True:
        try:
            # Baca data suhu dan kelembapan
            suhu = dht.temperature      # derajat Celcius
            kelembapan = dht.humidity   # persen (%)
            
            if suhu is not None and kelembapan is not None:
                print(f"Suhu : {suhu:.1f} °C")
                print(f"Kelembapan : {kelembapan:.1f} %")
            else:
                print("Gagal membaca data dari DHT11.")
                
        except RuntimeError as error:
            # DHT seringkali error pembacaan, abaikan dan coba lagi
            time.sleep(2.0)
            continue
            
        time.sleep(2.0)

except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    dht.exit()