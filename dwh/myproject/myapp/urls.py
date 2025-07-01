from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),  # กำหนด path หลักให้เรียกหน้า index.html
    # path('admin/', admin.site.urls),  # ตัวอย่างถ้ามี admin
]
