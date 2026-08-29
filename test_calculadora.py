from calculadora import soma, subtracao, multiplicacao, divisao


def test_soma():
    assert soma(10, 5) == 15


def test_subtracao():
    assert subtracao(10, 5) == 5


def test_multiplicacao():
    assert multiplicacao(10, 5) == 50


def test_divisao():
    assert divisao(10, 5) == 2


def test_divisao_por_zero():
    try:
        divisao(10, 0)
        assert False
    except ValueError:
        assert True