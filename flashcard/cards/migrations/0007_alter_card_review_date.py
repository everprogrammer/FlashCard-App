# Generated by Django 4.2.4 on 2023-08-08 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_card_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='review_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
