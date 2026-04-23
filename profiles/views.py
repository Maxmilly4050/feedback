from django.shortcuts import render
from django.views import View

def store_file(file):
    with open("temp/uploaded_file.jpg", "wb+") as f:
        for chunk in file.chunks():
            f.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        profile_image = request.FILES.get("profile_image")
        store_file(profile_image)
        return render(request, "profiles/create_profile.html")
