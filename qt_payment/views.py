import stripe

from django.conf import settings

# from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.response import Response
from django.core.exceptions import SuspiciousOperation
from .serializers import PaymentSerializer
from django.http import JsonResponse


class Payment(APIView):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    PRODUCTS_STRIPE_PRICING_ID = {
        'quanttrade_sub': 'price_1IRhMmF1Q4ZxgxN3LrHOeyi1',
    }

    serializer_class = PaymentSerializer

    def post(self, request):
        # serializer = self.serializer_class(data=request.data)

        try:
            print('try')
            checkout_session = stripe.checkout.Session.create(
                success_url="https://example.com/success",
                cancel_url="https://example.com/cancel",
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": 'price_1IRhMmF1Q4ZxgxN3LrHOeyi1',
                        "quantity": 1,
                    },
                ],
                mode="subscription",
                )

            return JsonResponse({'id': checkout_session.id})

        except Exception as e:
            print(e)
            raise SuspiciousOperation(e)
