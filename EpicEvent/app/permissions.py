from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'management':
            return True
        else:
            return False
