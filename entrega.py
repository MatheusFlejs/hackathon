import sqlite3
from enum import Enum

class StatusPedido(Enum):
    PEDIDO_FEITO = 1
    PEDIDO_ENCAMINHADO = 2
    ENTREGUE = 3

class SistemaPedidos:
    def __init__(self, db_name='pedidos.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY,
            produto TEXT,
            status INTEGER
        )
        ''')
        self.conn.commit()

    def adicionar_pedido(self, produto):
        self.cursor.execute('INSERT INTO pedidos (produto, status) VALUES (?, ?)',
                            (produto, StatusPedido.PEDIDO_FEITO.value))
        self.conn.commit()
        return self.cursor.lastrowid

    def atualizar_status(self, pedido_id, novo_status):
        self.cursor.execute('UPDATE pedidos SET status = ? WHERE id = ?',
                            (novo_status.value, pedido_id))
        self.conn.commit()

    def obter_status(self, pedido_id):
        self.cursor.execute('SELECT status FROM pedidos WHERE id = ?', (pedido_id,))
        resultado = self.cursor.fetchone()
        if resultado:
            return StatusPedido(resultado[0])
        return None

    def listar_pedidos(self):
        self.cursor.execute('SELECT * FROM pedidos')
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()

# Exemplo de uso
if __name__ == "__main__":
    sistema = SistemaPedidos()

    # Adicionar pedidos
    pedido1 = sistema.adicionar_pedido("Smartphone")
    pedido2 = sistema.adicionar_pedido("Notebook")

    print(f"Pedido 1 criado com ID: {pedido1}")
    print(f"Pedido 2 criado com ID: {pedido2}")

    # Atualizar status
    sistema.atualizar_status(pedido1, StatusPedido.PEDIDO_ENCAMINHADO)
    sistema.atualizar_status(pedido2, StatusPedido.ENTREGUE)

    # Obter status
    print(f"Status do Pedido 1: {sistema.obter_status(pedido1)}")
    