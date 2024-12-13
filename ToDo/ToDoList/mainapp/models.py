from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    Timestamp = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100,blank=True)
    Description = models.TextField(max_length=1000,blank=True)
    Due_date = models.DateField(null=True, blank=True)
    Tags = models.TextField(null=True, blank=True)  # Comma-separated tags
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.Title
