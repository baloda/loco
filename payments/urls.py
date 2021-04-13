from django.urls import path
from payments.views import TransactionListAPIView
from payments.views import TransactionDetailView
from payments.views import TransactionTypeAPIView
from payments.views import TransactionSumAPIView

urlpatterns = [
    path('transaction/', TransactionListAPIView.as_view()),
    path('transaction/<int:id>/', TransactionDetailView.as_view()),

    path('transaction/types/<str:category>/', TransactionTypeAPIView.as_view()),
    path('transaction/sums/<int:id>/', TransactionSumAPIView.as_view()),
]

