input.onButtonPressed(Button.A, function () {
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    basic.showArrow(ArrowNames.South)
})
input.onGesture(Gesture.Shake, function () {
    music.setVolume(255)
    music.playMelody("C5 B A G F E D C ", 162)
})
basic.showLeds(`
    . . . . .
    . # # # .
    . # . . .
    . # . . .
    . # # # .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . # . # .
    . # # # .
    . # . # .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . # . # .
    . # . # .
    . # # # .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . . . .
    . # . # .
    . # # # .
    . . . # .
    . # # # .
    `)
basic.pause(1000)
basic.forever(function () {
	
})
