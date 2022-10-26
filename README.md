
# AtividadePytest

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Demonstração

pip install pytest


## Instalação

Instalação do pytest:

É recomendado o uso de ambientes virtuais para imports de frameworks, 
então caso não tenha instalado é bom fazer uso:
```bash
  pip install virtualenv
  
```
E para ativá-lo usa-se:
#### No Windows:
```bash
  .\Nome_da_venv/Scripts/activate
```
#### No Linux:
```bash
    source venv/Scripts/activate
```

Após isso instale o pytest:
```bash
    pip install pytest
```

## Orientações do programa:

O programa consiste em decidir se um identificador é válido. Para ele ser válido ele deve
começar com uma letra, conter apenas letras e números, e ter no mínimo 1 caractére e 
no máximo 6. 

Pasta/arquivo identifier são as funções.

Pasta/arquivo test(s) são os testes dessas funções

O arquivo de documentos entra em detalhe quais são os testes do programa.
## Testes do programa:


| ID | Modulo | Descrição | Roteiro | Resultado|
|----|--------|-----------|---------|----------|
| 1| Identificador de letras|Inserção de letras| t1| Válido|
| 1| Identificador de letras|Inserção de letras| a12345| Válido|
| 1| Identificador de letras|Inserção de letras| 78787848484| Inválido|
| 1| Identificador de letras|Inserção de letras| | Inválido|
| 1| Identificador de letras|Inserção de letras| *| Inválido|
| 1| Identificador de letras|Inserção de letras| a123456| Inválido|




