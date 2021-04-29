# Generated by Django 3.2 on 2021-04-29 19:46

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210421_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=blog.models.user_directory_path),
            preserve_default=False,
        ),
    ]