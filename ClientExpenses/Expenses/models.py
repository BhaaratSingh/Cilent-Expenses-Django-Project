from django.db import models
from django.utils import  timezone

# Create your models here.


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, blank=False, unique=True)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['date_created', ]


#
#
# Expenses belong to a Client. A Client must have at least a name property.
#


class Expenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 150, blank=False, unique=True)
    description = models.CharField(max_length = 255)
    currency = models.CharField(max_length=30)
    amount = models.FloatField(null=False)
    timestampOfExpense = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Expenses"
        verbose_name_plural = "Expenses"
        ordering = ['timestampOfExpense', ]

