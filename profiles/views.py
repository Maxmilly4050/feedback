from django.shortcuts import render
from django.views import View
from profiles.models import Profile
from .forms import UploadFileForm
from django.views.generic import ListView


class CreateProfileView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, "profiles/create_profile.html", context={"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_image = Profile(image=form.cleaned_data["profile_image"])
            profile_image.save()
        return render(request, "profiles/create_profile.html", context={"form": form})
    
class ListProfileView(ListView):
    model = Profile
    template_name = "profiles/create_profile.html"
    context_object_name = "profiles"
