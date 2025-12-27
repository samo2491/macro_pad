# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1, board.D6, board.D7, board.D5, board.D8,board.D9]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
HOME_ALL = KC.MACRO(
    Tap(KC.DOLLAR),
    Tap(KC.H),
    Tap(KC.ENTER),
)
ABORT = KC.MACRO(
    Press(KC.LCTRL),
    Tap(KC.X),
    Release(KC.LCTRL),
    Tap(KC.ENTER),
    Press(KC.LCTRL),
    Tap(KC.X),
    Release(KC.LCTRL),
)
ZERO_X_AND_Y = KC.MACRO(
    Tap(KC.G), Tap(KC.N1), Tap(KC.N0), Tap(KC.SPACE),
    Tap(KC.L), Tap(KC.N2), Tap(KC.N0), Tap(KC.SPACE),
    Tap(KC.P), Tap(KC.N1), Tap(KC.SPACE),
    Tap(KC.X), Tap(KC.N0),
    Tap(KC.ENTER),
        Tap(KC.G), Tap(KC.N1), Tap(KC.N0), Tap(KC.SPACE),
    Tap(KC.L), Tap(KC.N2), Tap(KC.N0), Tap(KC.SPACE),
    Tap(KC.P), Tap(KC.N1), Tap(KC.SPACE),
    Tap(KC.Y), Tap(KC.N0),
    Tap(KC.ENTER),
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [ABORT,KC.KP_8,KC.KP_9],
    [KC.KP_4,HOME_ALL,KC.KP_6],
    [ZERO_X_AND_Y,KC.KP_2,KC.KP_3],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()