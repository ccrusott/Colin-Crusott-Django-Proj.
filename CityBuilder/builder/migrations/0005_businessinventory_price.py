# Generated by Django 4.1.1 on 2022-11-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_npctraits_businessinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinventory',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]