# Generated by Django 3.2.9 on 2022-04-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetwo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='videos',
            field=models.FileField(default=1, upload_to='vdeo/%y'),
            preserve_default=False,
        ),
    ]
