from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

# Create your models here.


class Customuser(AbstractUser):
    phone = PhoneNumberField(_("Phone Number"))

    def __str__(self) -> str:
        return self.username
    

class PostalWorker(models.Model):
    user = models.ForeignKey("accounts.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE)
    orders_count  = models.PositiveIntegerField(_("Orders Count"), default=0) 
