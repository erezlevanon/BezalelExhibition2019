# Generated by Django 2.2.3 on 2019-07-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0007_auto_20190710_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
