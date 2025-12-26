# 🛠️ CNC Macro Pad

A customizable **CNC Macro Pad** designed to speed up CNC workflows by providing dedicated physical buttons for common commands, macros, and shortcuts. Perfect for CNC routers, mills, laser cutters, and CAD/CAM software.

---

## ✨ Features

- ⌨️ Fully programmable macro keys  
- 🧠 Supports multi-key and layered macros  
- 🛠️ CNC-focused controls (Jog, Home, Zero, Start, Stop)  
- 🔌 USB HID (plug & play, no drivers required)  
- 🖥️ Cross-platform support (Windows, Linux, macOS)  
- 🔧 Open-source hardware and firmware  

---

## 📸 Preview

> Add photos or renders of your CNC Macro Pad here.


---

## 🧰 Hardware

- **Microcontroller:** Arduino Pro Micro / RP2040 / STM32 *(edit as needed)*  
- **Keys:** 6 / 9 / 12 / 16 *(configurable)*  
- **Switches:** Mechanical / Tactile / Low-profile  
- **Connection:** USB  
- **Optional Add-ons:**
  - Rotary encoder
  - OLED display
  - RGB LEDs

---

## 💾 Firmware

The macro pad firmware supports custom keymaps and CNC-specific macros.

Built using:
- **QMK / Arduino / CircuitPython** *(choose what applies)*

### Flashing Firmware (Example)

```bash
qmk flash -kb cnc_macropad -km default
