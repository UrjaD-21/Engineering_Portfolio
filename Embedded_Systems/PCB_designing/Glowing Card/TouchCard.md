# 📟 Professional Hardware Interface Card

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/urjadoshi2024etc-creator/PinFlow-Hub/825182d0a622871cc5c795fa33b702f2ecf3068a/TouchCard/Images/TouchCard_3D%20-%201.png" alt="3D Render Front" width="400"/></td>
    <td><img src="https://raw.githubusercontent.com/urjadoshi2024etc-creator/PinFlow-Hub/825182d0a622871cc5c795fa33b702f2ecf3068a/TouchCard/Images/TouchCard_3D%20-%202.png" alt="3D Render Angle" width="400"/></td>
  </tr>
</table>

## 🎯 Project Objective
**The Core Objective:** To transition from theoretical circuit design to a high-density, professional SMD hardware product that is as light as a credit card but features a high-speed reactive interface.

**The Idea:** This is a **Glowing Card** that reacts instantly when touched by the user. By integrating capacitive sensing with a specialized driver circuit, I created a modular input device that provides immediate visual feedback through a vibrant LED array.

**The Creative Desire:** Driven by a fascination with "Cute & Cool" design, I treated the PCB as a canvas. I envisioned a customized piece of hardware featuring a **Chibi character** fascinated by the glowing LEDs, proving that professional engineering can be both technically advanced and aesthetically expressive.

**The Technical Exploration:** To achieve this ultra-thin form factor, I explored the world of Surface Mount Devices (SMDs). This journey involved mastering the **BSS138 N-Channel MOSFET** for silent switching and integrating **0805 footprints** to replace bulky mechanical parts with a modern, capacitive system.

---

## 🔬 Technical Specifications (BOM)

| Component | Footprint | Value | Engineering Logic |
| :--- | :--- | :--- | :--- |
| **Touch Sensor** | SOT-23-6 | U1 | High-sensitivity capacitive detection in a tiny footprint. |
| **N-MOSFET** | SOT-23 | Q1 | Low gate-threshold voltage for reliable logic-level switching. |
| **Battery Cell** | CR2032 | BT1 | Slim 3V power source suited for the "Card" form factor. |
| **SMD LEDs** | 0805 | x6 | Current-optimized array for visual feedback. |
| **Passive Parts** | 0805 | 22nF - 10uF | Decoupling and signal stabilization for the sensor IC. |

---

## 🧠 Engineering Design Decisions

### 1️⃣ Why these components?
* **0805 SMD over THT:** Through-hole is for breadboards; 0805 is for products. It keeps the card thin while remaining hand-solderable.
* **BSS138 MOSFET over Relays:** Silent, fast, and solid-state. No mechanical wear and tear.
* **CR2032 over Li-Po:** Avoids the complexity of charging ICs. Simple, safe, and efficient for low-power use.

### 2️⃣ Trace Width & Routing Strategy
> **The Rule:** Wider for power, thinner for signal.

* **⚡ Power Paths (0.50 mm):** The "Highway." Prevents voltage drop so all 6 LEDs shine with equal brightness.
* **📟 Signal Lines (0.25 mm):** The "Side Streets." Optimized to snake between small SMD pads without causing shorts.
* **🔋 Battery Pads (1.00 mm+):** The "Foundation." Provides mechanical strength for the battery holder clips.

---

## 📈 Design & Schematics
![Touch Card Schematic](https://raw.githubusercontent.com/urjadoshi2024etc-creator/PinFlow-Hub/567569ddcafb217990949e4e75850ec64b8a179b/TouchCard/Images/TouchCard_Sch.png)

### 📟 2D Board Layout
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/urjadoshi2024etc-creator/PinFlow-Hub/825182d0a622871cc5c795fa33b702f2ecf3068a/TouchCard/Images/TouchCard_2D%20-%201.png" alt="PCB Top View" width="400"/></td>
    <td><img src="https://raw.githubusercontent.com/urjadoshi2024etc-creator/PinFlow-Hub/825182d0a622871cc5c795fa33b702f2ecf3068a/TouchCard/Images/TouchCard_2D%20-%202.png" alt="PCB Bottom View" width="400"/></td>
  </tr>
</table>

---

## 📂 Repository Structure
* **/Hardware**: Original KiCad project files.
* **/Images**: Schematic diagrams, 2D layouts, and 3D renders.
* **/Gerbers**: Production-ready ZIP for manufacturing (JLCPCB/PCBWay).

---

## 📸 Join the Journey
* **Instagram:** [@pinflow.hub](https://www.instagram.com/pinflow.hub)
* **Pinterest:** [PinFlow Hub](https://in.pinterest.com/pinflowh)

*Developed by PinFlow Hub | MIT License © 2026*
