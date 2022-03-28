from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmailForm


# Create your views here.


def acceuil(request):
    return render(request, 'pages/acceuil.html')


def propos(request):
    return render(request, 'pages/propos.html')


def beta(request):
    context = {}
    context['form'] = EmailForm()
    return render(request, 'pages/beta.html', context)


def email(request):  # a delete/modifier ...
    return render(request, 'pages/propos.html')


def get_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'pages/beta.html', {'form': form})
