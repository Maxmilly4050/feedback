from django.forms import Form, FileField

class UploadFileForm(Form):
    profile_image = FileField()