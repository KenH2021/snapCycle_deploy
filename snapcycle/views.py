from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm
from django.http import HttpResponse


# Create your views here.


def accueil(request):
    return render(request, 'pages/accueil.html')


def propos(request):
    return render(request, 'pages/propos.html')


def contact(request):
    return render(request, 'pages/contact.html')


def mission(request):
    return render(request, 'pages/mission.html')

def spool(request):
    return render(request, 'pages/spool.html')

def carbo(request):
    return render(request, 'pages/carbo.html')

def cameraIA(request):
    return render(request, 'pages/cameraIA.html')

def thanks(request):
    return render(request, 'pages/thanks.html')


def beta(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        print
        if form.is_valid():
            subject = "New client email"
            body = {
                'title': "New email: ",
                'email': form.cleaned_data['email_address'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'elwinmevopro@gmail.com',
                          ['elwinmevopro@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/thanks")
    form = EmailForm()
    return render(request, "pages/beta.html", {'form': form})
