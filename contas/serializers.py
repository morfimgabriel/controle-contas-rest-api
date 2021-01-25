from rest_framework import serializers
from .models import Conta, Transacoes, Extrato


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = ['tipo_transacao', 'valor', 'data_movimento', 'descricao', 'numero_conta']


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'


class ContasTransacoesSerializer(serializers.ModelSerializer):
    transactions = TransacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Conta
        fields = [
            'numero_conta',
            'saldo',
            'transactions'
        ]


class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = '__all__'


class ExtratoTransacoesConta(serializers.ModelSerializer):
    extrato = ExtratoSerializer(read_only=True)
    transacoes = TransacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Conta
        fields = [
            'numero_conta',
            'extrato',
            'transacoes',
        ]
