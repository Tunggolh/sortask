# Generated by Django 5.0.3 on 2024-03-09 19:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortask', '0001_add_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sortask.project')),
            ],
        ),
    ]
