# Generated by Django 4.1.5 on 2023-01-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_user_u_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_img',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
