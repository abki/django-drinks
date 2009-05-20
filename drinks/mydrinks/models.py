from django.db import models

RATING_CHOICES = ((0, 'Nop'),
                  (1, 'Great'),
                  (2, 'Good'),
                  (3, 'Awesome'),
                  (4, 'Take it easy !'),
                  (5, 'Excellent'))

class Drink(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField()
    alcohol = models.PositiveIntegerField()
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
