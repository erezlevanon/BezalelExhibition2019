# Generated by Django 2.2.3 on 2019-07-10 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0004_graduate_image_0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graduate',
            old_name='image_0',
            new_name='profile_image',
        ),
        migrations.CreateModel(
            name='ProcessImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('graduate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduates.Graduate')),
            ],
        ),
    ]
