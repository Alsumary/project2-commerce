# Generated by Django 4.2.3 on 2023-08-17 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listing_isactive_alter_listing_newprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidswinners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidamount', models.FloatField()),
                ('userwinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userwinner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
