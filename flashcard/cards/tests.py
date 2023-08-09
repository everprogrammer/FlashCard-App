from django.test import TestCase
from .models import Card, Deck
from datetime import timedelta

# Create your tests here.
class CardModelTest(TestCase):

    def setUp(self):
        # Create some decks and cards for testing
        deck1 = Deck.objects.create(number=1)
        deck2 = Deck.objects.create(number=2)
        deck3 = Deck.objects.create(number=3)
        self.card1 = Card.objects.create(question='What is Django?', answer='A web framework', example='Django is used to create web applications', deck=deck1)
        self.card2 = Card.objects.create(question='What is Python?', answer='A programming language', example='Python is used to write Django code', deck=deck2)

    def test_update_review_date(self):
    
        # Check the initial review dates
        self.assertEqual(self.card1.review_date, self.card1.date_created)
        self.assertEqual(self.card2.review_date, self.card2.date_created)
        print(f'card1 deck number = {self.card1.deck.number}')
        print(f'card2 deck number = {self.card2.deck.number}')

        # Update the review dates
        self.card1.update_review_date()
        self.card2.update_review_date()

        # Check the updated review dates
        self.assertEqual(self.card1.review_date, self.card1.date_created + timedelta(days=1))
        self.assertEqual(self.card2.review_date, self.card2.date_created + timedelta(days=3))
        print(f'card1 deck number = {self.card1.deck.number}')
        print(f'card2 deck number = {self.card2.deck.number}')

        self.card1.move(solved=True)
        self.card2.move(solved=True)

        self.card1.update_review_date()
        self.card2.update_review_date()

        self.assertEqual(self.card1.review_date, self.card1.date_created + timedelta(days=4))
        self.assertEqual(self.card2.review_date, self.card2.date_created + timedelta(days=10))
        print(f'card1 deck number = {self.card1.deck.number}')
        print(f'card2 deck number = {self.card2.deck.number}')

        self.card1.move(solved=True)
        self.card2.move(solved=True)

        self.card1.update_review_date()
        self.card2.update_review_date()

        self.assertEqual(self.card1.review_date, self.card1.date_created + timedelta(days=11))
        self.assertEqual(self.card2.review_date, self.card2.date_created + timedelta(days=24))
        print(f'card1 deck number = {self.card1.deck.number}')
        print(f'card2 deck number = {self.card2.deck.number}')

        self.card1.move(solved=True)
        self.card2.move(solved=True)

        self.card1.update_review_date()
        self.card2.update_review_date()
        
    def test_move(self):
        # Test the move method of the Card model
        card1 = Card.objects.get(question='What is Django?')
        card2 = Card.objects.get(question='What is Python?')

        # Check the initial deck numbers
        self.assertEqual(card1.deck.number, 1)
        self.assertEqual(card2.deck.number, 2)

        # Move the cards
        card1.move(solved=True)
        card2.move(solved=False)

        # Check the updated deck numbers
        self.assertEqual(card1.deck.number, 2)
        self.assertEqual(card2.deck.number, 1)
