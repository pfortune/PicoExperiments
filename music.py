from machine import PWM, Pin
from time import sleep

MusicNotes = {"B0": 31, "C1": 33,"CS1": 35,"D1": 37,"DS1": 39,"E1": 41,"F1": 44,"FS1": 46,"G1": 49,"GS1": 52,"A1": 55,"AS1": 58,"B1": 62,
"C2": 65,"CS2": 69,"D2": 73,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,"GS2": 104,"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,"C4": 262,"CS4": 277,"D4": 294,
"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,
"E5": 659,"F5": 698,"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1324,
"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,"A6": 1760,"AS6": 1865,"B6": 1976,"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,
"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978}


mario = ["E7", "E7", "0", "E7", "0", "C7", "E7", "0", "G7", "0", "0", "0", "G6", "0", "0", "0", "C7", "0", "0", "G6", "0", "0", "E6",
         "0", "0", "A6", "0", "B6", "0", "AS6", "A6", "0", "G6", "E7", "0", "G7", "A7", "0", "F7", "G7", "0", "E7", "0","C7", "D7",
        "B6", "0", "0", "C7", "0", "0", "G6", "0", "0", "E6", "0", "0", "A6", "0", "B6", "0", "AS6", "A6", "0", "G6", "E7", "0", "G7",
        "A7", "0", "F7", "G7", "0", "E7", "0","C7", "D7", "B6", "0", "0"]
tetris = ["E5","B4","C5","D5","C5","B4","A4","A4","C5","E5","D5","C5","B4","C5","D5","E5","C5","A4","A4","0","C5","E5","D5","C5","B4","C5","D5","E5","C5","A4",
          "A4","0","A5","GS5","B5","D6","C6","B5","A5","A5","D6","FS6","F6","DS6","E6","CS6","B5","B5","E6","G6","FS6","F6","DS6","E6","CS6","B5","B5","0","0"]
starwars = ["A4","A4","A4","F4","C5","A4","F4","C5","A4","0","E5","E5","E5","F5","C5","GS4","F4","C5","A4","0","A5","A4","A4","A5","GS5","G5","FS5","F5","FS5",
            "0","AS4","DS5","D5","CS5","C5","B4","0","E5","E5","E5","F5","C5","GS4","F4","C5","A4","0", "A5","A4","A4","A5","GS5","G5","FS5","F5","FS5","0","AS4",
            "DS5","D5","CS5","C5","B4"]

button = Pin(10, Pin.IN, Pin.PULL_UP)
speaker = PWM(Pin(13))
redled = Pin(12, Pin.OUT)
blueled = Pin(11, Pin.OUT)
redled.high()
blueled.low()

def playnote(Note):
    speaker.duty_u16(0)
    sleep(0.05)
    redled.toggle()
    blueled.toggle()
    speaker.duty_u16(1500)
    speaker.freq(MusicNotes[Note])

def stopnote():
    speaker.duty_u16(0)

def button_pressed():
    return button.value() == 0  # Returns True when the button is pressed

def play_song(song, note_duration):
    for note in song:
        if note == "0" or note == "S":
            stopnote()
            sleep(note_duration)
        else:
            playnote(note)
            sleep(note_duration)
        if button_pressed():
            sleep(0.05)  # Debounce
            break  # Stop playing the song if the button is pressed

# Create a list of songs and durations
songs = [(mario, 0.2), (starwars, 0.2), (tetris, 0.2)]

song_index = 0  # Use an index to remember the last song that was played

while True:
    if button_pressed():
        sleep(0.05)  # Debounce
        # Play the appropriate song depending on the last song that was played
        play_song(*songs[song_index])
        song_index = (song_index + 1) % len(songs)  # Increment and wrap the index