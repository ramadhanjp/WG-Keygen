import os
import sys
import threading
import time

# ========== FLASK APP ==========
from flask import Flask, jsonify, render_template_string, send_from_directory
import nacl.utils
from nacl.public import PrivateKey
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    print("Serving index page")
    return render_template_string(INDEX_HTML)

@app.route('/generate-keys')
def generate_keys():
    print("Generating keys")
    private_key_obj = PrivateKey.generate()
    private_key = private_key_obj.encode()
    public_key = private_key_obj.public_key.encode()
    private_b64 = base64.standard_b64encode(private_key).decode('ascii').strip()
    public_b64 = base64.standard_b64encode(public_key).decode('ascii').strip()
    return jsonify({
        'private_key': private_b64,
        'public_key': public_b64
    })

@app.route('/fonts/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'fonts'), filename)

# Run Flask server in a separate thread
def start_server():
    app.run(port=5000)

server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

time.sleep(1)  # Wait for server to be ready

# ========== PYSIDE6 WINDOW ==========
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>WireGuard Key Generator</title>
<style>
  @font-face {
    font-family: 'Roboto Mono';
    src: url('/fonts/RobotoMono-Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
  }

  body {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    font-family: 'Roboto Mono', monospace;
    color: #e0e6f1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    margin: 0;
    padding: 1rem;
    box-sizing: border-box;
  }
  h1 {
    margin: 1rem 0 0.5rem 0;
    font-weight: 700;
    font-size: clamp(20px, 3vw, 30px);
    text-shadow: 0 0 8px #0ff;
    max-width: 100%;
    word-break: break-word;
  }
  p.subtitle {
    font-weight: 400;
    margin-bottom: 2rem;
    font-size: clamp(14px, 2vw, 20px);
    color: #a0b9d1;
    max-width: 100%;
    word-break: break-word;
    text-align: center;
  }
  .key-container {
    width: 90vw;
    max-width: 600px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 0 15px rgba(0,255,255,0.2);
    transition: box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
  }
  .key-container:hover {
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
  }
  label {
    font-weight: 700;
    font-size: clamp(16px, 2vw, 24px);
    display: block;
    margin-bottom: 0.5rem;
    color: #0ff;
  }
  textarea {
    width: 100%;
    resize: none;
    font-family: 'Roboto Mono', monospace;
    font-size: clamp(14px, 1.8vw, 18px);
    background: rgba(0,0,0,0.3);
    border: none;
    border-radius: 8px;
    color: #c0f4f4;
    padding: 0.8rem;
    height: auto;
    max-height: 10vh;
    box-sizing: border-box;
    user-select: all;
    overflow-wrap: break-word;
    white-space: pre-wrap;
  }
  button#generateBtn {
    background: #0ff;
    color: #012;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    padding: clamp(12px, 1vw, 18px) clamp(24px, 3vw, 36px);
    font-size: clamp(16px, 2vw, 24px);
    cursor: pointer;
    box-shadow: 0 0 15px #0ff88aa;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    max-width: 600px;
    width: 90vw;
  }
  button#generateBtn:hover {
    background: #00bcd4;
    box-shadow: 0 0 30px #0ff88aa;
  }
  .copy-btn {
    margin-top: 0.5rem;
    align-self: flex-start;
    background: #0ff;
    color: #012;
    border: none;
    border-radius: 8px;
    padding: clamp(6px, 0.5vw, 10px) clamp(12px, 1.2vw, 20px);
    font-size: clamp(12px, 1vw, 16px);
    cursor: pointer;
    box-shadow: 0 0 8px #0ff88aa;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    user-select:none;
  }
  .copy-btn:hover {
    background: #00bcd4;
    box-shadow: 0 0 20px #0ff88aa;
  }
  footer {
    margin-top: auto;
    padding-top: 1rem;
    padding-bottom: 1rem;
    font-size: clamp(12px, 0.9vw, 16px);
    color: #88ccee;
    opacity: 0.6;
    user-select:none;
  }
  @media (max-width: 480px) {
    h1 { font-size: 6vw; }
    p.subtitle { font-size: 3vw; }
    label { font-size: 3vw; }
    textarea { font-size: 3vw; max-height: 15vw; }
    button#generateBtn { font-size: 4vw; padding: 3vw; width: 100%; }
    .copy-btn { font-size: 3vw; padding: 1.5vw; }
    footer { font-size: 2.5vw; }
  }
</style>
</head>
<body>
  <h1>WireGuard Key Generator</h1>
  <p class="subtitle">Generate a private and public key pair for WireGuard VPN</p>

  <div class="key-container">
    <label for="privateKey">Private Key</label>
    <textarea id="privateKey" readonly></textarea>
    <button class="copy-btn" onclick="copyText('privateKey')">Copy Private Key</button>
  </div>

  <div class="key-container">
    <label for="publicKey">Public Key</label>
    <textarea id="publicKey" readonly></textarea>
    <button class="copy-btn" onclick="copyText('publicKey')">Copy Public Key</button>
  </div>

  <button id="generateBtn">Generate Keys</button>

  <footer>Author Ramadhanjp</footer>

  <script>
    async function generateKeys() {
      try {
        const response = await fetch('/generate-keys');
        if (!response.ok) throw new Error("HTTP error: " + response.status);
        const data = await response.json();
        document.getElementById('privateKey').value = data.private_key;
        document.getElementById('publicKey').value = data.public_key;
      } catch (e) {
        alert("Failed to generate keys: " + e.message);
      }
    }

    document.getElementById('generateBtn').addEventListener('click', generateKeys);

    function copyText(id) {
      const el = document.getElementById(id);
      const btn = document.querySelector(`[onclick="copyText('${id}')"]`);
      el.select();
      el.setSelectionRange(0, 99999);
      try {
        document.execCommand('copy');
        btn.textContent = "Copied!";
        setTimeout(() => {
          btn.textContent = id === 'privateKey' ? 'Copy Private Key' : 'Copy Public Key';
        }, 2000);
      } catch {
        btn.textContent = "Copy failed";
        setTimeout(() => {
          btn.textContent = id === 'privateKey' ? 'Copy Private Key' : 'Copy Public Key';
        }, 2000);
      }
      window.getSelection().removeAllRanges();
      el.blur();
    }
  </script>
</body>
</html>
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WireGuard Key Generator")
        self.resize(800, 600)

        # Detect the app path for icon loading also supporting PyInstaller bundle mode
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "icon.ico")  # Make sure the icon.ico exists here

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://localhost:5000"))
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
