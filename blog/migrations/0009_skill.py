# Generated by Django 2.2.13 on 2020-06-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200623_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='skill', max_length=200)),
                ('experienced', models.BooleanField(default='False')),
                ('level', models.IntegerField(default='0')),
            ],
        ),
    ]