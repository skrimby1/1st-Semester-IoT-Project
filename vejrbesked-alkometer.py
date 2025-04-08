from machine import ADC, Pin, PWM, I2C
import utime
from ustrftime import strftime
from time import sleep
from machine import Pin
from gpio_lcd import GpioLcd
import requests
from WiFi import connectPC
import json
import utime
import network
import espnow

connectPC()


#Wii skal aktiveres til stationmode, for at få forbindelse
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

stationary_time = 0
reminder_interval = 30

esp1 = espnow.ESPNow()
esp1.active(True)

receiver_mac = b'\xc8.\x18\x15\x16\x14'  # Replace with receiver's MAC
esp1.add_peer(receiver_mac)

def send_besked():
    message = b"lås"
    try:
        esp1.send(receiver_mac, message)
        print("Message sent!")
    except Exception as e:
        esp1.send(receiver_mac, message)

def aflåsning():
    aflåsning(False)
    
def korrekt_kode():
    korrekt_kode(False)

def stillestående():
    stillestående(False)
    
def stillestående():
    while True:
        if esp1.any():
            msg = esp1.recv()  # Receive the message
            if msg:
                sender_mac, message = msg  # Unpack the messag
                if message == b"display":
                    stillestående = True  # Set flag to True if password matches
                    print("Været Stillestående i 30 sekunder")
                    lcd.clear()
                    lcd.putstr("Husk at låse!")
                    log_data("Husk at låse!")
                    sound_reminder()
                    break  # Exit the loop once correct password is receive
            

while True:
    if esp1.any():
        msg = esp1.recv()  # Receive the message
        if msg:
            sender_mac, message = msg  # Unpack the message
            if message == b"1934":
                korrekt_kode = True  # Set flag to True if password matches
                print("Korrekt kode!")
                break  # Exit the loop once correct password is receive
            elif message == b"aflåst":
                aflåsning = True
                print("Cykel Aflåst!")
                break

    utime.sleep(0.1)  # Small delay to avoid high CPU usage

def buzzer(pwm_object, frequency, tone_duration, silence_duration):
    pwm_object.duty(512)
    pwm_object.freq(frequency)
    sleep(tone_duration)
    pwm_object.duty(0)
    sleep(silence_duration)

def log_data(besked):
    with open('promillelog.txt','a') as f:
        formatteret_tid = "{:00}:{:00}".format(tid_nu // 100, tid_nu % 100)
        f.write(f"{formatteret_tid} - {besked}\n")
        
def alkodenied():
    buzzer(buzzer_pwm, 1000, 0.2, 0.2)
    buzzer(buzzer_pwm, 200, 0.2, 0.2)
    buzzer(buzzer_pwm, 1000, 0.2, 0.2)
    buzzer(buzzer_pwm, 200, 0.2, 0.2)
    buzzer(buzzer_pwm, 1000, 0.2, 0.2)
    buzzer(buzzer_pwm, 200, 0.2, 0.2)
    buzzer(buzzer_pwm, 1000, 0.2, 0.2)
    buzzer(buzzer_pwm, 200, 0.2, 0.2)
    buzzer(buzzer_pwm, 1000, 0.2, 0.2)
    buzzer(buzzer_pwm, 200, 0.2, 0.2)
def alkoaprooved():
    buzzer(buzzer_pwm, 1100, 0.1, 0.2)
    buzzer(buzzer_pwm, 1200, 0.1, 0.2)
    buzzer(buzzer_pwm, 1300, 0.1, 0.2)
    buzzer(buzzer_pwm, 1400, 0.1, 0.2)
    buzzer(buzzer_pwm, 1500, 0.8, 0.2)
def trykketknap(trykknap):
        if trykknap.value() == 0:
            lcd.putstr("Remove Battery!")
            lcd.move_to(0,0)
            buzzer(buzzer_pwm, 3000, 0.8, 0.2)
            buzzer(buzzer_pwm, 1000, 0.8, 0.2)
            buzzer(buzzer_pwm, 3000, 0.8, 0.2)
            buzzer(buzzer_pwm, 1000, 0.8, 0.2)
            buzzer(buzzer_pwm, 3000, 0.8, 0.2)
            buzzer(buzzer_pwm, 1000, 0.8, 0.2)
def aflåslyd():
    buzzer(buzzer_pwm, 200, 1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)
    buzzer(buzzer_pwm, 500, 0.1, 0.2)
    buzzer(buzzer_pwm, 1000, 0.1, 0.2)

lcd = GpioLcd(rs_pin=Pin(27), 
               enable_pin=Pin(25),
               d4_pin=Pin(33),
               d5_pin=Pin(32),
               d6_pin=Pin(21),
               d7_pin=Pin(22),
               num_lines=4, 
               num_columns=20)

snemand = bytearray([0b1110,
  0b10001,
  0b11011,
  0b10001,
  0b01110,
  0b10101,
  0b10101,
  0b01110,])
lcd.custom_char(0, snemand)

vejrforhold = bytearray([0b0000,
  0b00100,
  0b01010,
  0b01010,
  0b10001,
  0b10001,
  0b10001,
  0b01110,])

    
buzzer_pin = 15

buzzer_PIN = Pin(buzzer_pin, Pin.OUT)

buzzer_pwm = PWM(buzzer_pin, duty=0)

# Jo højere ao_pin value er, jo mere ethanol har den detected
AO_PIN = ADC(Pin(36))

# Set the ADC width (resolution) to 12 bits
AO_PIN.width(ADC.WIDTH_12BIT)

# Sætter dæmpningen til 11 dB, som gør vores input kan gå op til 3.3V, og ikke brænde af
AO_PIN.atten(ADC.ATTN_11DB)

#Når DO_pin er low (0), så har den detected gas. Når den er high (1), så er der ikke gas.
DO_PIN = (Pin(16, Pin.IN))

current_time = utime.localtime()

current_time_dansk = utime.time()

ugedag = current_time[6]

#Tid, gør så tiden tjekker for de næste 10 timer
current_time_utc = utime.time()

#+ 3600 sekunder, grundet vi skal i dansk tidszone
current_time_dansk = current_time_utc + 3600

end_time = current_time_dansk + 11 * 3600

#Utime
starttid = strftime("%Y-%m-%dT%H:%M:%SZ", utime.localtime(current_time_dansk))

sluttid = strftime("%Y-%m-%dT%H:%M:%SZ", utime.localtime(end_time))

currenttime = f"{starttid}/{sluttid}"

#############################################################################################################
response = requests.get(
        url = f'https://dmigw.govcloud.dk/v1/forecastedr/collections/harmonie_dini_sf/position?coords=POINT%2812.568%2055.676%29&crs=crs84&parameter-name=temperature-0m,precipitation-type&datetime={currenttime}&api-key=2c152c27-c9e5-437d-92ca-4200e4678d74')
print(response)
#Læs op på den her kode
a = response.text.split('\n')
a = a[1:-3]
print(''.join(a))
data = json.loads(''.join(a))

#Localtime er en tuple, hvilket er derfor den er strftime - da man ikke kan lave om på den ellers
tid_nu_str = strftime("%H%M", utime.localtime(current_time_dansk))

tid_nu = int(tid_nu_str)

temperatur = data['ranges']['temperature-0m']['values']

vejrforhold = data['ranges']['precipitation-type']['values']

#time temperatur data, data fra 1 til 10 time, -273.15 da det skal omdannes fra kelvin til celcius
tempdata = {
"temp1" : round (temperatur[1] - 273.15),
"temp2" : round (temperatur[2] - 273.15),
"temp3" : round (temperatur[3] - 273.15),
"temp4" : round (temperatur[4] - 273.15),
"temp5" : round (temperatur[5] - 273.15),
"temp6" : round (temperatur[6] - 273.15),
"temp7" : round (temperatur[7] - 273.15),
"temp8" : round (temperatur[8] - 273.15),
"temp9" : round (temperatur[9] - 273.15),
"temp10" : round (temperatur[10] - 273.15),
}

list_tempdata = list(tempdata.values())

for i in range(0,10):
    if aflåsning == True:
        if list_tempdata[i] <= 0:
            lcd.clear()
            lcd.move_to(7, 0)
            lcd.putstr('FROST')
            lcd.move_to(2, 1)
            lcd.putstr('PARK RESPONSIBLY')
            lcd.move_to(7, 3)
            lcd.putchar(chr(0))
            lcd.move_to(8, 3)
            lcd.putchar(chr(0))
            lcd.move_to(9, 3)
            lcd.putchar(chr(0))
            lcd.move_to(10, 3)
            lcd.putchar(chr(0))
            lcd.move_to(11, 3)
            lcd.putchar(chr(0))
            sleep(0.8)
            lcd.clear()
            sleep(0.8)
#Vejrforhold, altså regn, sne osv. 1-7 indikerer der er et vejrforhold,
vejrdata = {
"vejr1" : (vejrforhold[1]),
"vejr2" : (vejrforhold[2]),
"vejr3" : (vejrforhold[3]),
"vejr4" : (vejrforhold[4]),
"vejr5" : (vejrforhold[5]),
"vejr6" : (vejrforhold[6]),
"vejr7" : (vejrforhold[7]),
"vejr8" : (vejrforhold[8]),
"vejr9" : (vejrforhold[9]),
"vejr10" : (vejrforhold[10]),
}
    
for i in range(0,9):
    if list_tempdata[i] >= 30:
        print("Extreme Heat")
#Vejrforhold, altså regn, sne osv. 1-7 indikerer der er et vejrforhold,
vejrdata = {
"vejr1" : (vejrforhold[1]),
"vejr2" : (vejrforhold[2]),
"vejr3" : (vejrforhold[3]),
"vejr4" : (vejrforhold[4]),
"vejr5" : (vejrforhold[5]),
"vejr6" : (vejrforhold[6]),
"vejr7" : (vejrforhold[7]),
"vejr8" : (vejrforhold[8]),
"vejr9" : (vejrforhold[9]),
"vejr10" : (vejrforhold[10]),
}

list_vejrdata = list(vejrdata.values())
for i in range(0,10):
    if aflåsning == True:
        if list_vejrdata[i] == [1,2,3,4,5,6,7]:
            lcd.clear()
            lcd.move_to(2, 0)
            lcd.putstr('WEATHER DETECTED')
            lcd.move_to(2, 1)
            lcd.putstr('PARK RESPONSIBLY')
            lcd.move_to(6, 3)
            lcd.putchar(chr(1))
            lcd.move_to(7, 3)
            lcd.putchar(chr(1))
            lcd.move_to(8, 3)
            lcd.putchar(chr(1))
            lcd.move_to(9, 3)
            lcd.putchar(chr(1))
            lcd.move_to(10, 3)
            lcd.putchar(chr(1))
            lcd.move_to(11, 3)
            lcd.putchar(chr(1))
            lcd.move_to(12, 3)
            lcd.putchar(chr(1))
            sleep(0.8)
            lcd.clear()
            sleep(0.8)

if korrekt_kode == True:
    print("Analyzing date and time...")
    if tid_nu in range (0000,2359):
        if ugedag in range (0, 4):
            lcd.putstr("Breathalyzer test required!")
            log_data("Breathalyzer test recquired! - LCD Display")
            while True:
                print("Varmer op...")
                sleep(30)
                lcd.putstr("BLOW until end of the beep!")
                buzzer(buzzer_pwm, 512, 10, 0.2)
                promille_value = AO_PIN.read() #0-4095 aflæsning
                print(promille_value)
                log_data(promille_value)
                utime.ticks_ms(10)
                if promille_value > 2000:
                    lcd.putstr("You are too drunk!")
                    log_data("You are too drunk!")
                    alkodenied()
                    break
                elif promille_value < 2000:
                    lcd.putstr("You are good to go!")
                    log_data("You are good to go!")
                    alkoaprooved()
                    send_besked()
                    while True:
                        stillestående()
                    break