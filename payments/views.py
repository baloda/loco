from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_202_ACCEPTED
from payments.services.transaction import TransactionService
from payments.serializers import TansactionSerializer
from payments.serializers import TansactionIDSerializer

# Create your views here.

class TransactionListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        records = TransactionService.get_all()
        return Response(
            data=TansactionSerializer(records, many=True).data,
            status=HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        record = TransactionService.create(data=request.data)
        return Response(
            data=TansactionSerializer(record).data,
            status=HTTP_201_CREATED
        )

class TransactionDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        record = TransactionService.get(id=id)
        return Response(
            data=TansactionSerializer(record).data,
            status=HTTP_200_OK
        )

    def put(self, request, id, *args, **kwargs):
        record = TransactionService.update(id=id, data=request.data)
        return Response(
            data=dict(status="ok"),
            status=HTTP_202_ACCEPTED
        )

    def delete(self, request, id, *args, **kwargs):
        return Response(status=HTTP_200_OK, data=dict(status="ok"))


class TransactionTypeAPIView(APIView):
    def get(self, request, category, *args, **kwargs):
        ids = TransactionService.get_by_types(category=category)
        return Response(status=HTTP_200_OK, data=ids)

class TransactionSumAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        hierarchical_amount_sum = TransactionService.get_hierarchical_amount_sums(id=id)
        return Response(status=HTTP_200_OK, data=hierarchical_amount_sum)