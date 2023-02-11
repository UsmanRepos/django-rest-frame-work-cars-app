
from django.contrib import admin
from django.urls import path
from .views import CarAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CarAPIView.as_view()),
]
