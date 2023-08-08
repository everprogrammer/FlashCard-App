from django.test import TestCase
from .models import Card, Deck
from datetime import timedelta

# Create your tests here.
class CardModelTest(TestCase):

    def setUp(self):
        # Create some decks and cards for testing
        deck1 = Deck.objects.create(number=1)
        deck2 = Deck.objects.create(number=2)
        card1 = Card.objects.create(question='What is Django?', answer='A web framework', example='Django is used to create web applications', deck=deck1)
        card2 = Card.objects.create(question='What is Python?', answer='A programming language', example='Python is used to write Django code', deck=deck2)

    def test_update_review_date(self):
        # Test the update_review_date method of the Card model
        card1 = Card.objects.get(question='What is Django?')
        card2 = Card.objects.get(question='What is Python?')
        

        # Check the initial review dates
        self.assertEqual(card1.review_date, card1.date_created)
        self.assertEqual(card2.review_date, card2.date_created)
        print(f'card1 deck number = {card1.deck.number}')
        print(f'card2 deck number = {card2.deck.number}')

        # Update the review dates
        card1.update_review_date()
        card2.update_review_date()

        # Check the updated review dates
        self.assertEqual(card1.review_date, card1.date_created + timedelta(days=1))
        self.assertEqual(card2.review_date, card2.date_created + timedelta(days=3))
        print(f'card1 deck number = {card1.deck.number}')
        print(f'card2 deck number = {card2.deck.number}')

        card1.move(solved=True)
        card2.move(solved=True)

        card1.update_review_date()
        card2.update_review_date()

        self.assertEqual(card1.review_date, card1.date_created + timedelta(days=4))
        self.assertEqual(card2.review_date, card2.date_created + timedelta(days=6))
        print(f'card1 deck number = {card1.deck.number}')
        print(f'card2 deck number = {card2.deck.number}')

        card1.move(solved=True)
        card2.move(solved=True)

        card1.update_review_date()
        card2.update_review_date()

        self.assertEqual(card1.review_date, card1.date_created  + timedelta(days=7))
        self.assertEqual(card2.review_date, card2.date_created  + timedelta(days=9))
        print(f'card1 deck number = {card1.deck.number}')
        print(f'card2 deck number = {card2.deck.number}')

        card1.move(solved=True)
        card2.move(solved=True)

        card1.update_review_date()
        card2.update_review_date()

        self.assertEqual(card1.review_date, card1.date_created  + timedelta(days=10))
        self.assertEqual(card2.review_date, card2.date_created  + timedelta(days=12))



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
