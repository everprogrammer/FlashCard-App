from django.contrib import admin
from .models import Card, Deck

# Register your models here

class CardAdmin(admin.ModelAdmin):
    list_display = ['question', 'deck', 'date_created', 'review_date']
    list_filter = ['deck' ,'date_created', 'review_date']

admin.site.register(Card, CardAdmin)
admin.site.register(Deck)