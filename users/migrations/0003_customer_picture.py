# Generated by Django 3.2.15 on 2022-11-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customer_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default='bookcovers/book.ico', upload_to='media/profiles/'),
        ),
    ]
