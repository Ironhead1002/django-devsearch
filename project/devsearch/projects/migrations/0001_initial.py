# Generated by Django 4.0 on 2022-01-04 09:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('bbb5b137-fcd9-4033-aa0f-d0371b92d0c2'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
