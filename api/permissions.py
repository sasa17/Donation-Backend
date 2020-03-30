from rest_framework.permissions import BasePermission

class IsCartOwner(BasePermission):
	message = "You must be the owner of this cart"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.cart.user == request.user):
			return True
		else:
			return False