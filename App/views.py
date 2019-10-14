from django.http import HttpResponse
from django.shortcuts import render

from App.models import MainWheel, MainNav, MustBuy


def index(request):
    return HttpResponse('index')


def home(request):

    main_wheels = MainWheel.objects.all()

    main_navs = MainNav.objects.all()

    must_buys = MustBuy.objects.all()

    data = {
        "main_wheels": main_wheels,
        "main_navs": main_navs,
        "must_buys": must_buys,
    }

    return render(request, 'main/home.html', context=data)


def market(request):

    return render(request, 'main/market.html')


def cart(request):

    return render(request, 'main/cart.html')


def mine(request):
    return render(request, 'main/mine.html')