from books import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"books", views.ListBookAPIView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("api/", include(router.urls)),
]
