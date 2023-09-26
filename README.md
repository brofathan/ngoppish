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

<hr>
<hr>

## Apa perbedaan antara form POST dan form GET dalam Django?

Http protocol mempunyai banyak metode request, salah satunya adalah POST dan GET.
Metode GET adalah dimana client mengambil data dari server, dengan memasukkan query requestnya ke dalam URL dan server me-respons request tersebut
Metode POST adalah dimana client mengirimkan data ke server dan server bisa memproses data tersebut. Pengiriman ini querynya tidak terlihat pada URL.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML mengirimkan data dengan membungkus data menggunakan format seperti format HTML, yaitu memiliki Tag pembuka dan Tag penutup. Format XML harus memiliki root element atau element yang paling atas.

JSON mengirimkan data dengan membungkus data menggunakan format seperti dictionary, atau biasa disebut object pada javascript. Format ini memiliki key dan value.

HTML mengirimkan data dengan format Tag. Tag ini disebut html element, yang nantinya akan diproses atau dirender oleh web browser dan ditampilkan kepada user berbentuk web page.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON mengirimkan data dengan format javascript object yang mana lebih ringkas, padat, dan jelas. Hal ini membuat data yang diproses dan dikirim mempunyai ukuran yang lebih ringan yang berarti akan lebih efisien dalam proses pengiriman data. Selain itu, format JSON berbentuk text, sehingga bisa dibaca oleh banyak bahasa pemrograman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat file baru di direktori main dengan nama forms.py untuk membuat class form yang dimiliki oleh django. Isi file dengan kode berikut:

```
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
```

2. Meng-import class ProductForm di file forms.py ke file views.py agar class ProductForm bisa digunakan dan ditampilkan ke user 

3. Membuat fungsi baru pada file views.py untuk menampilkan form dengan nama form_page. Isi fungsi tersebut dengan kode:

```
def form_page(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:homepage'))

    return render(request, "forms.html", {"form": form})
```

- request.POST or None berfungsi untuk mengecek apakah user sudah memberikan data. Jika sudah, maka data bisa diproses server. Jika belum, form tidak akan memproses data ke server.
- form.is_valid() and request.method == "POST" untuk mengecek apakah form yang disubmit sudah valid dan metodenya POST. Jika benar, maka form akan di save ke server.
- return HttpResponseRedirect(reverse('main:homepage')) berfungsi agar saat user submit form, user kembali ke homepage.

4. Membuat folder templates baru di direktori root sebagai kerangka html yang kedepannya akan dipakai di halaman-halaman lain agar struktur html lebih simpel dan terorganisir. Buat file base.html di folder root/templates dan isi kode:

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

5. Mengganti default direktori di settings.py menjadi BASE_DIR / 'templates'
6. Mengganti main.html pada main/templates menjadi:

```
{% extends "base.html" %}

{% block meta %}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ngoppish App</title>

{% endblock meta %}

{% block content %}

<h1>Welcome to ngoppish</h1>
<p>Nama: {{ name }}</p>
<p>Kelas: {{ class }}</p>

<p>Kamu menyimpan {{count}} item pada aplikasi ini</p>

<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
    </tr>

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.amount}}</td>
            <td>{{product.description}}</td>
        </tr>
    {% endfor %}
</table>

<a href="{% url 'main:create-product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

7. Membuat file baru di folder templates pada direktori main dengan nama forms.html yang bertujuan sebagai tampilan form page saat user membuat produk baru. Isi file dengan kode:

```
{% extends "base.html" %}

{% block content %}

<form action="." method="POST">{% csrf_token %}
    <table>
        {{form.as_table}}
    </table>

    <input type="submit" value="Save">
</form>

{% endblock content %}
```

8. Membuat key dan value baru pada dictionary pada fungsi main_page untuk menghitung berapa banyak products yang user sudah buat. Kode sebagai berikut:

```data = {
    "name": "Fathan",
    "class": "C",
    "products": products,
    "count": products.count()
}
```
9. Menambahkan kode untuk mengimport reverse, HttpResponseRedirect, serializers di views.html:

```
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
```

10. Menambahkan 4 fungsi baru pada views.html yaitu show_json untuk display model dalam format JSON, show_xml untuk display model dalam format XML, show_json_by_id untuk display model dalam format JSON berdasarkan spesifik id, show_xml_by_id untuk display model dalam format XML berdasarkan spesifik id.

```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

serializers berfungsi untuk mengubah format data model menjadi format JSON/XML

11. Meng-import fungsi-fungsi yang sudah dibuat di view.py ke main/urls.py:

from .views import show_xml, show_json, show_xml_by_id, show_json_by_id
```

12. Membuat URL baru di main/urls.py untuk menampilkan JSON dan XML

```
path('xml/', show_xml, name='show_xml'), 
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
 ```

## Screenshot Postman

```http://localhost:8000/```<br>
<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/img/ssHTML.png?raw=true">

```http://localhost:8000/json```<br>
<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/img/ssJSON.png?raw=true">

```http://localhost:8000/xml```<br>
<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/img/ssXML.png?raw=true">

```http://localhost:8000/json/19```<br>
<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/img/ssJSONid.png?raw=true">

```http://localhost:8000/xml/19```<br>
<img width="600" src="https://github.com/brofathan/ngoppish/blob/main/img/ssXMLid.png?raw=true">

<hr>
<hr>