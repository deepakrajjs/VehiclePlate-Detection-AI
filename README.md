# VehiclePlate-Detection-AI
Hi 👋

Here’s the README.md content in text form for your project 👇

Title: Indian Number Plate OCR

Description:
An AI-powered Number Plate Recognition system using Python, OpenCV, and Tesseract OCR. Detects vehicle number plates from uploaded images, extracts text, maps the plate to Indian states, and logs details with a simple Flask web interface.

Features:
• Automatic number plate detection using Haar Cascade
• Text extraction with Tesseract OCR
• State identification from the plate code
• Saves cropped plate images with timestamp
• Logs all data to CSV
• Flask web interface for uploading images and viewing results

Installation:
1️⃣ Clone the repository:
git clone https://github.com/your-username/Indian-NumberPlate-OCR.git
cd Indian-NumberPlate-OCR

2️⃣ Install required Python libraries:
pip install -r requirements.txt

3️⃣ Install Tesseract OCR from:
https://github.com/tesseract-ocr/tesseract/releases
➡️ Set the path in the Python file (pytesseract.pytesseract.tesseract_cmd)

4️⃣ Run the application:
python number_plate_ocr.py

Usage:
➡️ Open browser and go to: http://localhost:5000
➡️ Upload car image → Detect plate → View results
