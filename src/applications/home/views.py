from django.shortcuts import render

context = {
    "name": "supermercado",
}

def home(request): return render(request, "pages/home/index.html", context)
def dashboard(request): return render(request, "pages/home/dashboard.html", context)
def provider(request): return render(request, "pages/home/provider.html", context)
