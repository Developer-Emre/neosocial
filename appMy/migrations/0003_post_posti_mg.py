# Generated by Django 4.2.1 on 2023-08-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_post_posttext'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postİmg',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='post görsel'),
        ),
    ]
