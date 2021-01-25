from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContaViewSet, TransactionViewSet

router_conta = DefaultRouter()
router_conta.register('', ContaViewSet, basename='contas')
router_conta.register('', ContaViewSet, basename='contas<numero_conta>/extrato')
router_conta.register('', ContaViewSet, basename='contas<numero_conta>/extrato_credito')
router_conta.register('', ContaViewSet, basename='contas<numero_conta>/extrato_debito')

router_transaction = DefaultRouter()
router_transaction.register('', TransactionViewSet, basename='debitar_creditar')

contas_urls = router_conta.urls
transaction_urls = router_transaction.urls
