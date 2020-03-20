# notes/views.py
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class NoteViewSet(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsOwner,)
    
    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user)
        raise PermissionDenied()
        
    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    # def get_read_serializer_class(self):

    #     if self.request.method == 'POST':
    #         return NoteSerializer

    #     return NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsOwner,)

    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user)
        raise PermissionDenied()
