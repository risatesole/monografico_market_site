from django.shortcuts import render, redirect
from ...forms.form_image_upload import ImageUploadForm

def view_image_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload")

    else:
        form = ImageUploadForm()

    return render(request, "pages/image_upload/upload.html", {"form": form})
