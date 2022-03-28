from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm
from django.http import HttpResponse


# Create your views here.


def acceuil(request):
    return render(request, 'pages/acceuil.html')


def propos(request):
    return render(request, 'pages/propos.html')


def contact(request):
    return render(request, 'pages/contact.html')


def mission(request):
    return render(request, 'pages/mission.html')


def thanks(request):
    return render(request, 'pages/thanks.html')


def beta(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        print
        if form.is_valid():
            subject = "New client email"
            body = {
                'title': "email",
                'email': form.cleaned_data['email_address'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'elwinmevo@gmail.com',
                          ['elwinmevopro@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/thanks")
    form = EmailForm()
    return render(request, "pages/beta.html", {'form': form})
