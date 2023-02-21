from django.db import models

class Order(models.Model):
    orderID = models.CharField(max_length=100)
    orderItem = models.TextField()
    orderBudget = models.IntegerField()
    orderDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name