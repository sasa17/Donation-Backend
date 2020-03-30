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
    # path('cart/', views.CartDetail.as_view(), name="cart"),
    # path('cart/item/', views.CartItem.as_view(), name="cart_item"),
    # path('cart/<int:cartitem_id>/update/', views.UpdateCart.as_view(), name="update-cartitem"),
    # path('cart/<int:cartitem_id>/delete/', views.DeleteCartItem.as_view(), name="delete-cartitem"),
    # path('checkout/', views.Checkout.as_view(), name="checkout"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
