from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.role == 'management':
            return True
        else:
            return False


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        elif view.action == 'create':
            return request.user.role == 'management'
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':
            return request.user.role == 'management'
        elif view.action in ['update', 'partial_update']:
            return request.user.role == 'management' \
                or obj.sales_contact == request.user
        else:
            return True


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        elif view.action == 'create':
            return request.user.role == 'management'
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':
            return request.user.role == 'management'
        elif view.action in ['update', 'partial_update']:
            return request.user.role == 'management' \
                or obj.client.sales_contact == request.user
        else:
            return True


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        elif view.action == 'create':
            return request.user.role == 'management'
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':
            return request.user.role == 'management'
        elif view.action in ['update', 'partial_update']:
            return request.user.role == 'management' \
                or obj.client.sales_contact == request.user \
                or obj.support_contact == request.user
        else:
            return True

