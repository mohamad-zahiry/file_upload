from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import FileUploadForm
from .utils import save_uploaded_file


def index(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["file"]
            save_uploaded_file(file, file.name)
            context["success"] = True

    else:
        form = FileUploadForm()

    context["form"] = form
    return render(request, "index.html", context)
