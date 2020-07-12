from django.db import models

# Create your models here.
class Item(models.Model):
    item_id=models.IntegerField()
    item_name=models.CharField(max_length=25)
    price=models.FloatField()
    quantity=models.FloatField()
    total=models.FloatField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return(self.item_name)
