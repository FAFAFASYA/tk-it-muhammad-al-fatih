from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("""
        <h1>TK IT Muhammad Al Fatih</h1>
        <p>Website Profil Sekolah</p>
        <p>Website berhasil online dengan Django.</p>
    """)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]