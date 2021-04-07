import stripe
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model


stripe.api_key = settings.STRIPE_SECRET_KEY


class Payment(APIView):
    def post(self, request):

        QUANTTRADE_PRODUCT = settings.STRIPE_PRICE_ID

        try:
            print("try")
            checkout_session = stripe.checkout.Session.create(
                success_url=settings.PAYMENT_SUCCESS_URL,
                cancel_url=settings.PAYMENT_FAILED_URL,
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": QUANTTRADE_PRODUCT,
                        "quantity": 1,
                    },
                ],
                mode="subscription",
            )

            return Response({"id": checkout_session.id})

        except Exception as error:
            raise ValidationError(({"error": error}))


class StripeWebhook(APIView):
    # endpoint secret: whsec_ZJKdBuoAbKjkgSA3BAKg8NbAqHzGj2Yi

    @csrf_exempt
    def post(self, request):
        payload = request.body
        event = None

        try:
            event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
        except ValueError as error:
            raise error

        if event.type == "payment_intent.succeeded":
            email = event.data.object.charges["data"][0].billing_details.email
            self._set_user_paid(email)

        elif event.type == "payment_method.attached":
            pass

        elif event.type == "customer.subscription.created":
            print("customer.subscription.created ADDED")

        elif event.type == "charge.succeeded":
            print("charge.succeeded ADDED")

        elif event.type == "invoice.created":
            print("invoice.created ADDED")

        elif event.type == "checkout.session.completed":
            print("checkout.session.completed ADDED")

        elif event.type == "invoice.finalized":
            print("invoice.finalized ADDED")

        elif event.type == "invoice.payment_succeeded":
            print("invoice.payment_succeeded ADDED")

        elif event.type == "payment_intent.created":
            print("payment_intent.created ADDED")

        elif event.type == "invoice.updated":
            print("invoice.updated ADDED")

        elif event.type == "invoice.paid":
            print("invoice.paid ADDED")

        elif event.type == "customer.subscription.updated":
            print("customer.subscription.updated ADDED")

        elif event.type == "customer.created":
            print("customer.created ADDED")

        elif event.type == "invoice.updated":
            print("invoice.updated ADDED")

        else:
            print("Unhandled event type {}".format(event.type))

        return HttpResponse(status=200)

    def _set_user_paid(self, email):
        print("Settings user to paid")
        User = get_user_model()
        new_customer = User.objects.get(username=email)
        new_customer.paid_subscription = True
        new_customer.save()
