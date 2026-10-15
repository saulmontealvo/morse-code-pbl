from machine import Pin
import time

simple_led = Pin(15, Pin.OUT)
button = Pin(13,Pin.IN, Pin.PULL_UP)

data = {
  "A": [0,1],
  "B": [1,0,0,0],
  "C": [1,0,1,0],
  "D": [1,0,0],
  "E": [0],
  "F": [0,0,1,0],
  "G": [1,1,0],
  "H": [0,0,0,0],
  "I": [0,0],
  "J": [0,1,1,1],
  "K": [1,0,1],
  "L": [0,1,0,0],
  "M": [1,1],
  "N": [1,0],
  "O": [1,1,1],
  "P": [0,1,1,0],
  "Q": [1,1,0,1],
  "R": [0,1,0],
  "S": [0,0,0],
  "T": [1],
  "U": [0,0,1],
  "V": [0,0,0,1],
  "W": [0,1,1],
  "X": [1,0,0,1],
  "Y": [1,0,1,1],
  "Z": [1,1,0,0]
}

wpm=5
unit = 1.2/wpm

def visual(thg):
  list = []
  
  for tif in thg:
    if tif == 1:
      list.append("-")
    else:
      list.append(".")
  print(list)  

def SingleWordMorse(Message):
    Message = Message.upper()
    split = list(Message)

    data_table = []

    for letters in split: # For Loop Letters from string ["P", "A", "R", "I", "S", ""]
      if letters == " ":
        print("appending space")
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)
      else:
        print("appending binary letter: " + letters)
        data_table.append(0)
        data_table.append(0)
        data_table.append(0)

        binary_data = data[letters]
        for doe_state in binary_data:
          data_table.append(0)
          if doe_state == 0:
            data_table.append(1)
          elif doe_state == 1:
            data_table.append(1)
            data_table.append(1)
            data_table.append(1)

    print(data_table)


SingleWordMorse("PARIS ")