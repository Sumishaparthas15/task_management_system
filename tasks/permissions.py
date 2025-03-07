# from rest_framework import permissions

# class IsManagerOrAssignedUser(permissions.BasePermission):
#     """
#     - Managers can update or delete any task.
#     - Developers can only update tasks assigned to them.
#     """
#     def has_object_permission(self, request, view, obj):
#         if request.user.role == "Manager":
#             return True
#         return obj.assigned_to == request.user
from rest_framework.permissions import BasePermission

class IsManagerOrAssignedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == "Manager":
            return True
        return obj.assigned_to == request.user
