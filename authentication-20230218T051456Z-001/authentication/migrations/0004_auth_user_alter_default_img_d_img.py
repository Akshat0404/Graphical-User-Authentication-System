# Generated by Django 4.1.5 on 2023-01-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_default_img_img_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userimg', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='default_img',
            name='d_img',
            field=models.ImageField(upload_to='image'),
        ),
    ]
