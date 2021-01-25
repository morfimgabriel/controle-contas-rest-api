from django.urls import reverse

from contas.models import Conta, Transacoes
from rest_framework import status
from django.test import TestCase


class IntegrationTests(TestCase):

    def setUp(self):
        self.conta = Conta.objects.create(numero_conta='1234567', nome_usuario='gabriel', saldo='500.00')
        numero_conta = Conta.objects.only('numero_conta').get(numero_conta='1234567')
        self.transacao = Transacoes.objects.create(tipo_transacao='debito', valor='100.00', data_movimento='28/12/2018',
                                                   descricao='debito teste', numero_conta=numero_conta)

    def test_create_conta(self):
        dto = {
            "numero_conta": "115155115",
            "nome_usuario": "testando",
            'saldo': "123"
        }

        response = self.client.post(reverse('contas-list'), dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transacao_debito_credito(self):
        dto = {
            "tipo_transacao": "debito",
            "valor": "50.00",
            "data_movimento": "28/12/2018",
            "descricao": "debito teste",
            "numero_conta": '1234567',
        }

        response = self.client.post(reverse('debitar_creditar-list'), dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        dto["tipo_transacao"] = "credito"

        response = self.client.post(reverse('debitar_creditar-list'), dto, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_conta_por_numero_conta(self):
        response = self.client.get(reverse('contas-list', kwargs={'<numero_conta>': self.conta.numero_conta}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)




