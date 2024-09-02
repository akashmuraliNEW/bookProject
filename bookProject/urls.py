"""bookProject URL Configuration

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
from bookApp import views
from django.conf import settings
from django.conf.urls.static import static
from userApp import views as userview
from accounts import views as userAccounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', views.homePage, name='home'),
    path('display', views.display_books, name='display'),
    path('update_book/<int:id>/', views.update_books, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    # login & register
    path('', userAccounts.userRegister, name='register'),
    path('login', userAccounts.userLogin, name='login'),
    # user
    path('userdisplay/<int:book_id>/', userview.userBookdisplay, name='userBookdisplay'),
    path('userbooks', userview.userBookDetails, name='userbookdetails'),

    # cart
    path('add_to_cart/<int:book_id>/', userview.add_to_cart, name='add_to_cart'),
    path('view_cart',userview.view_cart,name='view_cart'),
    path('remove_from_cart/<int:item_id>/', userview.remove_from_cart, name='remove_from_cart'),
    path('buy_cart/', userview.buy_cart, name='buy_cart'),
    path('payment_success/', userview.payment_success, name='payment_success'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)