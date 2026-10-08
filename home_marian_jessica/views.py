from django.shortcuts import render

def vista_home(request):
    return render(request, 'home_marian_jessica/home.html')  