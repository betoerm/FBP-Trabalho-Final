# Generated by Django 3.0.4 on 2020-06-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinanceiro', '0006_auto_20200609_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contaspagar',
            name='classificacoes',
        ),
        migrations.AddField(
            model_name='contaspagar',
            name='classificacoes',
            field=models.ManyToManyField(to='controlefinanceiro.ClassificacaoPagar'),
        ),
    ]
