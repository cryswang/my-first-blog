# Generated by Django 2.2.13 on 2020-06-27 02:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='project', max_length=200)),
                ('context', models.DateTimeField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField()),
                ('work_period', models.CharField(default='date - date', max_length=200)),
            ],
        ),
    ]
