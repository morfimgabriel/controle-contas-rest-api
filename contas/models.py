from django.core.validators import DecimalValidator
from django.db import models

tipos_transacoes = (
    ('debito', 'debito'),
    ('credito', 'credito'),
)


class Conta(models.Model):
    numero_conta = models.CharField(primary_key=True, max_length=30)
    nome_usuario = models.CharField(max_length=30)
    saldo = models.DecimalField(max_digits=20, decimal_places=2,
                                validators=[DecimalValidator(decimal_places=2, max_digits=20)],
                                help_text="Colocar o saldo com 2 casas decimais ex: 10.00")

    class Meta:
        managed = True
        db_table = 'conta'

    def __str__(self):
        return f'{self.nome_usuario} - {self.numero_conta}'


class Transacoes(models.Model):
    tipo_transacao = models.CharField(max_length=30, choices=tipos_transacoes, default="")
    valor = models.DecimalField(max_digits=20, decimal_places=2,
                                validators=[DecimalValidator(decimal_places=2, max_digits=20)],
                                help_text="Colocar o valor com 2 casas decimais ex: 10.00")
    data_movimento = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=30, blank=True, default="")
    numero_conta = models.ForeignKey(Conta, related_name='transacoes', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'transacoes'

    def __str__(self):
        return f'Transacao - "{self.descricao}" / Tipo "{self.tipo_transacao}" / Conta "{self.numero_conta}"'


class Extrato(models.Model):
    numero_conta = models.OneToOneField(Conta, related_name='extrato', on_delete=models.CASCADE, primary_key=True)
    saldo_inicial = models.DecimalField(max_digits=20, decimal_places=2, default="0")
    saldo_final = models.DecimalField(max_digits=20, decimal_places=2, default="0")

    class Meta:
        managed = True
        db_table = 'extrato'
