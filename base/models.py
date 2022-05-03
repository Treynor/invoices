from django.db import models

# Create your models here.

class Invoice(models.Model):
    supplier = models.CharField(max_length=50)
    invoiceNumber = models.CharField(max_length=50)
    reason = models.CharField(max_length=100)
    reportedTo = models.CharField(max_length=100)
    solved = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier
        
       
