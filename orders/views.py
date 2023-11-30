from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .forms import OrderForm, TrackingCodeForm
from .models import Order
from accounts.models import PostalWorker


    
class OrderDetailView(generic.FormView, generic.View):
    template_name = 'orders/order_detail.html'
    form_class = TrackingCodeForm

    def get(self, request, *args, **kwargs):
        # عملیات مربوط به درخواست GET
        return render(request, 'orders/track.html')

    def post(self, request, *args, **kwargs):
        # عملیات مربوط به درخواست POST
        form = self.get_form()
        # tracking_code = form.cleaned_data['tracking_code']
        # order = get_object_or_404(Order, args=[tracking_code] )
        # return render(request, 'orders/order_detail.html', {'order' : order})

        if form.is_valid():
            tracking_code = form.cleaned_data['tracking_code']
            order = get_object_or_404(Order, id=tracking_code )

            # انجام هر چیزی که نیاز است با مقدار tracking_code
            return render(request, 'orders/order_detail.html', {'order' : order})
        else:
            # اگر فرم نامعتبر بود
            return HttpResponse(form.data)




class OrdercreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_create.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender_user = self.request.user
        try : 
            obj.postal_worker = PostalWorker.objects.order_by('orders_count').first()
        except :
            messages.error(self.request, _('No postal workers available'))
            return self.form_invalid(form)

        obj.save()
        messages.success(self.request, _('Order successfully created'))
        return super().form_valid(form)
    
