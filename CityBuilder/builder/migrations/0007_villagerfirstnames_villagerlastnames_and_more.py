# Generated by Django 4.1.1 on 2022-11-14 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_villagernames_remove_villagerlastname_race_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillagerFirstNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, unique=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.race')),
            ],
        ),
        migrations.CreateModel(
            name='VillagerLastNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, unique=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.race')),
            ],
        ),
        migrations.DeleteModel(
            name='VillagerNames',
        ),
    ]
