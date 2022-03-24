import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gesli', email='gesli.medina@gmail.com'),
            Usuario(nome='Thiago', email='santannathiago@gmail.com')
        ],
        [
            Usuario(nome='Gesli', email='gesli.medina@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gesli.medina@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gesli', email='gesli.medina@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'santannathiago@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    assert enviador.parametros_de_envio ==(
        'santannathiago@gmail.com',
        'gesli.medina@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )