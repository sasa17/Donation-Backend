from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
# CartSerializer, Cart_ItemSerializer
from .serializers import UserCreateSerializer, ProfileSerializer
# from .models import Cart_Item, Cart


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileDetails(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# class CartDetail(RetrieveAPIView):
#     serializer_class = CartSerializer

#     def get_object(self):
#         cart,created = Cart.objects.get_or_create(user=self.request.user, active=True)
#         return cart

# class DeleteCartItem(DestroyAPIView):
# 	queryset = CartItem.objects.all()
# 	lookup_field = 'id'
# 	lookup_url_kwarg = 'cartitem_id'
# 	permission_classes = [IsAuthenticated, IsCartOwner]

# class UpdateCart(RetrieveUpdateAPIView):
#     serializer_class = CartUpdateSerializer
#     queryset = CartItem.objects.all()
#     lookup_field = 'id'
#     lookup_url_kwarg = 'cartitem_id'
#     permission_classes = [IsAuthenticated, IsCartOwner]

# class CartItem(CreateAPIView):
#     serializer_class = CartItemCreateSerializer
#     def create(self, request, *args, **kwargs):
#         serializer = CartItemCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         new_data = self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(CartItemSerializer(new_data).data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         cart,created = Cart.objects.get_or_create(user=self.request.user, active=True)
#         return serializer.save(cart = cart)

# class Checkout(APIView):
#     serializer_class = CartSerializer
#     def get(self, request):
#         cart = Cart.objects.get(user=request.user, active=True)
#         cart.active = False
#         cart.save()
#         return Response(CartSerializer(cart).data)
