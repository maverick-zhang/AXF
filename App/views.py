from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('index')


def home(request):

    return render(request, 'main/home.html')


def market(request):

    return render(request, 'main/market.html')


def cart(request):

    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')