# Generated by Django 4.2.3 on 2023-08-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_catname_category_categoryname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
