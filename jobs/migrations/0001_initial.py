# Generated by Django 4.1.2 on 2022-11-05 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompanyName",
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
                    "name",
                    models.CharField(
                        max_length=200, verbose_name="Наименование компании"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                    "vacancy_name",
                    models.CharField(
                        max_length=150, verbose_name="Наименование вакансии"
                    ),
                ),
                ("price", models.FloatField(verbose_name="Заработная плата")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата публикации"),
                ),
                (
                    "company_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobs.companyname",
                    ),
                ),
            ],
        ),
    ]