from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world.")

def contas(request):
    html = """<h1>Contas</h1>"""

    listContas = Conta.objects.all()

    for c in listContas:
        catid = c.categoria_id
        cat = CategoriaConta.objects.get(pk=catid)

        credorid = c.credor_id
        pj = PessoaJuridica.objects.get(pk=credorid)
        credor = Pessoa.objects.get(pk=credorid)

        devedorid = c.devedor_id
        pf = PessoaFisica.objects.get(pk=devedorid)
        devedor = Pessoa.objects.get(pk=devedorid)







        html += '<li>Categoria: {}	</li>'.format(cat.tipo)

        html += '<li>Nome Credor: {}	CNPJ {}</li>'.format(credor.nome, pj.CNPJ)
        html += '<li>Nome Devedor: {}	CPF {}</li>'.format(devedor.nome,pf.CPF )

        html += '<li>Valor a pagar: {}	</li>'.format(c.valorAPagar)
        html += '<li>Valor pago: {}	</li>'.format(c.valorPago)

        return HttpResponse(html)


def contaid(request, pk):
    html = """<h1>Conta Individual</h1>"""

    c = Conta.objects.get(pk = pk)
    catid = c.categoria_id
    cat = CategoriaConta.objects.get(pk=catid)

    credorid = c.credor_id
    pj = PessoaJuridica.objects.get(pk=credorid)
    credor = Pessoa.objects.get(pk=credorid)

    devedorid = c.devedor_id
    pf = PessoaFisica.objects.get(pk=devedorid)
    devedor = Pessoa.objects.get(pk=devedorid)

    html += '<li>Categoria: {}	</li>'.format(cat.tipo)
    html += '<li>Nome Credor: {}	CNPJ {}</li>'.format(credor.nome, pj.CNPJ)
    html += '<li>Nome Devedor: {}	CPF {}</li>'.format(devedor.nome,pf.CPF )

    html += '<li>Valor a pagar: {}	</li>'.format(c.valorAPagar)
    html += '<li>Valor pago: {}	</li>'.format(c.valorPago)

    return HttpResponse(html)
