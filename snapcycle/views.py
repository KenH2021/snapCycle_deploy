from django.shortcuts import render

# Create your views here.


def acceuil(request):
    return render(request, 'pages/acceuil.html')


def propos(request):
    return render(request, 'pages/propos.html')


def beta(request):
    return render(request, 'pages/beta.html')
