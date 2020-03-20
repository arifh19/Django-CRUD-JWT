from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NoteViewSet
from notes import views

urlpatterns = [
    path('notes', views.NoteViewSet.as_view(), name='hello'),
    path('notes/<int:pk>', views.NoteDetail.as_view()),
]