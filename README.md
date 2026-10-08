# Exercício 1 - Residência e Cômodos

<img width="217" height="167" alt="image" src="https://github.com/user-attachments/assets/c71d7da1-133e-4382-93d5-914aaf7f2196" />


Documentação técnica do arquivo `exercicio1_residencia.py`.

## Descrição

- Programa em Python com orientação a objetos que simula uma residência composta por cômodos.
- Permite criar uma residência, adicionar cômodos, listá-los e calcular a área total.
- A interação com o usuário é feita por um menu no console.

## Requisitos

- Python 3.6 ou superior (uso de f-strings).
- Nenhuma biblioteca externa.

## Como executar

```
python exercicio1_residencia.py
```

## Conceitos de POO aplicados

- **Composição:** os objetos `Comodo` são criados exclusivamente dentro de `Residencia`, que é a dona do ciclo de vida deles.
- **Encapsulamento:** os atributos são privados (`__nome`, `__area`, `__comodos`) e o acesso é feito apenas por métodos públicos.
- **Abstração:** o menu usa apenas os métodos públicos de `Residencia`, sem conhecer os detalhes internos.

## Classes

### `Comodo`

- Representa um cômodo da residência.
- **Atributos privados:**
  - `__nome` (str): nome do cômodo, como "sala" ou "cozinha".
  - `__area` (float): área em metros quadrados.
- **Métodos:**
  - `get_nome()`: retorna o nome.
  - `get_area()`: retorna a área.

### `Residencia`

- Representa a residência e gerencia seus cômodos.
- **Atributos privados:**
  - `__comodos` (list): lista de objetos `Comodo`.
- **Métodos:**
  - `adicionar_comodo(nome, area)`: cria um `Comodo` internamente e o adiciona à lista (composição).
  - `listar_comodos()`: retorna uma lista de textos no formato `nome - área m²`, sem expor os objetos `Comodo`.
  - `calcular_area_total()`: retorna a soma das áreas de todos os cômodos.

## Menu interativo

- **1 - Criar residência:** instancia uma nova `Residencia`.
- **2 - Adicionar cômodo:** pede nome e área e chama `adicionar_comodo`.
- **3 - Visualizar cômodos:** exibe todos os cômodos cadastrados.
- **4 - Calcular área total:** exibe a soma das áreas.
- **0 - Sair:** encerra o programa.

## Validações e tratamento de erros

- As opções 2, 3 e 4 só funcionam depois que a residência for criada (opção 1).
- Área não numérica gera a mensagem "Área inválida." (tratada com `try/except ValueError`).
- Área menor ou igual a zero é rejeitada.
- Opção de menu inexistente gera a mensagem "Opção inválida."
- Listar sem cômodos cadastrados exibe "Nenhum cômodo cadastrado."

## Exemplo de uso

```
=== MENU RESIDÊNCIA ===
Escolha: 1
Residência criada!

Escolha: 2
Nome do cômodo: Sala
Área (m²): 20
Cômodo adicionado!

Escolha: 2
Nome do cômodo: Cozinha
Área (m²): 10.5
Cômodo adicionado!

Escolha: 3
- Sala - 20.00 m²
- Cozinha - 10.50 m²

Escolha: 4
Área total: 30.50 m²
```

## Estrutura do arquivo

- `Comodo`: classe do cômodo.
- `Residencia`: classe da residência, que compõe os cômodos.
- `main()`: função com o menu interativo.
- `if __name__ == "__main__"`: ponto de entrada do programa.
