# Generated by Django 2.2.13 on 2020-06-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200626_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(default='desc'),
        ),
        migrations.AlterField(
            model_name='involvement',
            name='description',
            field=models.TextField(default='desc'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='text'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='desc'),
        ),
    ]