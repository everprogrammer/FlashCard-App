from django.urls import path
from . import views

urlpatterns = [
    path("", views.CardListView.as_view(), name='card-list'),
    path("new-card", views.CardCreateView.as_view(), name='card-create'),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name='card-update'),
    path("learning/", views.LearningView.as_view(), name='learning'),
    path("search/", views.SearchView.as_view(), name='search'),
    path("archive/", views.ArchiveView.as_view(), name='archive'),
    path("reset/<int:card_id>", views.ResetDeckView.as_view(), name='reset-deck'),
]
