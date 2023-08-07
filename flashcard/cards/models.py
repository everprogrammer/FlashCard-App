from django.db import models
from datetime import date, timedelta, datetime
from django.core.validators import MinValueValidator, MaxValueValidator

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
    review_date  = models.DateField(default=datetime.today()+timedelta(days=1))

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

        # Get deck number
        deck_number = self.deck.id

        # Get the corresponding number of days from dictionary
        days_to_add = interval_revision_mapping.get(deck_number, 0)

        # Update review date - instance
        new_review_date = self.review_date + timedelta(days=days_to_add)

        # Save new review date to the object
        self.review_date = new_review_date
        self.save()

    def move(self, solved):
        if solved:
            # Move to the next deck
            next_deck = Deck.objects.filter(id__gt=self.deck.id).order_by('id').first()
            if next_deck:
                self.deck = next_deck
        else:
            # Move to the first deck
            first_deck = Deck.objects.order_by('id').first()
            if first_deck:
                self.deck = first_deck

        self.save()
        


    def __str__(self):
        return self.question



