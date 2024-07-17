from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Kundalik(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250),
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


    @classmethod
    def get_total_expenses(cls, user):
        total = cls.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        return total if total is not None else 0.00