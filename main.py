def on_button_pressed_a():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.SOUTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.set_volume(255)
    music.play_melody("C5 B A G F E D C ", 162)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    . . . . .
        . # # # .
        . # . . .
        . # . . .
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # . # .
        . # . # .
        . # # # .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    . . . . .
        . # . # .
        . # # # .
        . . . # .
        . # # # .
""")
basic.pause(1000)

def on_forever():
    pass
basic.forever(on_forever)
