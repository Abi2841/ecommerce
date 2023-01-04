"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm ,MyPasswordResetForm

urlpatterns = [
    
    path('', views.home),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(),name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('adress/', views.ProfileView.as_view(), name = 'address'),

    #login auth
    path('registration/', views.CustomerRegistrationView.as_view(), name= "customerregistration" ),
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name = 'login'),
    path('password-resrt/',auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = MyPasswordResetForm),name='password_reset'),
    path('product/', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),


    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
