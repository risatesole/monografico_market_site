from django.shortcuts import render

context = {
    "name": "supermercado",
}

def home(request): return render(request, "pages/home/index.html", context)
