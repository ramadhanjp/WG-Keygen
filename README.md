
# WG Keygen

> Aplikasi sederhana untuk menghasilkan pasangan kunci privat dan publik WireGuard secara cepat dan aman.

![Wireguard]


## Deskripsi

**WG Key Generator** adalah aplikasi ringan dan intuitif yang membantu pengguna membuat pasangan kunci kriptografi (kunci privat dan publik) untuk digunakan dalam konfigurasi [WireGuard®](https://www.wireguard.com ), protokol jaringan privat virtual modern yang cepat dan aman.

Alih-alih menggunakan perintah baris perintah seperti `wg genkey` dan `wg pubkey`, aplikasi ini memberikan antarmuka yang ramah pengguna agar pengguna awam maupun profesional dapat dengan mudah membuat kunci tanpa harus bersentuhan langsung dengan terminal.

---

## 🔧 Fitur Utama

- ✅ Generate kunci privat acak berkualitas tinggi  
- ✅ Otomatis generate kunci publik dari kunci privat  
- ✅ Salin ke clipboard hanya dengan satu klik  
- 📁 Simpan hasil kunci ke file `.txt` atau ekspor sebagai bagian dari konfigurasi `.conf`  
- 💻 Tersedia untuk berbagai platform: Windows, macOS, Linux *(sesuaikan sesuai implementasi)*  
- 🌐 Antarmuka pengguna yang bersih dan responsif *(jika GUI)*  
- 🔒 Semua proses dilakukan secara lokal – tidak ada data yang dikirim ke server  

---

## 🖥️ Tangkapan Layar (Contoh)

![Screenshot Aplikasi WG Key Generator](screenshots/screenshot-1.png)

_(Catatan: tambahkan gambar nyata di folder `/screenshots` jika sudah tersedia.)_

---

## 🧰 Teknologi yang Digunakan

- **Backend:** Menggunakan `wireguard-tools` atau library kriptografi lokal (misalnya libsodium, cryptography, dll.)
- **Frontend:** _(Sesuaikan dengan teknologi yang dipakai, contoh: Python + Tkinter, Electron, Flutter, dll.)_
- **Build Tool:** _(Opsional: PyInstaller, Webpack, dll.)_

---

## 📦 Instalasi

### Untuk Pengguna:

Unduh versi terbaru dari halaman [Releases](https://github.com/username/wg-key-generator/releases ).

### Untuk Developer / Pengembangan:

```bash
git clone https://github.com/username/wg-key-generator.git 
cd wg-key-generator
npm install  # atau pip install -r requirements.txt dsb., tergantung teknologi

![Screenshot 2025-07-09 184651](https://github.com/user-attachments/assets/ae91ea3d-75cd-484b-94a3-e6240bd65868)

