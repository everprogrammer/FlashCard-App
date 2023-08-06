from django.db import models
from datetime import date

# Create your models here.

INTERVAL_DAYS = {
    'FIRST_REP': 1,
    'SECOND_REP': 3, 
    'THIRD_REP': 7,
    'FOURTH_REP': 14,
    'FIFTH_REP': 30
}

class Deck(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'Box number {self.number}'
    
class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=255)
    example = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    review_date #

