# Generated by Django 3.0.5 on 2022-04-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_auto_20220218_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]