from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers

def main_page(request):

    products = Product.objects.all()

    data = {
        "name": "Fathan",
        "class": "C",
        "products": products,
        "count": products.count()
    }

    return render(request, "main.html", data)

def form_page(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:homepage'))

    return render(request, "forms.html", {"form": form})

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