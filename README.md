# Custom QR Code Generator

![Python](https://img.shields.io/badge/python-3.9-blue)
![Pillow](https://img.shields.io/badge/Pillow-image%20processing-yellow)
![qrcode](https://img.shields.io/badge/qrcode-generator-orange)

---

## **Table of Contents**
1. [General Info](#general-info)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [License](#license)

---

## **General Info**
This project is a **Python-based QR code generator** that creates customized QR codes with:
- **Rounded square modules** for a modern look.
- **Customizable colors** for foreground and background.
- **Centered icons** with configurable colors and margins.

The QR codes can be used for links, text, or any other encoded information.

---

## **Features**
- Generate **QR codes** with a rounded-square design.
- Customize the **foreground and background colors**.
- Add a **custom icon** at the center of the QR code.
- Saves the QR code as an image file.

---

## **Technologies**
- **Python 3.10**
- **qrcode** (QR code generation)
- **Pillow (PIL)** (Image processing)

---

## **Installation**

### **Prerequisites**
- **Python 3.9 or higher**
- **pip** installed

### **Steps**
1. Clone the repository:
    ```bash
    git clone https://github.com//.git
    cd QR-GENERATOR
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Usage**

Run the script with the required parameters:

```python
from main import create_custom_qr

# Define parameters
uri = "https://example.com"
qr_color = "#1a73e8"  # Blue color for QR modules
bg_color = "#f1f3f4"  # Light gray background
file_name = "custom_qr.png"
icon_path = "icon.png"  # Path to the custom icon

# Generate the QR code
create_custom_qr(uri, qr_color, bg_color, file_name, icon_path)
```

---

## **License**
This project is open-source and available under the **MIT License**.

