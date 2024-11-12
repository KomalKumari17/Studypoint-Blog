# Generated by Django 5.1.1 on 2024-09-30 14:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tutorial_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.tutorial'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]