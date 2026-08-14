# Desafios de Testes em Python

Projeto contendo 5 desafios de testes automatizados utilizando **Python** e **pytest**.

## Estrutura do projeto

```text
projeto/
│
├── Desafio1/
│   ├── desafio1.py
│   └── test_desafio1.py
│
├── Desafio2/
│   ├── desafio2.py
│   └── test_desafio2.py
│
├── Desafio3/
│   ├── desafio3.py
│   └── test_desafio3.py
│
├── Desafio4/
│   ├── desafio4.py
│   └── test_desafio4.py
│
├── Desafio5/
│   ├── desafio5.py
│   └── test_desafio5.py
│
└── README.md
```

## Requisitos

* Python 3 instalado
* `pip`
* `pytest`

## 1. Criar o ambiente virtual

Na pasta raiz do projeto, execute:

### Windows

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

## 2. Instalar o pytest

Com o ambiente virtual ativado:

```bash
pip install pytest
```

## 3. Executar todos os testes

Na **pasta raiz do projeto**, execute:

```bash
pytest
```

Esse único comando procura automaticamente os arquivos de teste, como:

```text
test_desafio1.py
test_desafio2.py
test_desafio3.py
test_desafio4.py
test_desafio5.py
```

e executa todos os testes dos cinco desafios.

Ao final, o `pytest` exibirá um resumo indicando quantos testes passaram ou falharam.

## Executar um desafio específico

Caso seja necessário executar somente um dos desafios:

```bash
pytest Desafio1/
```

ou:

```bash
pytest Desafio2/
```

E assim por diante.

## Objetivo

Os desafios abordam diferentes conceitos de testes automatizados, incluindo:

* Testes unitários com `pytest`;
* Parametrização de testes;
* Testes de casos válidos e inválidos;
* Validação de CPF;
* Isolamento de dependências;
* Uso de `Mock`;
* Injeção de dependência;
* Fixtures para preparação comum dos testes.

## Comando principal

Depois de criar e ativar a `venv` e instalar o `pytest`, todos os testes podem ser executados com:

```bash
pytest
```

**Esse é o comando único utilizado para executar a suíte completa de testes.**
