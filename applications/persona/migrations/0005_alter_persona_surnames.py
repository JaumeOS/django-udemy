# Generated by Django 4.1.5 on 2023-01-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_persona_hoja_vida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='surnames',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre completo'),
        ),
    ]