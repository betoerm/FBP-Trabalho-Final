# Generated by Django 3.0.4 on 2020-06-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinanceiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='data_pagamento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contaspagar',
            name='data_vencimento',
            field=models.DateField(),
        ),
    ]