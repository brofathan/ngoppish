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

##  Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm adalah class form bawaan django yang berfungsi untuk pembuatan form register pada website django. Kelebihannya, kita bisa langsung pakai saja class tersebut dan kode-kode untuk membuat form sudah tersedia, jadi memudahkan developer. Namun, kekurangannya adalah developer jadi terbatas dalam mengembangkan websitenya. Karena, fitur yang tersedia di class UserCreatioinForm belum tentu sudah cukup untuk developer.

##  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses pengecekan user dalam sebuah sistem login pada website django. Autentikasi berfungsi untuk memastikan apakah user yang melakukan login benar-benar user yang memiliki izin. Jika hal tersebut benar, maka proses otorisasi mengizinkan user untuk masuk ke dalam websitenya.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah data dari sebuah website yang disimpan di device user lewat browser, saat user sedang melakukan browsing. Django menggunakan data cookies salah satunya untuk agar user tidak bolak-balik login ke sebuah website, karena data user tersebut sudah tersimpan di browser yang berasal dari local. Selain itu, cookies juga membuat server storage lebih ringan karena data session disimpan di masing-masing device user.

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Cookies dalam pengembangan web defaultnya sebenarnya dibuat untuk tujuan yang positif dan aman dalam penggunaannya. Namun, karena cookies pada umumnya menyimpan informasi data dari user pengunjung, maka banyak orang yang mengeksploitasi kegunaan cookies. Contohnya adalah Cross-Site Scripting (XSS), CSRF attack, cookie hijacking, dan lain-lain.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Meng-import library-library yang dibutuhkan untuk membuat form register di ```views.py``` yaitu:

```py
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
```

- redirect untuk agar bisa mengganti page sesudah mengklik tombor tertentu
- UserCreationForm adalah form register bawaan django

2. Membuat fungsi baru di ```views.py``` bernama ```register```, dengan kode:

```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

form adalah UserCreationForm, jika form-nya valid maka save data user baru ke database lalu rediret ke login.

3. Membuat file baru di ```templates``` dengan nama ```register.html``` yang berisi:

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

4. Menyambungkan fungsi register views ke urls

```py
from main.views import *
```

```py
path('register/', register, name='register'),
```

5. Meng-import library baru untuk membuat fungsi login di ```views.py```

```py
from django.contrib.auth import authenticate, login
```

6. Menambahkan fungsi baru yaitu login_user di ```views.py```

```py
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:mainpage')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

```

Setelah user memasukkan username dan password, maka dicek oleh fungsi authenticate apakah ada user dengan username dan password tersebut. Jika ada maka lakukan fungsi login dan redirect ke mainpage

7. Membuat file baru yaitu login.html di main/templates dengan isi:

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

8. Tambahkan urls baru untuk menghubungkan ke templates

```py
path('login/', login_user, name='login'),
```

9. Meng-import library baru untuk fungsi logout di ```views.py```

```py
from django.contrib.auth import logout
```

10. Tambahkan fungsi logout di ```views.py```

```py
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

11. Tambahkan kode di ```main/templates/main.html``` untuk agar user bisa logout dengan button

```html
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

12. Menghubungkan urls ke views templates

```py
path('logout/', logout_user, name='logout'),
```

13. Meng-import library baru di ```views.py``` untuk merestriksi user yang belum login untuk akses webpage mainpage

```py
from django.contrib.auth.decorators import login_required
```

14. Menambahkan kode diatas fungsi ```main_page``` di ```views.py```

```py
@login_required(login_url='/login')
```

15. Membuat dua akun dengan tiga dummy data

Akun pertama: <br>
![image](https://github.com/brofathan/ngoppish/assets/45114836/4ebfd11c-c70a-44c6-ada6-bed1663913c4)
<br><br>
Akun kedua: <br>
![image](https://github.com/brofathan/ngoppish/assets/45114836/2dad9be2-cced-4824-b1aa-14256b9eb055)

16. Meng-import library baru unutk menghubungkan Model dengan user. Di file ```models.py```, tambahkan kode berikut

```py
from django.contrib.auth.models import User
```

```py
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Hal ini dilakukan agar tiap user memiliki key yang berbeda pada modelnya.

17. Mengganti fungsi ```form_page``` di file ```views.py``` dengan

```py
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```

Hal ini agar attribut user pada model terhubung dengan user yang men-submit

18. Mengubah fungsi ```main_page``` menjadi

```py
def main_page(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```

Filter dilakukan untuk menampilkan product yang hanya dimiliki oleh user tersebut dan tidak menampilkan product dari user lain.

19. Melakukan ```makemigrations``` dan ```migrate```

20. Meng-import library untuk menyimpan data datetime di cookies

```py
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

21. Menambahkan kode di fungsi ```login_user``` agar data login user tersimpan di cookies dan user tidak perlu login berkali-kali selama data cookies masih ada.

```py
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

22. Mengganti data pada fungsi ```main_page```, menambahkan informasi cookies

```py
data = {
    'name': 'Fathan',
    'class': 'C',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```

23. Menambahkan kode di fungsi ```logout_user``` agar ketika user logout, data cookies terhapus

```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

24. Menambahkan kode di ```main.html``` untuk menunjukkan kapan user terakhir kali login

```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

<hr>
<hr>

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Selector berfungsi agar kita bisa memilih bagian html atau elemen html mana yang mau kita style menggunakan css
- Element Selector, yaitu memilih element html mana yang akan dilakukan styling
- ID selector, yaitu memilih ID pada atribut ID di elemen html.
- Class selector, yaitu memilih class pada atribut class di elemen html.

## Jelaskan HTML5 Tag yang kamu ketahui.
- Tag ```<a>``` berfungsi untuk menyisipkan link pada element kita.
- Tag ```<audio>``` berfungsi untuk memasukkan suara atau audio stream ke html document kita.
- Tag ```<header>``` berfungsi untuk mendefinisikan bagian header pada website kita.
- Tag ```<footer>``` berfungsi untuk mendefinisikan bagian footer pada website kita.
- Tag ```<nav>``` berfungsi untuk mendefinisikan bagian navigation pada website kita.
- Tag ```<picture>``` berfungsi untuk container yang berisi banyak image.
- Tag ```<video>``` berfungsi untuk menampilkan video di dalam html document.

## Jelaskan perbedaan antara margin dan padding.
- Padding adalah jarak atau gap antara content di dalam sebuah container dengan border containernya.
- Margin adalah jarak atau gap antara sebuah element dengan element yang lainnya.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
- Framework tailwind lebih membebaskan developer dalam membuat websitenya karena class-class yang didefinisikan lebih kurang terstruktur atau kurang ter-develop untuk elemennya. Karena itu, tiap developer yang menggunakan tailwind pasti masing-masing memiliki design yang unik.
- Framework bootstrap class-class elemennya lebih ter-develop. Dalam artian, beberapa elemen itu sudah jadi dan developer tinggal memakainya, seperti template. Contohnya seperti class navbar dan button sudah disediakan oleh bootstrap. Karena itu, developer kurang bisa berkreasi dalam pembuatan websitenya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Karena saya menggunakan tailwind, saya menginstall dulu django tailwind dengan bantuan dokumentasi django.
2. Menambahkan bg-color pada tag body di base.html
3. Menambahkan class display flex di container pada login.html, karena display flex memudahkan untuk positioning element.
4. Menambhakan class-class lain seperti margin, padding, warna, font size, width, height, dan lain-lain supaya tampilan login menjadi lebih menarik dan proper.
5. Membuat file navbar.html dan men-include-nya di file main.html dan forms.html.
6. Menambahkan class width-full supaya panjang navbar sepanjang page.
7. Menambahkan elemen-elemen di dalam navbar yang berupa nama website dan tombol logout.
8. Style navbar.
9. Menambahkan class diplay flex di elemen container list product.
10. Menambahkan class-class width, height, diplay flex, background color di tiap-tiap product yang ada di list product supaya tampilan berbentuk cards.
11. Langkah terakhir yaitu melakukan pewarnaan supaya website lebih menarik.

<hr>
<hr>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming mengharuskan user untuk menunggu request dari server setelah user melakukan interaksi event pada website. Namun, asynchronous programming memungkinkan user tidak menunggu request dari server sehingga user tetap bisa berinteraksi dengan web tanpa adanya delay.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Pada event-driven programming terdapat event listeners dan event itu sendiri. Event akan di-trigger oleh user dan nantinya akan ditangkap oleh event listeners agar event dihandle dan dilakukan ke webpage. Contoh penerapannya adalah misal saat tombol delete product dipencet maka tombol tersebut dikaitkan ke function deleteProduct(id) oleh atribut onclick di html.

## Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX yaitu contohnya pada Fetch API. Karena saat melakukan FetchAPI, user tidak perlu me-reload webpage untuk mendapatkan data yang di-Fetch.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Menurut saya menggunakan fetch API lebih baik karena merupakan promise-based. Jadi, yang saya ketahui, promise ini memungkinkan user mendapatkan message error atau success saat proses fetch data. Selain itu juga, Fetch API adalah bagian dari javascript jadi tidak perlu mengimpor library apa-apa dan juga syntax-nya seperti javascript.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat fungsi untuk mengembalikan data product dalam JSON yang sudah di-filter berdasarkan user

```py
def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```

2. Membuat fungsi di views.py untuk menambahkan produk dengan AJAX dan mengimpor juga csrf_exempt dari django.views.decorators.csrf

```py
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

Bedanya dengan tidak menggunakan AJAX adalah pada returnnya. Kalau penambahan pada AJAX, hanya me-return HttpResponse saja.

3. Membuat path di urls.py untuk fungsi-fungsi yang baru saja dibuat

4. Melakukan FetchAPI di main.html meggunakan javascript.

```js
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
</script>
```

Fetch ini dilakukan untuk mendapatkan item.

5. Mengganti display cards menjadi.

```html
<div>
    <div id="product_table" class="flex justify-evenly flex-wrap px-20 mt-7"></div>

    <div class="self-center my-14">
        <button>
        </button>
    </div>
</div>
```

6. Menambahkan script untuk refresh product.

```js
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = ``
        let amountString = Object.keys(products).length

        products.forEach((product) => {
            htmlString += `\n
            <div class="flex flex-col m-5 bg-[#eceeff] rounded-md p-5 w-[45%] justify-between shadow-[5px_5px_0px_0px_rgba(63,76,173)]">
                <div>
                    <h1 class="text-2xl font-bold text-[#000000] mb-3">${product.fields.name}</h1>
                
                    <div class="min-h-[100px]">${product.fields.description}</div>
                </div>

                <div class="flex justify-end items-center mt-8">
                    
                    <div class="flex border-2 border-gray-300 mx-5">
                        <a class="cursor-pointer text-[#000000] text-center px-[20px] border-r-2 border-gray-300" onclick="editProduct(${product.pk},0)">
                            <button>-</button>
                        </a>
                        <div class="px-5">${product.fields.amount}</div>
                        <a class="cursor-pointer text-[#000000] text-center px-[20px] border-l-2 border-gray-300" onclick="editProduct(${product.pk},1)">
                            <button>+</button>
                        </a>
                    </div>

                    <div>
                        <a onclick="deleteProduct(${product.pk})"><button class="cursor-pointer w-[150px] bg-[#ff4136] text-indigo-50 rounded-md px-[10px] text-center">Delete product</button></a>
                    </div>
                    
                </div>
            </div>
            ` 
        })

        document.getElementById("product_table").innerHTML = htmlString
        document.getElementById("product_amount").innerHTML = amountString
    }

    refreshProducts()
```

Hal ini dilakukan untuk me-refresh tampilan (tidak perlu reload page) dari HTML menggunakan javascript agar data yang di Fetch secara live bisa langsung ditampilkan di page.

7. Membuat modal untuk bisa menambahkan product

```h
  <div id="defaultModal" tabindex="-1" aria-hidden="true" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
      <div class="relative w-full max-w-2xl max-h-full">
          <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                  <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                      Add product
                  </h3>
                  <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="defaultModal">
                      <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                      </svg>
                      <span class="sr-only">Close modal</span>
                  </button>
              </div>
              <div class="p-6 space-y-6">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <textarea class="form-control" id="amount" name="amount"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
              </div>
              <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                  <button data-modal-hide="defaultModal" type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                  <button data-modal-hide="defaultModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Decline</button>
              </div>
          </div>
      </div>
  </div>
```

8. Membuat fungsi untuk addProduct di javascript

```js
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addProduct
```