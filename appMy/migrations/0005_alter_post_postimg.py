# Generated by Django 4.2.1 on 2023-08-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_rename_posti_mg_post_postimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImg',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='post görsel'),
        ),
    ]
