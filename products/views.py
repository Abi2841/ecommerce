from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.views import View
from .models import Product
from django.db.models import Count
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.
 

def home(request):
    return render(request ,"app/home.html")

def about(request):
    return render(request ,"app/about.html")

def contact(request):
    return render(request ,"app/contact.html")
    

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category =val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html",locals())        

class CustomerRegistrationView(View): 
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())
    @csrf_protect
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations!!! User Registered Succesfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html',locals())  