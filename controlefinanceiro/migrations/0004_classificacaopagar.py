# Generated by Django 3.0.4 on 2020-06-09 18:18

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinanceiro', '0003_auto_20200609_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]