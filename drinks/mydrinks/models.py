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

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def meta(self):
        try :
            first = self.comment_set.all().order_by("date")[0]
            return "by %s rated as %s" % (first.name, first.get_rating_display())
        except :
            return "Segmentation Fault : No First Comment"

    def comment(self):
        try :
            first = self.comment_set.all().order_by("date")[0]
            return first.content
        except :
            return "Segmentation Fault : No First Comment"

    def comments(self):
        try :
            more = self.comment_set.all().order_by("date")[1:]
            return more
        except :
            return "Segmentation Fault : No More Comments"

class Comment(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    drink = models.ForeignKey(Drink)

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

#
# FORMS
#

from django.forms import ModelForm

class DrinkForm(ModelForm):
    class Meta:
        model = Drink

class CommentForm(ModelForm):
    class Meta:
        model = Comment
