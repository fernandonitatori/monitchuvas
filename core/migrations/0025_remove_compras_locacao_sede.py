# Generated by Django 3.2.8 on 2021-10-27 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_rename_locacao_acao_sede_locacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras_locacao',
            name='sede',
        ),
    ]
