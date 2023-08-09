from django.db import models
from django.contrib.auth.models import AbstractUser
class Track(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

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
   
