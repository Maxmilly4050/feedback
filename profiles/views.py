from django.shortcuts import render
from django.views import View
from .forms import UploadFileForm

def store_file(file):
    with open("temp/uploaded_file.jpg", "wb+") as f:
        for chunk in file.chunks():
            f.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, "profiles/create_profile.html", context={"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_image = form.cleaned_data["profile_image"]
            store_file(profile_image)
        return render(request, "profiles/create_profile.html", context={"form": form})
