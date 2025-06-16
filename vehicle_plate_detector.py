import cv2
import numpy as np
import pytesseract
import os
import time
import csv
from flask import Flask, render_template_string, request, send_from_directory

# ==================== CONFIG ====================
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/deepak raj js/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

if not os.path.exists("Detected_Plates"):
    os.makedirs("Detected_Plates")

csv_file = 'plates_log.csv'
if not os.path.isfile(csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Plate_Text", "State", "Image_Path"])

states = {
    "AN": "Andaman and Nicobar", "AP": "Andhra Pradesh", "AR": "Arunachal Pradesh", "AS": "Assam",
    "BR": "Bihar", "CH": "Chandigarh", "DN": "Dadra and Nagar Haveli", "DD": "Daman and Diu",
    "DL": "Delhi", "GA": "Goa", "GJ": "Gujarat", "HR": "Haryana", "HP": "Himachal Pradesh",
    "JK": "Jammu and Kashmir", "KA": "Karnataka", "KL": "Kerala", "LD": "Lakshadweep",
    "MP": "Madhya Pradesh", "MH": "Maharashtra", "MN": "Manipur", "ML": "Meghalaya",
    "MZ": "Mizoram", "NL": "Nagaland", "OD": "Odisha", "PY": "Puducherry", "PB": "Punjab",
    "RJ": "Rajasthan", "SK": "Sikkim", "TN": "Tamil Nadu", "TR": "Tripura", "UP": "Uttar Pradesh",
    "WB": "West Bengal", "CG": "Chhattisgarh", "TS": "Telangana", "JH": "Jharkhand", "UK": "Uttarakhand"
}

# ============ DETECTION FUNCTION (USED IN FLASK) ============
def detect_plate_and_save(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

    results = []

    for (x, y, w, h) in plates:
        a, b = (int(0.02 * w), int(0.02 * h))
        plate_img = img[y + a:y + h - a, x + b:x + w - b]

        plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        _, plate_thresh = cv2.threshold(plate_gray, 150, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(plate_thresh, config='--psm 8')
        text_clean = ''.join(filter(str.isalnum, text))

        state_code = text_clean[:2].upper()
        state_name = states.get(state_code, "Unknown")

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"Detected_Plates/{text_clean}_{timestamp}.jpg"
        cv2.imwrite(filename, plate_img)

        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, text_clean, state_name, filename])

        results.append({
            'timestamp': timestamp,
            'plate_text': text_clean,
            'state': state_name,
            'image_path': filename
        })

    return results

# ============ FLASK SETUP ============
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <title>Number Plate Detection</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            input[type="file"] { margin-top: 20px; }
            img { margin-top: 20px; max-width: 80%; height: auto; }
        </style>
    </head>
    <body>
        <h1>Upload Car Image</h1>
        <form method=post enctype=multipart/form-data action="/upload">
          <input type=file name=file required>
          <br><br>
          <input type=submit value="Upload and Detect">
        </form>
    </body>
    </html>
    ''')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filepath = os.path.join("Detected_Plates", file.filename)
        file.save(filepath)
        results = detect_plate_and_save(filepath)

        result_html = "<h2>Results:</h2>"
        for r in results:
            result_html += f"<p><b>Plate:</b> {r['plate_text']} | <b>State:</b> {r['state']}<br><img src='/Detected_Plates/{os.path.basename(r['image_path'])}' width=300></p>"

        result_html += "<p><a href='/'>Upload another</a></p>"
        return result_html

@app.route('/Detected_Plates/<path:filename>')
def serve_file(filename):
    return send_from_directory('Detected_Plates', filename)

if __name__ == "__main__":
    import logging
    logging.getLogger('werkzeug').disabled = True

    try:
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)
    except ImportError:
        print("Waitress not installed. Running with Flask development server...")
        app.run(debug=False, use_reloader=False, port=5000)

# =================== END ===================
