# Generated by Django 4.2.4 on 2023-08-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_card_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='deck',
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ManyToManyField(to='cards.deck'),
        ),
    ]
