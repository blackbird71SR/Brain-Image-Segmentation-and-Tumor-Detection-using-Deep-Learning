# Generated by Django 2.1.7 on 2019-03-03 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0004_inputimage_img_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputimage',
            name='img_path',
        ),
    ]