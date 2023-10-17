from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsOrganiserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only organisers to edit/delete events.
    """
    def has_permission(self, request, view):
        # Allow read permissions for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions only if user is an organiser
        return request.user and request.user.is_organiser

class IsEventOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of an event to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read permissions for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions only if user is the owner of the event
        return obj.organiser == request.user

class IsAttendeeOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the attendee to edit/delete their sticky notes.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read permissions for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions only if user is the owner of the sticky note
        return obj.creator == request.user

class IsSuperuser(permissions.BasePermission):
    """
    Custom permission to allow only superusers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
