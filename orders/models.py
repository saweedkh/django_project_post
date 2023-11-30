from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.



class Order(models.Model):

    SERVICES = (
        ('1', 'Service 1'),
        ('2', 'Service 2'),
        ('3', 'Service 3'),
    )



    SHIPMENT_SIZE = (
        ('1', 'Size 1'),
        ('2', 'Size 2'),
        ('3', 'Size 3'),
        ('4', 'Size 4'),
        ('5', 'Size 5'),
        ('6', 'Size 6'),
        ('7', 'Size 7'),
        ('8', 'Size 8'),
        ('9', 'Size 9'),
        ('10', 'Size +9'),
    )


    
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    title = models.CharField(_("Order Title"), max_length=50)
    sender_user = models.ForeignKey("accounts.CustomUser", verbose_name=_("User Sender"), on_delete=models.PROTECT)
    sender_full_name = models.CharField(_("Sender Full Name"), max_length=255)
    phone_number_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Phone number must be entered in the format: '09123456789'."
    )

    sender_phone = models.CharField(
        _("Sender Phone"),
        validators=[phone_number_regex],
        max_length=11,

        
    )
    sender_address = models.TextField(_("Sender Address"))

    receiver_full_name = models.CharField(_("Receiver Full Name"), max_length=255)
    receiver_phone = models.CharField(
        _("Receiver Phone"),
        validators=[phone_number_regex],
        max_length=11,     
    )
    receiver_address = models.TextField(_("Receiver Address"))


    shipment_price = models.IntegerField(_("Shipment Price (Rial)"))
    shipment_content = models.TextField(_("Shipment Contet"))
    shipment_size = models.CharField(_("Shipment Size"), choices=SHIPMENT_SIZE, max_length=50)
    shipment_count = models.PositiveIntegerField(_("Shipment Count"))
    shipment_weight = models.PositiveIntegerField(_("Shipment Weight (Gram)"))

    choosing_Service = models.CharField(_("Choosing a Service"), choices=SERVICES, max_length=50)

    postal_worker = models.ForeignKey("accounts.PostalWorker", verbose_name=_("Postal Worker"), on_delete=models.SET_NULL, null=True)

    need_packaging = models.BooleanField(default=False, verbose_name=_("Do you need an envelope/box for postage?"))



    description = models.TextField(_("Additional Information"), blank=True)

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
    

    
