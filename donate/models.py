from django.db import models
from core.models import HotdogUser


class Donation(models.Model):
    user = models.ForeignKey(HotdogUser, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Donation by {self.user.username} : {self.amount}'