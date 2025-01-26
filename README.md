# PRODIGY_CS_02

# Pixel Encryption Tool 🖼️🔒

A Python-based application to encrypt and decrypt images using pixel manipulation. Transform your images into secure, unintelligible formats using a unique key, ensuring they can only be restored with the correct decryption key.

---

## ✨ Features
- **Image Encryption**: Swap or manipulate pixel values using a secure key.
- **Image Decryption**: Restore the original image with the correct decryption key.
- **User-Friendly Input**: Input paths for images and choose your output location.
- **Lightweight**: Minimal dependencies and fast execution.
- **Sample Images**: Included for testing the tool.

---

## 🚀 How to Use

### Prerequisites
Ensure Python is installed on your system. Install the required libraries using the command:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Steps to Run the Tool
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/your-username/pixel-encryption-tool.git
   cd pixel-encryption-tool
   \`\`\`

2. Run the script:
   \`\`\`bash
   python image.py
   \`\`\`

3. Follow the prompts:
   - Enter the path to the image 
   - Provide an encryption key (e.g., \`123\`).
   - Enter the output path for the encrypted or decrypted image.

4. View the results.
   
---

## 🛠️ How It Works
1. **Encryption**:
   - Reads the pixel values of the image.
   - Modifies pixel values based on the user-defined key.
   - Saves the encrypted image to the specified output path.

2. **Decryption**:
   - Reads the encrypted image.
   - Reverses the pixel modifications using the same key.
   - Restores and saves the original image.

---

## ⚙️ Requirements
The tool depends on the following Python libraries:
- **Pillow**: For image handling and processing.
- **NumPy**: For mathematical operations on pixel data.

Install them via:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

---


## 💡 Significance
This project demonstrates:
- Practical application of pixel manipulation for encryption.
- Learning basic encryption/decryption techniques.
- Understanding how images are processed and stored in Python.

---

## 🛡️ License
This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributions
Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

---


