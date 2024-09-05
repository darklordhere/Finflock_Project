from django.db import models

class Table1(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Table2(models.Model):
    table1 = models.ForeignKey(Table1, related_name='table2_items', on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.description} ({self.quantity})"
