from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.views import View
from .models import Customer, Product
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


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
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!!! User Registered Succesfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html',locals())  

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())  
    def post(self, request): 
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality'] 
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg= Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations!!! Profile Saved Succesfully.")
        else:
            messages.warning(request,"Invalid Input Data")
        return render (request, 'app/profile.html', locals())























#API_PART
from rest_framework import generics
from products.models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','title','category','stock']

class ProductApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
