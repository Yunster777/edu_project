# Generated by Django 5.0.1 on 2024-01-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
