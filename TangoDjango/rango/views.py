from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'bold_message': 'About'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')