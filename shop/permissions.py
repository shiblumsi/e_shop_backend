from rest_framework import permissions

class IsShopMerchant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE": 
            # check here if the user is merchant of the shop
            return obj.merchant == request.user

        # else always return True.
        return True
    
class IsShopOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "POST": 
            # check here if the user is merchant of the shop
            return obj.merchant == request.user

        # else always return True.
        return True