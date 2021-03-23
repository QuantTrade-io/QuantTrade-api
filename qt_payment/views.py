import stripe
from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class Payment(APIView):

    def post(self, request):

        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
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
