# 🚗 VehiclePlate-Detection-AI 🇮🇳

An **AI-powered Indian Vehicle Number Plate Recognition System** built using **Python**, **OpenCV**, **Tesseract OCR**, and **Flask**.

Detect number plates from vehicle images, extract text, identify the state from the plate code, and log everything — all from a simple and interactive web interface.

---

## ✨ Features 

* 🎯 **Automatic Number Plate Detection** (Haar Cascade)
* 🔎 **Text Extraction** using Tesseract OCR
* 🗺️ **Indian State Identification** from plate code
* 🗂️ **Cropped Plate Saving** with Timestamp
* 📑 **Detection Logs Stored** in CSV
* 🌐 **Flask Web Interface** for uploads & results

---

## 📦 Tech Stack

* Python 3.x
* OpenCV
* Tesseract OCR
* Flask
* Haar Cascade Classifier (for plate detection)

---

## 📁 Project Structure

```
VehiclePlate-Detection-AI/
├── haarcascade_russian_plate_number.xml
├── number_plate_ocr.py
├── templates/
│   └── index.html
├── static/
│   └── uploads/
├── logs.csv
├── README.md
└── requirements.txt
```

---

## 🛠️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/VehiclePlate-Detection-AI.git
cd VehiclePlate-Detection-AI
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Tesseract OCR

* 📥 Download: [Tesseract Releases](https://github.com/tesseract-ocr/tesseract/releases)
* 🔧 Set the path in your Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 4️⃣ Run the Application

```bash
python number_plate_ocr.py
```

---

## 🚀 Usage

➡️ Open browser and visit:

```
http://localhost:5000
```

➡️ **Upload** a vehicle image → **Detect Number Plate** → **View Results**

---

## 📌 Requirements

* Python 3.x
* OpenCV
* pytesseract
* Flask
* Haar Cascade XML
* Tesseract OCR (installed separately)


---

## 💡 Future Improvements

* 🔐 Add Admin Panel
* 📱 API Integration
* 📦 Docker Support
* 📊 Data Visualization of Logs

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!
Fork this repo → Make changes → Submit Pull Request ✅

---

## 📧 Contact

Made with ❤️ by DEEPAK RAJ JS
🔗 [GitHub](https://github.com/deepakrajjs) | 📧 [deepakrajs2909@gmail.com]
---

## ⭐ Support

If you like this project❤️, **give it a ⭐ on GitHub**.
It motivates me to build more awesome projects! 
