# Generated by Django 3.0.2 on 2020-01-21 12:02

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='services'),
        ),
    ]
