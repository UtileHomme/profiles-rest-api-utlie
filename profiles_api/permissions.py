from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # If requestd method is GET, because users are allowed to view other profiles
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
