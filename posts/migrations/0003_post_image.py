# Generated by Django 4.2.5 on 2023-10-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts'),
            preserve_default=False,
        ),
    ]
