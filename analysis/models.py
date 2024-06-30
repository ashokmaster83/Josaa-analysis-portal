from django.db import models

class Data(models.Model):
    Institue = models.CharField(max_length=500)
    Branch = models.CharField(max_length=500)
    Quota = models.CharField(max_length=500)
    Seat_Type = models.CharField(max_length=500)
    Opening_Rank = models.IntegerField()
    Closing_Rank = models.IntegerField()
    Year = models.IntegerField()
    Round = models.IntegerField()
    
    def __str__(self):
        return f"{self.Institue} - {self.Branch} - {self.Quota} - {self.Seat_Type} - {self.Opening_Rank} - {self.Closing_Rank} - {self.Year} - {self.Round}"
    
    

# Create your models here.
