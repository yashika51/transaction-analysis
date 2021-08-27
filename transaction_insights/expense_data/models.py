"""Script to create model for data storage"""

from django.db import models


class ExpenseData(models.Model):
    category = models.TextField(null=False)
    year_month = models.DateField(null=False)
    amount = models.FloatField(null=False)
