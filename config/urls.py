from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("edu/", include("edu.urls")),
    path("common/", include("common.urls")),
]
