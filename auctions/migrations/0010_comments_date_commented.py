# Generated by Django 4.2.3 on 2023-08-17 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_bids_lister_remove_comments_bidlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date_commented',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
