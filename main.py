def on_received_string(receivedString):
    if receivedString == "C":
        pass
radio.on_received_string(on_received_string)

def 모션():
    pass
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.set_brightness(100)
strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.GREEN))
strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.PURPLE))
strip.show()

def on_forever():
    strip.rotate(1)
    strip.show()
    basic.pause(1000)
basic.forever(on_forever)
