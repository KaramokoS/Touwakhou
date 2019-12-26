# Generated by Django 2.2.1 on 2019-12-26 11:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('afrik_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
