from django.shortcuts import render, redirect

# Shared variable
shared_messages = []





def debug(request):
    print("=================================================")
    print("first_number:")
    print(request.POST.get("first_number"), flush=True)
    print("=================================================")


def duck(request):
    pass

def provider_view(request):
    if request.method == "POST":
        debug(request)
        duck(request)
    return render(request, "provider.html", {})







def shared_view(request):
    global shared_messages

    if request.method == "POST":
        msg = request.POST.get("message")
        
        debug(request)

        if msg:
            shared_messages.append(msg)
        return redirect("shared")

    return render(request, "shared.html", {
        "messages": shared_messages
    })