# Generated by Django 2.0.5 on 2018-05-14 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meu', '0018_aparelho_escola'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparelho',
            name='escola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meu.Escola'),
        ),
    ]
