import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def  test_criar_enviador_de_email():
     enviador = Enviador()
     assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
     ['gavelar@grsa.com.br', 'gesli.medina@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'santannathiago@gmail.com',
        'Curso Python Pro',
        'Primeira turma aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
     ['', 'gesli']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'santannathiago@gmail.com',
            'Curso Python Pro',
            'Primeira turma aberta.'
    )

