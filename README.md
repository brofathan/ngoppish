# ngoppish

[Link Adaptable](https://ngoppish.adaptable.app/main/)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

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

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jadi, saat user memasukkan url dari proyek kita, urls.py akan digunakan dan setelah itu urls.py akan memanggil fungsi main_page pada views.py. File views.py akan memanggil file main.html pada templates dan akan ditampilkan kepada user. File views.py juga akan memanggil models.py. File models.py menyiapkan models dan menyimpannya di dalam database yang data tersebut bisa di-pass ke views.py dan sekaligus ditampilkan di templates, main.html, yang nantinya akan ditampilkan juga ke user.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/bagandjango.png?raw=true">

Kita menggunakan virtual environment dalam membuat proyek django karena untuk sebuah proyek django yang berbeda, biasanya memiliki dependencies yang berbeda. Oleh karena itu, dibutuhkanlah virtual environment agar dependencies tiap proyek terisolasi. Dalam artian, dependencies tiap-tiap proyek tidak akan bertabrakan satu sama lain. Kita bisa saja membuat proyek django tanpa venv, namun dependencies pada proyek-proyek kita harus sama. Maka, lebih baik kita menggunakan venv dalam membuat proyek.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

* MVC (Model-View-Controller)
  - Model: Model adalah komponen yang menyimpan data dan berkomunikasi langsung dengan database. Model merepresentasikan data dan logika pada aplikasi kita.
  - View: Komponen yang menampilkan data yang dimiliki model dan menampilkannya ke user dengan memanggil komponen template
  - Controller: Komponen yang menggabungkan Model dan View

* MVT (Model-View-Template)
  - Template: Template adalah komponen yang mengatur interface yang akan ditampilkan ke user. Template berisi file-file html yang menjadi halaman dari website.

* MVVM (Model-View-ViewModel)
  - ViewModel: ViewModel adalah perantara antara komponen view dan model. ViewModel mengubah format data yang dimiliki model agar bisa ditampilkan oleh view di template

* Perbedaan ketiganya:
  - MVC digunakan untuk menerima data dari user dan akan berkomunikasi dengan database.
  - MVT untuk menampilkannya kepada user karena adanya komponen template.
  - MVVM lebih kepada menerima data sekaligus mengembalikannya kepada user.
