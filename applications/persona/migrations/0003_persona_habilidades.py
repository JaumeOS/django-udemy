# Generated by Django 4.1.5 on 2023-01-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_habilidades_alter_persona_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]