from machine import Pin
import time

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
  " ": [0,0,0,0,0,0,0]
}

wpm=20
unit = 1.2/wpm

def MultiAppend(database,value,howMany):
    for number in range(1,howMany+1):
        database.append(value)

def SingleWordMorse(Message):
    Message = Message.upper()
    split = list(Message)

    data_table = []

    for i in range(len(split)):
        letters = split[i]
        before = split[i-1] if i > 0 else None
        after = split[i+1] if i < len(split) -1 else None

        print(f"Before: {before}, Current: {letters}, After: {after}")

        # if letters == " ":
        #     MultiAppend(data_table,0,7)
        # else:
        #         MultiAppend(data_table,0,3)
        #         data_table.extend(data[letters])
        if after == " ":
            data_table.append(0)
            data_table.append(0)
            data_table.append(0)
            data_table.extend(data[letters])
        else:
            if letters == " ":
                data_table.extend(data[letters])
            else:      
                MultiAppend(data_table,0,3)
                data_table.extend(data[letters])


    del data_table[:3]

    print(data_table)
    print(len(data_table))

    return data_table

# time.sleep(2)

SingleWordMorse("we go")