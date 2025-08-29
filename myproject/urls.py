from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Hello from Django on AWS 🚀")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
