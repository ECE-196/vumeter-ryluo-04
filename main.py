import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, #type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
previous_volume = 0
fall_rate = 500
ambient_volume = 22000
sensitivity = 5

while True:
    volume = microphone.value
    max_volume = 50000

    adjusted_volume = max(0, volume - ambient_volume) * sensitivity

    print(adjusted_volume)

    if adjusted_volume > previous_volume:
        display_volume = adjusted_volume
    else:
        display_volume = max(0, previous_volume - fall_rate)

    print(display_volume)


    for i in range(len(leds)):
        if adjusted_volume > i * max_volume / len(leds):
            leds[i].value = 1
        else:
            leds[i].value = 0

    sleep(0.1)