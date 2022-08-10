# Generated by Django 4.0.6 on 2022-08-10 00:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jsm_app', '0002_auto_20220805_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('quantidade', models.IntegerField(default=1)),
                ('valorUnitario', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(default='NOVO', max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsm_app.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsm_app.produto')),
            ],
        ),
    ]
