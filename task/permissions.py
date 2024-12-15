from rest_framework.permissions import BasePermission


class TaskPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.all()
        obj_groups = obj.related_to.all()

        for group in user_groups:
            if group in obj_groups:
                return True
        
        return False
    