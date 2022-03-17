from libpythonpro.spam.enviador_de_email import Enviador


def  test_criar_enviador_de_email():
     enviador = Enviador()
     assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'gesli.medina@gmail.com',
        'santannathiago@gmail.com',
        'Curso Python Pro',
        'Primeira turma aberta.'
    )
    assert 'gesli.medina@gmail.com' in resultado