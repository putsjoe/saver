from django.shortcuts import render
from django.http import HttpResponse

from .forms import UrlForm

def index(request):
    return HttpResponse("Hello, it begins.")

def get_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = UrlForm()

    return render(request, 'name.html', {'form':form})


