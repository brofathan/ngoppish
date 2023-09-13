# ngoppish

[Link Adaptable](https://ngoppish.adaptable.app/main/)

1. Menentukan direktori mana untuk menjadi tempat proyek django
2. Membuat virtual environment dengan command "py -m venv env"
3. Masuk kedalam virtual environment dengan command "env/Scripts/activate.bat"
4. Membuat file yang berisi requieremnts yang akan dipakai untuk berjalannya proyek django
5. Menginstall requirements dengan command "pip install -r requirements.txt"
6. Membuat proyek django baru di direktori dengan command "django-admin startproject ngoppish ."
7. Untuk keperluan deplyoment, tambahkan * pada ALLOWED_HOSTS di file settings.py
8. Membuat aplikasi django pada proyek django menggunakan command "python manage.py startapp main"
9. Mendaftarkan aplikasi django yang sudah kita buat di file settings.py pada direktori proyek. Hal ini dilakukan agar proyek kita tau aplikasi django yang kita buat.
10. Menambahkan kode pada file urls.py pada direktori proyek dengan mengisi kode:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include("main.urls")),
]
```
Hal ini dilakukan untuk menghubungkan url tingkat aplikasi kepada url tingkat proyek

11. Membuat model pada direktori aplikasi dengan menambahkan kode pada file models.py sebagai berikut:
```
class Product(models.Model):
    name = models.CharField(max_length=255) # untuk atribut nama
    amount = models.IntegerField() # untuk atribut jumlah
    description = models.TextField() # untuk atribut deskripsi
```
12. Membuat folder "templates" pada aplikasi dan membuat file "main.html" yang nantinya untuk tampilan utama website.

13. Menambahkan kode di file views.py pada direktori aplikasi yang berupa fungsi yang akan me-return kepada template HTML yang nantinya akan dirender disana. Kode sebagai berikut:
```
from django.shortcuts import render

def main_page(request):
    data = {
        "name": "Fathan",
        "class": "C"
    }

    return render(request, "main.html", data)
```
14. Menbambahkan kode pada urls.py di direktori aplikasi sebagai url, agar saat url dimasukan terhubung dengan fungsi main_page di views.py yang baru saja kita buat.

15. Melakukan push proyek tersebut ke repository github.

16. Melakukan deploy di adaptable untuk repository yang baru saja dibuat di github.
