from django.shortcuts import render, redirect

# Shared variable
shared_messages = []

def shared_view(request):
    global shared_messages

    if request.method == "POST":
        msg = request.POST.get("message")
        if msg:
            shared_messages.append(msg)
        return redirect("shared")

    return render(request, "shared.html", {
        "messages": shared_messages
    })