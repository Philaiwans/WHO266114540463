from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),  # แสดงหน้า index ที่คุณสร้าง
    path('admin/', admin.site.urls),
]
