# ☕ Tiban Kaffe - Django Coffee Shop Website

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

Website e-commerce modern untuk kedai kopi "Tiban Kaffe". Proyek ini dibangun menggunakan **Django Framework** dengan fokus pada pengalaman pengguna yang interaktif (AJAX) dan desain yang responsif (Mobile Friendly).

**Project ini dibuat untuk memenuhi Tugas Mata Kuliah: Pemrograman Database.**

---

## 🌟 Fitur Unggulan
* **Katalog Menu Dinamis:** Menampilkan produk, harga, dan gambar yang diinput melalui Admin Panel.
* **Smart Navbar:** Navigasi transparan yang berubah menjadi solid saat di-scroll (Sticky Glassmorphism).
* **AJAX Add-to-Cart:** Menambahkan kopi ke keranjang secara instan tanpa reload halaman (menggunakan Fetch API).
* **Session-Based Cart:** Sistem keranjang belanja ringan menggunakan *Django Sessions* (tanpa membebani database).
* **QRIS Checkout:** Halaman pembayaran simulasi dengan QR Code dinamis.
* **Responsive Design:** Tampilan optimal di Laptop, Tablet, dan HP.
* **Integrasi Lokasi:** Peta lokasi menggunakan Google Maps Embed API.

---

## 🚀 Panduan Instalasi (Cara Menjalankan)

Ikuti langkah-langkah berikut untuk menjalankan website ini di komputer lokal Anda:

### 1. Clone Repository
Unduh source code dari GitHub:
```bash
git clone [https://github.com/Blazingctz10/Template_websitekopi.git](https://github.com/Blazingctz10/Template_websitekopi.git)
cd Template_websitekopi
2. Buat Virtual Environment (Opsional)
Agar library project tidak tercampur dengan sistem komputer (Disarankan):

Bash

# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
3. Install Library (Requirements)
Install Django, Pillow, dan library pendukung lainnya sekaligus:

Bash

pip install -r requirements.txt
4. Setup Database
Buat tabel database (SQLite) berdasarkan model yang sudah dibuat:

Bash

python manage.py makemigrations
python manage.py migrate
5. Buat Akun Admin
Buat akun superuser untuk login ke halaman admin dan mengelola data kopi:

Bash

python manage.py createsuperuser
(Ikuti instruksi memasukkan username dan password di terminal)

6. Jalankan Server
Bash

python manage.py runserver
Buka browser dan akses: http://127.0.0.1:8000/
