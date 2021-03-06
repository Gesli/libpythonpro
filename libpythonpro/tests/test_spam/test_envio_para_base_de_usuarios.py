from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gesli.medina@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gesli', email='gesli.medina@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'santannathiago@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'santannathiago@gmail.com',
        'gesli.medina@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )