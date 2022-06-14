from django.forms import Form, FileField

class FileUploadForm(Form):
    file = FileField()