from django.contrib import admin
from django.urls import path
from exercises import views  # นำเข้าฟังก์ชัน views จากแอป exercises

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # เชื่อมโยง URL สำหรับหน้าแรก
    path('next/', views.next_page, name='next_page'),  # เชื่อมโยง URL สำหรับหน้า next_page
]
