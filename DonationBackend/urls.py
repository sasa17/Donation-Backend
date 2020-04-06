"""DonationBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', views.ProfileDetails.as_view(), name="profile-details"),
    path('donation/', views.DonationItem.as_view(), name="donation"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('restaurant/', views.RestaurantList.as_view(), name="restaurant-list"),
    path('menu/<int:menu_id>/', views.UpdateMenu.as_view(), name="update-menu-item"),
    path('restaurant/<int:restaurant_id>/', views.RestaurantDetail.as_view(), name="restaurant-detail"),
    path('donationbasket/',views.DonationBasketAdd.as_view(), name="add-basket"),
    path('menu/', views.MenuAdd.as_view(), name="add-menu-item"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
