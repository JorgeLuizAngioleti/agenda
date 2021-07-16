# Generated by Django 2.0.5 on 2018-05-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('aula', models.CharField(choices=[('1m', '1ª aula matutino'), ('2m', '2ª aula matutino'), ('3m', '3ª aula matutino'), ('4m', '4ª aula matutino'), ('5m', '5ª aula matutino')], max_length=2, verbose_name='Aula')),
                ('nome', models.CharField(max_length=50)),
                ('tema', models.CharField(max_length=30)),
                ('objetivo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Aparelho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='eletronico',
            field=models.ForeignKey(on_delete=False, to='meu.Aparelho'),
        ),
    ]
