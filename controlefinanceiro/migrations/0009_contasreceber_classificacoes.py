# Generated by Django 3.0.4 on 2020-06-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinanceiro', '0008_contasreceber'),
    ]

    operations = [
        migrations.AddField(
            model_name='contasreceber',
            name='classificacoes',
            field=models.ManyToManyField(to='controlefinanceiro.ClassificacaoPagar'),
        ),
    ]
