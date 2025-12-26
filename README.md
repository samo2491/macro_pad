🛠️ CNC Macro Pad

A customizable CNC Macro Pad designed to streamline CNC workflows by providing dedicated physical buttons for frequently used commands, macros, and shortcuts. Ideal for CNC routers, mills, laser cutters, and CAD/CAM software.

✨ Features

⌨️ Programmable macro buttons

🧠 Supports custom key mappings and multi-key macros

🛠️ Designed for CNC workflows (Jog, Home, Zero, Start, Stop, etc.)

🔌 USB HID device (plug & play)

🧩 Compatible with popular CNC and CAD/CAM software

🖥️ Cross-platform (Windows / Linux / macOS)

🔧 Open-source hardware & firmware

📸 Preview

(Add photos or renders of your macro pad here)

[ Image coming soon ]

🧰 Hardware

Microcontroller: (e.g. Arduino Pro Micro / RP2040 / STM32)

Number of Keys: (e.g. 6 / 9 / 12 / 16)

Switches: (Mechanical / Tactile / Low-profile)

Connection: USB

Optional:

Rotary encoder

OLED display

RGB LEDs

💾 Firmware

The macro pad firmware supports:

Custom keymaps

Layered macros

CNC-specific shortcuts

Built using:

QMK / Arduino / CircuitPython (adjust as needed)

Flashing the Firmware
# Example (QMK)
qmk flash -kb cnc_macropad -km default

🧩 Default Keymap (Example)
Button	Function
1	Home All Axes
2	Zero X/Y/Z
3	Jog Mode
4	Start Job
5	Pause
6	Emergency Stop

(Fully customizable)

🖥️ Software Compatibility

Tested with:

Mach3 / Mach4

GRBL

LinuxCNC

Fusion 360

FreeCAD

Universal G-code Sender

🏗️ Case & Files

📐 3D printable enclosure

🧷 Plate & PCB files included

/firmware
/hardware
/case
/docs

🚀 Getting Started

Clone this repository

Flash the firmware

Customize key mappings

Plug in and start machining

🔧 Customization

You can:

Change macros and shortcuts

Add layers (e.g. Jog / CAM / Setup)

Modify the enclosure

Expand with more keys or encoders

📄 License

This project is licensed under the MIT License (or your preferred license).
See the LICENSE file for details.

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request

⭐ Acknowledgments

QMK / Arduino community

CNC makers & open-source hardware contributors
