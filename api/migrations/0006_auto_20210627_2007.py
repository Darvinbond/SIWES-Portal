# Generated by Django 3.1.5 on 2021-06-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210627_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='sup_id',
            field=models.TextField(default=''),
        ),
    ]
