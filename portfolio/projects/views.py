from django.shortcuts import render
import requests
from django.conf import settings


def home(request):
    template_name = "index.html"
    response = requests.get("http://127.0.0.1:8000/api/portfolio/")

    print(settings.STATIC_ROOT)

    if response.status_code == 200:
        context = {
            "portfolios": response.json(),
            "base_dir": settings.MEDIA_ROOT.strip("media/"),
        }
    else:
        context = {"error": "Bad response!"}

    # print(context)

    return render(request, template_name, context)
