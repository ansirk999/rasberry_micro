import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def ukur_jarak():
    GPIO.output(TRIG, False)
    time.sleep(0.00001)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    durasi = stop - start
    jarak = durasi * 34300 / 2

    return jarak

try:
    while True:
        d = ukur_jarak()
        print(f"Jarak: {d:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")
    GPIO.cleanup()