# Generated by Django 4.1 on 2022-08-19 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "email",
                    models.CharField(
                        max_length=20, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("hostel", models.CharField(max_length=20)),
                ("photo_link", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hostel", models.CharField(max_length=20)),
                ("post_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="VoterList",
            fields=[
                (
                    "email",
                    models.CharField(
                        max_length=20, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("hostel", models.CharField(max_length=20)),
                ("voted", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="voting.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="voting.voterlist",
                    ),
                ),
                (
                    "vote_casted",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="voting.candidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contesting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="voting.candidate",
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="voting.post"
                    ),
                ),
            ],
        ),
    ]
