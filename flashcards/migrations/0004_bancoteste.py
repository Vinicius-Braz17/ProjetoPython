# Generated by Django 5.0.1 on 2024-01-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_flashcarddesafio_desafio'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancoTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('idade', models.IntegerField()),
                ('data_nascimento', models.DateField()),
                ('lugar_nascimento', models.CharField(choices=[('1', 'São Paulo'), ('2', 'Rio de Janeiro'), ('3', 'Curitiba')], max_length=1)),
            ],
        ),
    ]
