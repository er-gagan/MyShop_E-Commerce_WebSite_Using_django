from django.shortcuts import render
from MyShopApp.models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    n=len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # context = {'product':product,'nSlides':nSlides,'range':range(nSlides)}
    allProds = [[products,range(1,nSlides),nSlides],
                [products,range(1,nSlides),nSlides]]
    params = {'allProds':allProds}
    return render(request,"MyShopApp/index.html",params)

def about(request):
    return render(request,"MyShopApp/about.html")

def contact(request):
    return render(request,"MyShopApp/contact.html")

def tracker(request):
    return render(request,"MyShopApp/tracker.html")

def search(request):
    return render(request,"MyShopApp/search.html")

def productview(request):
    return render(request,"MyShopApp/productview.html")

def checkout(request):
    return render(request,"MyShopApp/checkout.html")
