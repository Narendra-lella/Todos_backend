# Generated by Django 4.2.7 on 2023-12-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totomodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]