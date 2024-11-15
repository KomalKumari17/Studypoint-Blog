# Generated by Django 5.1.1 on 2024-09-20 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='tutorial/')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.topics')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='tutorial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cms.tutorial'),
            preserve_default=False,
        ),
    ]
