# -*- coding: utf-8 -*-

# Classe que representa a tabela de segundo nível
class SecondLevelHashTable:
    def __init__(self, size):
        self.size = size
        self.T = [[] for _ in range(self.size)]  # Inicializa listas vazias

    # Função de hash para determinar a posição de inserção na lista
    def __hash(self, key_str):
        num = 0
        for c in key_str:
            num += ord(c)
        return num % self.size

    # Insere um valor na lista correspondente à chave
    def insert(self, key, value):
        pos = self.__hash(key)
        self.T[pos].append(value)

    # Recupera um valor com base na chave
    def get(self, key):
        pos = self.__hash(key)
        L = self.T[pos]
        for value in L:
            if value.matricula == key:
                return value
        return None

    # Imprime as listas do segundo nível
    def print(self):
        for i, lista in enumerate(self.T):
            print(f"Lista {i}:")
            for value in lista:
                print(value.to_string())
            print()

# Classe que representa a tabela hash principal
class HashTable:
    def __init__(self, s):
        self.size = s  # Tamanho da tabela principal
        self.T = [SecondLevelHashTable(s // 10) for _ in range(10)]  # Inicializa tabelas de segundo nível

    # Função de hash para determinar a posição na tabela principal
    def __hash(self, key_str, level):
        key = self.__hash_str(key_str)
        return key % self.size if level == 1 else key % (self.size // 10)

    # Função de hash para chaves como strings
    def __hash_str(self, key_str):
        num = 0
        for c in key_str:
            num += ord(c)
        return num

    # Insere um valor na tabela hash
    def insert(self, key, value):
        pos = self.__hash(key, 1)
        self.T[pos].insert(key, value)

    # Recupera um valor com base na chave
    def get(self, key):
        pos = self.__hash(key, 1)
        return self.T[pos].get(key)

    # Imprime a tabela hash principal e as listas do segundo nível
    def print(self):
        print("{")
        for i in range(10):
            print(f"Tabela {i}:")
            self.T[i].print()
        print("}")
