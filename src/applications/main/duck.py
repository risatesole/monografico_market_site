from django.shortcuts import render, redirect

def debug(request):
    print("=================================================")
    print("first_number:")
    print(request.POST.get("first_number"), flush=True)
    print("=================================================")

def duck_view(request):
    return render(request, "duck.html", {})
