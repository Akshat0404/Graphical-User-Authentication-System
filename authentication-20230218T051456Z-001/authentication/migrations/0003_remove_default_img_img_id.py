# Generated by Django 4.1.5 on 2023-01-11 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_delete_getimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='default_img',
            name='img_id',
        ),
    ]
