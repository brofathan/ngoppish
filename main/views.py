from django.shortcuts import render

def main_page(request):
    data = {
        "name": "Fathan",
        "class": "C"
    }

    return render(request, "main.html", data)