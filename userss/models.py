from django.db import models
from django.contrib.auth.models import User
# from .utils import generates_ref_code

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Bio = models.TextField(blank=True)
    # code = models.CharField(max_length=12,blank= True)

    def __str__(self):
        return f'{self.user.username}'
    # def get_recomded_profile(self):
    #     pass
    # def save(self,*args, **kwargs):
    #     if self.code == "":
    #         code = generates_ref_code()
    #         self.code = code
    #     super().save(*args, **kwargs)

class loan(models.Model):
    user = models.OneToOneField(profile,on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=True)
    # ,on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits =7,decimal_places =2)
    Approved = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Amount}"

    
