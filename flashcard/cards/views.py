from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse, reverse_lazy
from .models import Card, Deck
from datetime import datetime
from .forms import CardCheckForm
import random

# Create your views here.
class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('deck', '-date_created')

class CardCreateView(CreateView):
    template_name = 'cards/new_card.html'
    model = Card
    fields = ['question', 'answer', 'example', 'deck']
    success_url = reverse_lazy('card-create')

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy('card-list')

class LearningView(CardListView):
    template_name = 'cards/learning.html'
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(review_date__gte=datetime.today())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card_list = context['object_list']
        if card_list:
            context["card"] = random.choice(card_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
            card.move(form.cleaned_data['solved'])
            card.update_review_date()

        return self.get(request, *args, **kwargs)

    
    
# def learning_view(request):
#     cards_to_review = Card.objects.filter(review_date__gte=datetime.today())
#     card = random.choice(cards_to_review) if cards_to_review else None

#     if request.method == 'POST':
#         form = CardCheckForm(request.POST)
#         if form.is_valid():
#             card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
#             card.move(form.cleaned_data['solved'])
#             card.update_review_date()

#     else:
#         form = CardCheckForm(initial={'card_id': card.id} if card else None)

#     context = {
#         'card': card,
#         'form': form,
#     }

#     return render(request, 'cards/learning.html', context)