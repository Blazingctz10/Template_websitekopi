from django.db import models

class Kopi(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='kopi_img/', blank=True, null=True)

    def __str__(self):
        return self.nama