# Generated by Django 4.1.1 on 2022-10-31 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_business_villagerlastname_villagerfirstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPCtraits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, unique=True)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.business')),
            ],
        ),
    ]
