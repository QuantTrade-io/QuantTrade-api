import stripe
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

stripe.api_key = (
    'sk_test_51HkMJIF1Q4ZxgxN3TblMpv57Yn4w4SMwUIif62LkFmsslrrIE0c7lNLoCExHIFrLaWTzslEFPAQd2GMXgbKEK36P00u2rvGA71'
)


class Payment(APIView):
    def post(self, request):

        test_payment_intent = stripe.PaymentIntent.create(
            amount=1000, currency='pln',
            payment_method_types=['card'],
            receipt_email='test@example.com')
        return Response(status=status.HTTP_200_OK, data=test_payment_intent)
