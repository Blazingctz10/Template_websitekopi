from django.shortcuts import render, redirect
from django.http import JsonResponse  # <--- TAMBAHKAN BARIS INI (PENTING!)
from django.contrib import messages
from .models import Kopi

# 1. Halaman Home (Update sedikit)
def home(request):
    semua_kopi = Kopi.objects.all()
    # Hitung jumlah item di keranjang untuk badge di navbar
    cart_count = 0
    if 'cart' in request.session:
        cart_count = sum(request.session['cart'].values())
    
    return render(request, 'home.html', {
        'kopi_list': semua_kopi, 
        'cart_count': cart_count
    })

# 2. Fungsi Tambah ke Keranjang
def add_to_cart(request, kopi_id):
    cart = request.session.get('cart', {})
    kopi_id_str = str(kopi_id)
    
    if kopi_id_str in cart:
        cart[kopi_id_str] += 1
    else:
        cart[kopi_id_str] = 1
        
    request.session['cart'] = cart
    
    # Hitung total item
    total_items = sum(cart.values())

    # Cek apakah request datang dari AJAX (JavaScript)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'cart_count': total_items})

    # Jika tidak (fallback), lakukan refresh biasa
    return redirect('home')

# 3. Halaman Detail Keranjang
def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total_harga = 0

    for kopi_id, quantity in cart.items():
        kopi = Kopi.objects.get(id=kopi_id)
        subtotal = kopi.harga * quantity
        total_harga += subtotal
        items.append({
            'kopi': kopi,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'items': items, 
        'total_harga': total_harga
    })

# 4. Hapus Item dari Keranjang
def remove_from_cart(request, kopi_id):
    cart = request.session.get('cart', {})
    kopi_id_str = str(kopi_id)
    
    if kopi_id_str in cart:
        del cart[kopi_id_str]
        request.session['cart'] = cart
        
    return redirect('cart_detail')

# 5. Halaman Pembayaran (Checkout)
def checkout(request):
    cart = request.session.get('cart', {})
    total_harga = 0
    
    # Hitung total harga dulu
    for kopi_id, quantity in cart.items():
        try:
            kopi = Kopi.objects.get(id=kopi_id)
            total_harga += (kopi.harga * quantity)
        except Kopi.DoesNotExist:
            continue

    if request.method == 'POST':
        # Di sini Anda bisa simpan Nama + Total Harga ke database Order (jika ada)
        nama_pemesan = request.POST.get('nama')
        
        # Kosongkan keranjang setelah bayar
        request.session['cart'] = {}
        
        # Tampilkan halaman sukses (bikin file success.html extend base.html juga ya!)
        return render(request, 'success.html', {'nama': nama_pemesan})
        
    return render(request, 'checkout.html', {'total_harga': total_harga})