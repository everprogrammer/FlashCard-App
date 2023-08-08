from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # path("", TemplateView.as_view(template_name='base.html'),
    #      name='index'),
    path("", views.CardListView.as_view(), name='card-list'),
    path("new-card", views.CardCreateView.as_view(), name='card-create'),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name='card-update'),
    path("learning/", views.LearningView.as_view(), name='learning'),
    path("search/", views.SearchView.as_view(), name='search')

]
