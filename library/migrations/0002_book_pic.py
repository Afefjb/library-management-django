# Generated by Django 3.0.5 on 2022-02-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='book_image'),
        ),
    ]