# Generated by Django 3.1.7 on 2021-03-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to='post_pics'),
        ),
    ]
