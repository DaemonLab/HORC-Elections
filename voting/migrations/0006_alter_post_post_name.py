# Generated by Django 4.1 on 2022-08-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0005_alter_candidate_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_name",
            field=models.CharField(max_length=40),
        ),
    ]
