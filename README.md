# ☕ Tiban Kaffe - Django Coffee Shop Website TEMPLATE!

Website e-commerce sederhana untuk kedai kopi "Tiban Kaffe". Proyek ini dibangun menggunakan **Django Framework** dan dimodifikasi untuk mencakup fitur Keranjang Belanja (Cart) tanpa reload (AJAX) serta simulasi pembayaran QRIS.

**Dibuat untuk Tugas Mata Kuliah: Pemrograman Database**

## 🌟 Fitur Utama
1.  **Katalog Produk:** Menampilkan daftar menu kopi dengan gambar dan harga dari database.
2.  **Smart Navbar:** Transparan saat di Home, berubah solid saat discroll (Sticky Navigation).
3.  **AJAX Add-to-Cart:** Menambah item ke keranjang tanpa refresh halaman.
4.  **Shopping Cart:** Manajemen keranjang belanja menggunakan *Django Sessions*.
5.  **Checkout QRIS:** Halaman pembayaran dengan QR Code dinamis.
6.  **Responsive Mobile:** Tampilan optimal di Desktop dan HP.

---

## 🚀 Cara Menjalankan Project (Installation)

Jika Anda ingin mencoba project ini di komputer lokal:

1.  **Clone Repository**
    ```bash
    git clone https://github.com/Blazingctz10/Template_websitekopi.git
    cd Template_websitekopi
    ```

2.  **Install Dependencies**
    Pastikan Python terinstall, lalu jalankan:
    ```bash
    pip install django pillow
    ```

3.  **Setup Database**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Buat Superuser (Untuk Upload Produk)**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```
    Buka browser di `http://127.0.0.1:8000/`

---

Copyright © 2025 Blazingctz10 Project.


### Cara Pasang di GitHub:
1.  Buka repo kamu: `https://github.com/Blazingctz10/Template_websitekopi`.
2.  Kalau belum ada file `README.md`, klik **Add file** > **Create new file**, beri nama `README.md`.
3.  Kalau sudah ada, klik file tersebut lalu klik ikon **Pensil** (Edit).
4.  **Paste** kode di atas.
5.  Klik **Commit changes**.

Sekarang repository kamu sudah lengkap dengan tutorial dan instruksi install yang valid! Sukses buat ujiannya ya!
