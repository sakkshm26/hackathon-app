# Generated by Django 4.2 on 2023-04-21 15:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0004_alter_submission_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="hackathon",
            name="reward_prize",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]