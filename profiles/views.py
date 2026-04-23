from django.shortcuts import render
from django.views import View

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        profile_image = request.FILES.get("profile_image")
        print(profile_image)
        return render(request, "profiles/create_profile.html")
