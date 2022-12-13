# Generated by Django 4.1.1 on 2022-10-23 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('Human', 'Human'), ('Dwarf', 'Dwarf'), ('Elf', 'Elf'), ('Ork', 'Ork')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cityprefix',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.race'),
        ),
        migrations.AlterField(
            model_name='citysuffix',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.race'),
        ),
    ]
