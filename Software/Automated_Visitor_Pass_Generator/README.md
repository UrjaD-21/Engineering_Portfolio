
# 🪪 PassFlow: Data-Driven Visitor Pass & Verification System

## 🚀 Overview

PassFlow is a data-driven identity system that automates the creation of visitor passes using Google Forms and Google Sheets. It fetches user details and images, processes them, and generates verification-ready ID passes for controlled environments like college events and hackathons.

---

## ⚙️ Features

* 📄 Fetches **Name, Team ID, and Image** from Google Sheets
* 🖼️ Automatic image processing (crop, resize, rounded corners)
* ✍️ Dynamic text rendering on pass templates
* 🔗 Integrated pipeline: Google Forms → Google Sheets → Python
* 🛂 Passes designed for **real-time identity verification at entry points**
* 📦 Generates shareable digital passes

---

## 🧠 System Architecture

```
Google Form
     ↓
Google Sheets (Data Source)
     ↓
Python Script (Colab / Local)
     ↓
Data Extraction + Image Processing
     ↓
Pass Rendering Engine
     ↓
Generated Pass (Image/PDF)
```

---

## 🔄 Workflow

1. User submits Google Form (with image upload)
2. Data is stored in Google Sheets
3. Python script fetches latest entry:

   * Name
   * Team ID
   * Image URL
4. Image is downloaded and processed
5. Template engine renders:

   * Name
   * Team ID
   * Photo
   * QR Code
6. Final pass is generated for verification

---

## 🧩 Tech Stack

* Python
* PIL / OpenCV
* Google Sheets API
* Google Drive API
* NumPy
* QR Code Generation (qrcode library)

---

## 🔐 Verification System

Each generated pass includes:

* 📸 User Photo
* 🆔 Unique Team ID
* 🔳 QR Code

The QR code can be scanned at entry/exit points to:

* Verify identity
* Track attendance
* Log entry and exit timestamps

---

## 📸 Sample Output

(Add generated pass images here)

---

## ▶️ Demo

(Add YouTube demo link here)

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📌 Future Improvements

* QR-based live verification system
* Web dashboard for organizers
* Database integration (Firebase / SQL)
* Real-time attendance tracking
* Duplicate entry detection

---

## 🎯 Use Cases

* Hackathons
* College Events
* Visitor Management Systems
* Temporary ID Generation

---

## 👩‍💻 Author

Urja Doshi
