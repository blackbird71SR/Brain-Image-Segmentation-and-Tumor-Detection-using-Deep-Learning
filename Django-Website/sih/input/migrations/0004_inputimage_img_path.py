# Generated by Django 2.1.7 on 2019-03-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0003_auto_20190226_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputimage',
            name='img_path',
            field=models.FilePathField(default='none', path='/media/input/test.nii.gz'),
            preserve_default=False,
        ),
    ]
