# Generated by Django 2.0.6 on 2018-06-08 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='timestamp',
        ),
    ]