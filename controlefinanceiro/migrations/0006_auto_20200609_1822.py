# Generated by Django 3.0.4 on 2020-06-09 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinanceiro', '0005_contaspagar_classificacoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contaspagar',
            name='classificacoes',
        ),
        migrations.AddField(
            model_name='contaspagar',
            name='classificacoes',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='controlefinanceiro.ClassificacaoPagar'),
        ),
    ]