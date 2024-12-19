from django.shortcuts import render

# ฟังก์ชันแสดงหน้าแรก
def home(request):
    return render(request, 'exercises/home.html')

# ฟังก์ชันแสดงหน้า next_page
def next_page(request):
    return render(request, 'exercises/next_page.html')
