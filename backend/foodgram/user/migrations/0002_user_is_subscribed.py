# Generated by Django 3.2 on 2023-04-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]