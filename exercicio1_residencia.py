"""
Exercício 1 - Residência e Cômodos (relação de COMPOSIÇÃO).

Os objetos Comodo são criados exclusivamente dentro de Residencia e
nunca são entregues para fora da classe.
"""


class Comodo:
    """Representa um cômodo com nome e área (em metros quadrados)."""

    def __init__(self, nome, area):
        # Atributos privados (encapsulamento)
        self.__nome = nome
        self.__area = area

    def get_nome(self):
        """Retorna o nome do cômodo."""
        return self.__nome

    def get_area(self):
        """Retorna a área do cômodo em m²."""
        return self.__area


class Residencia:
    """Residência composta por vários cômodos."""

    def __init__(self):
        # Lista privada: ninguém fora da classe acessa os cômodos diretamente
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        """Cria um Comodo dentro da residência (composição)."""
        self.__comodos.append(Comodo(nome, area))

    def listar_comodos(self):
        """Retorna os cômodos como texto, sem expor os objetos Comodo."""
        return [f"{c.get_nome()} - {c.get_area():.2f} m²" for c in self.__comodos]

    def calcular_area_total(self):
        """Soma a área de todos os cômodos."""
        return sum(c.get_area() for c in self.__comodos)


def main():
    """Menu interativo no console."""
    residencia = None  # só existe depois que o usuário criar (opção 1)

    while True:
        print("\n=== MENU RESIDÊNCIA ===")
        print("1 - Criar residência")
        print("2 - Adicionar cômodo")
        print("3 - Visualizar cômodos")
        print("4 - Calcular área total")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            residencia = Residencia()
            print("Residência criada!")

        # Opções 2, 3 e 4 exigem que a residência já exista
        elif opcao in ("2", "3", "4") and residencia is None:
            print("Crie uma residência primeiro (opção 1).")

        elif opcao == "2":
            nome = input("Nome do cômodo: ")
            try:
                area = float(input("Área (m²): "))
            except ValueError:
                print("Área inválida.")
                continue
            if area <= 0:
                print("A área deve ser maior que zero.")
                continue
            residencia.adicionar_comodo(nome, area)
            print("Cômodo adicionado!")

        elif opcao == "3":
            comodos = residencia.listar_comodos()
            if not comodos:
                print("Nenhum cômodo cadastrado.")
            for comodo in comodos:
                print("-", comodo)

        elif opcao == "4":
            print(f"Área total: {residencia.calcular_area_total():.2f} m²")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
