from .models import Conta, Transacoes, Extrato
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ContaSerializer, TransacaoSerializer, ExtratoTransacoesConta


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()

    @action(detail=True, methods=['get'])
    def extrato(self, request, pk=None):
        queryset = Conta.objects.filter(pk=pk)
        self.serializer_class = ExtratoTransacoesConta
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data[0]['extrato']:
            serializer.data[0]['extrato']['transacoes'] = serializer.data[0]['transacoes']
            return Response(serializer.data[0]['extrato'])
        else:
            return Response("Esta conta não possui transações cadastradas", status=404)

    @action(detail=True, methods=['get'])
    def extrato_credito(self, request, pk=None):
        queryset = Conta.objects.filter(pk=pk)
        self.serializer_class = ExtratoTransacoesConta
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data[0]['extrato']:
            transacoes_credito = {'transacoes': []}
            for transaction in serializer.data[0]['transacoes']:
                if transaction['tipo_transacao'] == 'credito':
                    transacoes_credito['transacoes'].append(transaction)
            serializer.data[0]['extrato']['transacoes'] = transacoes_credito['transacoes']
            return Response(serializer.data[0]['extrato'])
        else:
            return Response("Esta conta não possui transações cadastradas", status=404)

    @action(detail=True, methods=['get'])
    def extrato_debito(self, request, pk=None):
        queryset = Conta.objects.filter(pk=pk)
        self.serializer_class = ExtratoTransacoesConta
        serializer = self.get_serializer(queryset, many=True)
        transacoes_debito = {'transacoes': []}
        if serializer.data[0]['extrato']:
            for transaction in serializer.data[0]['transacoes']:
                if transaction['tipo_transacao'] == 'debito':
                    transacoes_debito['transacoes'].append(transaction)
            serializer.data[0]['extrato']['transacoes'] = transacoes_debito['transacoes']
            return Response(serializer.data[0]['extrato'])
        else:
            return Response("Esta conta não possui transações cadastradas", status=404)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransacaoSerializer
    queryset = Transacoes.objects.all()

    def create(self, request, *args, **kwargs):
        transacao_serializer = TransacaoSerializer(data=request.data)
        if not transacao_serializer.is_valid():
            return Response("Parâmetros incorretos", status=400)

        try:
            numero_conta = Conta.objects.only('numero_conta').get(numero_conta=request.data['numero_conta'])
        except Conta.DoesNotExist:
            return Response("Número da conta para realizar a movimentação não existe", status=404)

        conta = Conta.objects.filter(numero_conta=request.data['numero_conta'])
        saldo_final = None
        if request.data['tipo_transacao'] == 'debito':
            saldo_final = float(conta[0].saldo) - \
                          float(request.data['valor'])
        elif request.data['tipo_transacao'] == 'credito':
            saldo_final = float(conta[0].saldo) + float(request.data['valor'])
        if saldo_final:
            extrato = Extrato.objects.filter(numero_conta=numero_conta)
            if not extrato:
                Extrato.objects.create(saldo_inicial=conta[0].saldo,
                                       numero_conta=numero_conta,
                                       saldo_final=saldo_final)
            elif extrato:
                extrato.update(saldo_final=saldo_final)
            conta.update(saldo=str(saldo_final))

        transacao_serializer.save()
        return Response(transacao_serializer.data, status=201)
