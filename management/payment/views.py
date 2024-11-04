# # import stripe
# # from django.shortcuts import get_object_or_404, redirect
# # from django.urls import reverse
# # from django.views import View
# #
# #
# # from management.package.models import Package
# # from travel_management import settings
# #
# # stripe.api_key = settings.STRIPE_SECRET_KEY
# #
# # class CreateCheckoutSessionView(View):
# #     def post(self, request, *args, **kwargs):
# #         package_destination = self.kwargs['package_destination']
# #         package = get_object_or_404(Package, destination=package_destination)
# #         YOUR_DOMAIN = "http://127.0.0.1:8000"  # Change to your domain
# #
# #         # Create Stripe Checkout Session
# #         checkout_session = stripe.checkout.Session.create(
# #             payment_method_types=['card'],
# #             line_items=[{
# #                 'price_data': {
# #                     'currency': 'cad',
# #                     'unit_amount': package.price,
# #                     'product_data': {
# #                         'name': package.destination,
# #                     },
# #                 },
# #                 'quantity': 1,
# #             }],
# #             mode='payment',
# #             success_url=YOUR_DOMAIN + reverse('success_view'),
# #             cancel_url=YOUR_DOMAIN + reverse('cancel_view'),
# #         )
# #         return redirect(checkout_session.url)
#
#
# # by Ravinder
# # views.py
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.shortcuts import render
stripe.api_key = settings.STRIPE_SECRET_KEY

def HomePageView(request):
    return render(request, 'payment/home.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
# payments/views.py

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'destination': 'package.destination',
                        'quantity': 1,
                        'currency': 'cad',
                        'amount': 'package.price',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
# payments/views.py

class SuccessView(TemplateView):
    template_name = 'payment/success.html'


class CancelledView(TemplateView):
    template_name = 'payment/cancelled.html'


stripe.api_key="sk_test_51PBMa7IzasFhrxZN79CK97nWsEEcyFZtRGTs96la3xJja4CldAlsub5RrLzl5OPItd64pucUmRKIOUjuaxrnRVAy00oRmaqVnx"


