# Generated by Django 4.2.3 on 2023-08-18 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_winnerpages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='content',
            new_name='description',
        ),
    ]