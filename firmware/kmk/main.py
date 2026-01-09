from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, SSD1306
from kmk.extensions.rgb import RGB
from kmk.scanners import DiodeOrientation

import board

keyboard = KMKKeyboard()

# ─────────────────────────────────────────────
# Matrix
# ─────────────────────────────────────────────
keyboard.col_pins = (
    board.GP29,  # col1
    board.GP3,   # col2
    board.GP4,   # col3
    board.GP2,   # col4
)

keyboard.row_pins = (
    board.GP28,  # row1
    board.GP27,  # row2
    board.GP26,  # row3
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ─────────────────────────────────────────────
# Layers
# ─────────────────────────────────────────────
layers = Layers()
keyboard.modules.append(layers)

# ─────────────────────────────────────────────
# RGB
# ─────────────────────────────────────────────
rgb = RGB(
    pixel_pin=board.GP1,   # argb pin
    num_pixels=12,         # 🔴 CHANGE to your LED count
    val_limit=100,
    hue_default=0,
    sat_default=255,
    val_default=100,
    animation_mode=RGB.STATIC,
)

keyboard.extensions.append(rgb)

# ─────────────────────────────────────────────
# OLED Display
# ─────────────────────────────────────────────
display = Display(
    display=SSD1306(
        width=128,
        height=32,
        i2c=board.I2C(),
        device_address=0x3C,
    ),
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=60,
)

keyboard.extensions.append(display)

# ─────────────────────────────────────────────
# Keymap
# (SW11 and SW12 ignored)
# ─────────────────────────────────────────────
keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,
        KC.A,    KC.S,    KC.D,    KC.F,
        KC.Z,    KC.X,    KC.C,    KC.V,
    ],
]

# ─────────────────────────────────────────────
# OLED Content
# ─────────────────────────────────────────────
@display.draw
def draw(display, keyboard):
    display.clear()
    display.text("XIAO RP2040", 0, 0, 1)
    display.text("RGB + OLED", 0, 12, 1)
    display.text(f"LAYER {keyboard.active_layers[0]}", 0, 24, 1)
    display.show()

keyboard.go()
