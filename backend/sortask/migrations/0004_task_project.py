# Generated by Django 5.0.3 on 2024-03-11 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortask', '0003_alter_task_description_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='sortask.project'),
            preserve_default=False,
        ),
    ]
