# Generated by Django 4.1 on 2022-08-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0003_alter_candidate_email_alter_voterlist_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="photo_link",
        ),
        migrations.AlterField(
            model_name="voterlist",
            name="voted",
            field=models.BooleanField(default=False),
        ),
    ]
