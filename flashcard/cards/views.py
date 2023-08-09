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
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Group cards by deck
        grouped_cards = {}
        total_card_count = 0
        for card in context['object_list']:
            if card.deck not in grouped_cards:
                grouped_cards[card.deck] = []
            grouped_cards[card.deck].append(card)
            total_card_count += 1

        context['grouped_cards'] = grouped_cards
        context['total_card_count'] = total_card_count
        # context['deck_card_counts'] = {deck: len(cards) for deck, cards in grouped_cards.items()}
        return context
    
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
            print(form.cleaned_data) 
            card_id = form.cleaned_data['card_id']
            solved = form.cleaned_data['solved'] == 'True'   

            card = get_object_or_404(Card, id=card_id)

            # Debug prints
            print(f"Card ID: {card_id}")
            print(f"Solved: {solved}")
            print(f"Current Deck Number: {card.deck.number}")
         
            card.move(solved)
            card.update_review_date()

            print(f"New Review Date: {card.review_date}")

        return self.get(request, *args, **kwargs)

class SearchView(ListView):
    template_name = 'cards/search.html'
    model = Card

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all()
        if search:
            object_list = object_list.filter(question__icontains=search)
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context
    
# class ArchiveView(ListView):
#     template = 'cards/archive.html'
#     queryset = Card.objects.filter(deck=6)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         card_list = context['object_list']
#         return context
    
class ArchiveView(ListView):
    model = Card
    template_name = 'cards/archive.html'
    queryset = Card.objects.filter(deck=6)    
    context_object_name = 'card_list'

class ResetDeckView(View):
    http_method_names = ['post']

    def post(self, request, card_id):
        card = Card.objects.get(id=card_id)
        card.deck = Deck.objects.get(number=1)
        card.save()
        return redirect('archive')


    
# class ResetDeckView(View):
#     http_method_names = ['post']

#     def post(self, request, card_id):
#         # get the card object by id
#         card = Card.objects.get(id=card_id)
#         # set deck number to one
#         card.deck = Deck.objects.get(number=1)

#         card.save()
#         return redirect(request.META.get('HTTP_REFERER'))

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