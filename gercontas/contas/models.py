from django.db import models

class Pessoa(models.Model):

    nome = models.CharField( max_length=200)




    def getNome(self):
        return self.nome




class PessoaFisica(Pessoa):
    CPF= models.CharField(max_length=20)



class PessoaJuridica(Pessoa):
    CNPJ= models.CharField(max_length=20)








class CategoriaConta(models.Model):
    tipo = models.CharField(max_length=100)





class Conta (models.Model):
    categoria = models.ForeignKey(CategoriaConta, on_delete=models.CASCADE)
    credor = models.ForeignKey(PessoaJuridica, on_delete=models.CASCADE)
    devedor = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE)
    dataVencimento  = models.DateTimeField('data vencimento')
    dataPagamento  = models.DateTimeField('data pagamento')
    valorAPagar = models.FloatField()
    valorPago = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
