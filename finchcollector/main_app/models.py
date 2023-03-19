from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.contrib.auth.models import User

class Toy(models.Model):
     name = models.CharField(max_length=50)
     color = models.CharField(max_length=20)

     def __str__(self):
          return self.name
     
     def get_absolute_url(self):
         return reverse("toys_detail", kwargs={"pk": self.id}) # we used pk because we are going to use class based views
     


class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    length = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    upload = models.ImageField(upload_to ='main_app/static/uploads/', blank=True) # default ="" is like blank=True
    toy = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete= models.CASCADE)



    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

# A tuple of 2-tuples
MEALS = (
     ('B', 'Breakfast'),
     ('L', 'Lunch'),
     ('D', 'Dinner'),
)
class Feeding(models.Model):
      date = models.DateField()
      meal = models.CharField(
        max_length=2,
        choices= MEALS,
        default= MEALS[0][0]                
      )
      finch = models.ForeignKey(Finch, on_delete=models.CASCADE) # to delete the feeding when we delete the finch
      class Meta:
           ordering = ['-date']
      
      

