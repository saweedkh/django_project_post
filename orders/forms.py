from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = (
            'title',
            'sender_full_name', 
            'sender_phone', 
            'sender_address', 
            'receiver_full_name', 
            'receiver_phone', 
            'receiver_address', 
            'shipment_price', 
            'shipment_content', 
            'shipment_size', 
            'shipment_count', 
            'shipment_weight', 
            'choosing_Service', 
            'need_packaging', 
            'description', 
            )
        
class TrackingCodeForm(forms.Form):
    tracking_code = forms.CharField(label='Tracking Code', max_length=50)
