from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """Разрешает изменять и удалять только своё объявление."""

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user