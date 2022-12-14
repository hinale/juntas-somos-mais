# Generated by Django 4.0.6 on 2022-08-14 14:50

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsm_app', '0005_alter_pedido_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(on_delete=builtins.id, to='jsm_app.usuario'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='figura',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
