from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from api.models import playList,Resources,RoadMaps
from api.models import Track
from phonenumber_field.modelfields import PhoneNumberField


class userCustom(AbstractUser):
    track=models.ForeignKey(Track,on_delete=models.CASCADE,default=None,blank=True,null=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        related_name='customer_user_permissions',
        help_text=('Specific permissions for this customer.'),
        related_query_name='customer_user_permission',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        related_name='customer_groups',
        help_text=('The groups this customer belongs to. A customer will get all permissions granted to each of their groups.'),
        related_query_name='customer_group',
    )

    def __str__(self):
        return self.username



class profile(models.Model):
    user=models.OneToOneField(userCustom,on_delete=models.CASCADE)
    roadmaps=models.ManyToManyField(RoadMaps)
    playList=models.ManyToManyField(playList)
    resource=models.ManyToManyField(Resources)
    def __str__(self):
        return self.user.username
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=userCustom)
    
   
class Contact(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    message=models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"