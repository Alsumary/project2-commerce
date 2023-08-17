# Generated by Django 4.2.3 on 2023-08-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catName',
            new_name='categoryName',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='ifActive',
            new_name='isActive',
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(),
        ),
    ]
