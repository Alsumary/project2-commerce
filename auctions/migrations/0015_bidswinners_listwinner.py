# Generated by Django 4.2.3 on 2023-08-17 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_bidswinners'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidswinners',
            name='listwinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listwinner', to='auctions.listing'),
        ),
    ]
