from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def tracker(request):
    return render(request,"tracker.html")

def search(request):
    return render(request,"search.html")

def productview(request):
    return render(request,"productview.html")

def checkout(request):
    return render(request,"checkout.html")
