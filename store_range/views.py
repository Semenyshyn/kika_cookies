from django.shortcuts import render_to_response
from .models import Product
# Create your views here.


def go_home(request):
    return render_to_response('main.html')


def get_all(request):
    return render_to_response('all.html', {'prod': Product.objects.all()})
