from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrClientReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated
        ) and (
            request.user.is_admin or (
                request.user.is_client and
                request.method in SAFE_METHODS
            )
        )


class AdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin
