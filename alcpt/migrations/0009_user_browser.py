# Generated by Django 3.1.1 on 2021-03-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcpt', '0008_exam_remaining_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='browser',
            field=models.TextField(null=True),
        ),
    ]
