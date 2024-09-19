from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import Detailsform
from django.contrib.auth import logout
from.models import Hotel,Food,Fooditem
def index(request):
    data=Hotel.objects.all()
    return render(request,"index.html",{"data":data})
def registration(request):
    form=UserCreationForm() 
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=UserCreationForm() 
            return redirect("login")
        return redirect("login") 
    return render(request,"registration.html",{"form":form}) 
def food(request):
    data=Food.objects.all()
    return render(request,"food.html",{"data":data})
def home(request):
    home(request)
    return redirect('/')
def order_now(request,product_id):
        fooditem= Food.objects.get(id=product_id)
        fooditem, created = Fooditem.objects.get_or_create(fooditem=fooditem, 
                                                       user=request.user)
        fooditem.quantity  += 1
        fooditem.save()
        return redirect("cart")
def cart(request):
    items=Fooditem.objects.filter(user=request.user)
    total_price = sum(item.fooditem.price * item.quantity for item in items)
    return render(request,"cart.html",{"items":items,"total_price":total_price})
def delete(request,id):
    items=Fooditem.objects.get(id=id)
    if request.method=="POST":
        items.delete()
        return redirect("cart")
def checkout(request):
    form=Detailsform()
    if request.method=='POST':
        form=Detailsform(request.POST)
        if form.is_valid():
            form.save()
            form=Detailsform()
            return redirect("/")
    return render(request,"checkout.html", {"form":form})
    return request()
def continue_shop(request):
    continue_shop(request)
    return redirect("/")
def logout(request):
    logout(request)
    return redirect("/")


    