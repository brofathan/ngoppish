import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import inspect


@login_required(login_url="/login")
def main_page(request):
    products = Product.objects.filter(user=request.user)

    data = {
        "name": request.user.username,
        "class": "C",
        "products": products,
        "last_login": request.COOKIES["last_login"],
        "count": products.count()
    }

    return render(request, "main.html", data)

def form_page(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('main:homepage'))

    return render(request, "forms.html", {"form": form})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully registered!")
            return redirect("main:login")
    context = {"form":form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:homepage")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Sorry, incorrect username or password.")
    context = {}
    
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:login")

def delete_product(request, id):
    product = Product.objects.filter(pk=id)

    product.delete()
    return HttpResponseRedirect("/")

def edit_product(request, id, param):
    product = Product.objects.filter(pk=id)

    if param:
        product.update(amount = product[0].amount + 1)
    else:
        if product[0].amount > 1:
            product.update(amount = product[0].amount - 1)

    return HttpResponseRedirect("/")

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