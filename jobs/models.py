from django.db import models
from django.utils.translation import gettext_lazy as _


class Job(models.Model):
    company_name = models.ForeignKey("jobs.CompanyName", on_delete=models.CASCADE)
    vacancy_name = models.CharField(_("Наименование вакансии"), max_length=150)
    price = models.FloatField(_("Заработная плата"))
    description = models.TextField(_("Описание"))
    created_at = models.DateTimeField(_("Дата публикации"), auto_now=True)


class CompanyName(models.Model):
    name = models.CharField(_("Наименование компании"), max_length=200)
