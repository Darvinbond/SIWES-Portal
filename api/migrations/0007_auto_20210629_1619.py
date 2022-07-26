# Generated by Django 3.1.5 on 2021-06-29 15:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210627_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='supervisor',
            fields=[
                ('sup_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='company_sup',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='sup_id',
        ),
    ]
