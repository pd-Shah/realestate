from kavenegar import KavenegarAPI
from django.views.generic import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import (
    InputPhoneNumber,
    InputCodeForm,
)
from .models import Phone
from random import randint


class SendSMS(FormView):
    template_name = 'sms/phone_number.html'
    form_class = InputPhoneNumber
    success_url = reverse_lazy('sms:check_code')

    def send_sms(self, number):
        try:
            phone = Phone.objects.get(phone_number=number)
        except Exception:
            phone = Phone(phone_number=number)
            phone.code = randint(10000, 99999)
            phone.save()
        try:
            api = KavenegarAPI('526D6956397A6B786F30464C38724E302F5A67646E6156322F677A7037633573447349373955426C5473343D')
            params = {
                'receptor': str(phone.phone_number),
                'message': str(phone.code),
            }
            response = api.sms_send(params)
            print(response)
        except Exception as e:
            print(e)

    def form_valid(self, form):
        number = form.cleaned_data['phone_number']
        self.send_sms(number)
        return super().form_valid(form)


class CheckCode(FormView):
    template_name = 'sms/code_input.html'
    form_class = InputCodeForm
    success_url = reverse_lazy('advertisement:my_ads')

    def form_valid(self, form):
        number = form.cleaned_data['phone_number']
        phone = Phone.objects.get(phone_number=number)
        if int(form.cleaned_data['code']) == int(phone.code):
            self.request.session['phone'] = number
            return super().form_valid(form)
        else:
            return redirect('/sms/check-code')
