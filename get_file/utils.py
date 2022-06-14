from django.core.files.uploadedfile import UploadedFile
from django.conf import settings


def save_uploaded_file(file: UploadedFile, name: str):
    # print(f"{settings.MEDIA_ROOT}/{name}")
    # return
    with open(f"{settings.MEDIA_ROOT}/{name}", "wb") as _file:
        for chunk in file.chunks():
            _file.write(chunk)
