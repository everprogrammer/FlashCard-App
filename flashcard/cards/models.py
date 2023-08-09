from django.db import models
from datetime import date, timedelta, datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.

class Deck(models.Model):
    number = models.IntegerField(default=1, validators=
                                            [MinValueValidator(1),
                                            MaxValueValidator(6)],
                                            unique=True)

    def __str__(self):
        return f'Deck ({self.number})'
    
class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=255)
    example = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    review_date  = models.DateField(default=date.today())

    def update_review_date(self):
        # first repition reminds after 1 day, second repition 
        #.. reminds after 3 days and so on...
        interval_revision_mapping = {
            1: 1,
            2: 3,
            3: 7,
            4: 14,
            5: 30,
        }

        deck_number = self.deck.number
        days_to_add = interval_revision_mapping.get(deck_number, 0)
        new_review_date = self.review_date + timedelta(days=days_to_add)
        self.review_date = new_review_date
        self.save()

    def move(self, solved):
        if solved:
            # Move to the next deck or archive
            if self.deck.number >= 5:
                self.deck = Deck.objects.get(number=6)
                self.review_date = self.review_date + timedelta(days=365)
                self.save()

            else:
                next_deck = Deck.objects.filter(number=self.deck.number+1).first()
                if next_deck:
                    self.deck = next_deck
                    self.save()
        else:
            # Move to the first deck
            first_deck = Deck.objects.filter(number=1).first()
            self.deck = first_deck

            self.save()
        
    def __str__(self):
        return self.question



