# Generated by Django 5.1.2 on 2024-10-12 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_apartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspaceDeDetente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.myimage')),
            ],
        ),
    ]
