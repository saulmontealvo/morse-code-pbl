from machine import Pin
from machine import I2C
from pico_i2c_lcd import I2cLcd
import time

i2c = I2C(id=1,scl=Pin(3),sda=Pin(2),freq=100000)
lcd = I2cLcd(i2c,0x27,2,16)
simple_led = Pin(15, Pin.OUT)
button = Pin(13,Pin.IN, Pin.PULL_UP)

data = {
  "A": [1,0,1,1,1],
  "B": [1,1,1,0,1,0,1,0,1],
  "C": [1,1,1,0,1,0,1,1,1,0,1],
  "D": [1,1,1,0,1,0,1],
  "E": [1],
  "F": [1,0,1,0,1,1,1,0,1],
  "G": [1,1,1,0,1,1,1,0,1],
  "H": [1,0,1,0,1,0,1],
  "I": [1,0,1],
  "J": [1,0,1,1,1,0,1,1,1,0,1,1,1],
  "K": [1,1,1,0,1,0,1,1,1],
  "L": [1,0,1,1,1,0,1,0,1],
  "M": [1,1,1,0,1,1,1],
  "N": [1,1,1,0,1],
  "O": [1,1,1,0,1,1,1,0,1,1,1],
  "P": [1,0,1,1,1,0,1,1,1,0,1],
  "Q": [1,1,1,0,1,1,1,0,1,0,1,1,1],
  "R": [1,0,1,1,1,0,1],
  "S": [1,0,1,0,1],
  "T": [1,1,1],
  "U": [1,0,1,0,1,1,1],
  "V": [1,0,1,0,1,0,1,1,1],
  "W": [1,0,1,1,1,0,1,1,1],
  "X": [1,1,1,0,1,0,1,0,1,1,1],
  "Y": [1,1,1,0,1,0,1,1,1,0,1,1,1],
  "Z": [1,1,1,0,1,1,1,0,1,0,1],
  " ": [0,0,0,0,0,0,0],
  "nil": ""
}

wpm=20
unit = 1.2/wpm

def MultiAppend(database,value,howMany):
    for number in range(1,howMany+1):
        database.append(value)

def clearFunc():
    lcd.clear()
    simple_led.value(0)

def SingleWordMorse(Message):
    Message = Message.upper()
    split = list(Message)

    data_table = []

    for i in range(len(split)):
        letters = split[i]
        before = split[i-1] if i > 0 else "nil"
        after = split[i+1] if i < len(split) -1 else "nil"

        # print(f"Before: {before}, Current: {letters}, After: {after}")

        if letters == " ":
            MultiAppend(data_table,0,7)
        else:
            if data[after] == "": # Final Append
                data_table.extend(data[letters])
            else:
                if after == " ": # append without adding 3
                    data_table.extend(data[letters])
                else:
                    data_table.extend(data[letters])
                    MultiAppend(data_table,0,3)
               
                

    print(data_table,len(data_table))

    return data_table

def RunMorse(lines):
    BinaryMorse = SingleWordMorse(lines) # Returns the string as a list of 0s and 1s for the final message includes spaces and interletter spaces.
    currentWord = []

    lcd.move_to(0,0)
    lcd.putstr(f"{lines.upper()} in M.C")

    for number in BinaryMorse:
        time.sleep(unit)
        lcd.move_to(0,0)
        lcd.putstr(f"{lines.upper()} in M.C")
        currentWord.append(number)

        key = next((k for k, v in data.items() if v == currentWord),None)

        if number == 1:
            lcd.move_to(0,1)
            lcd.putstr("1 value")
            simple_led.value(1)
        else:
            lcd.move_to(0,1)
            lcd.putstr("0 value")
            simple_led.value(0)

    clearFunc()

RunMorse("Hello")