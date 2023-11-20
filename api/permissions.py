
from rest_framework.permissions import BasePermission

class isSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and user.is_superuser) #is_authenticated checks weather the token is valid or not