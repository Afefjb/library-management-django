# Generated by Django 3.0.5 on 2022-02-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20220218_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='idClient',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.PositiveIntegerField(),
        ),
    ]