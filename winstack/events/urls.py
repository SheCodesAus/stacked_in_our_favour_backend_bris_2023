from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('events/<int:event_id>/stickynotes/', views.StickyNotesEvent.as_view()),
    path('sticky-notes/', views.StickyNoteList.as_view()),
    path('sticky-notes/<int:pk>/', views.StickyNoteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)