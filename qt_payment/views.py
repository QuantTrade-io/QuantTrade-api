import stripe
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class Payment(APIView):

    def post(self, request):

        QUANTTRADE_PRODUCT = settings.STRIPE_PRICE_ID

        try:
            print('try')
            checkout_session = stripe.checkout.Session.create(
                success_url="https://example.com/success",
                cancel_url="https://example.com/cancel",
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": QUANTTRADE_PRODUCT,
                        "quantity": 1,
                    },
                ],
                mode="subscription",
                )

            return Response({'id': checkout_session.id})

        except Exception as error:
            raise ValidationError(({"error": error}))


@csrf_exempt
def stripe_webhook(request):
    print('WEBHOOK!!')

    # Using Django
    # endpoint_secret = 'whsec_ZJKdBuoAbKjkgSA3BAKg8NbAqHzGj2Yi'

    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(e, status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':

        payment_intent = event.data.object
        print('[1]', payment_intent)
        # contains a stripe.PaymentIntent
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event.type == 'payment_method.attached':

        payment_method = event.data.object
        print('[2]', payment_method)
        # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
