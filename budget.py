# -*- coding: utf-8 -*-

class Category:
    
    def __init__(self, name):
        # Nombre de la categoria
        self.name = name
        # Variable saldo (lista)
        self.ledger = list()
    
    # Depositar dinero
    def deposit(self, amount, description = ""):
        # crea el diccionario
        self.dep = dict()
        # cantidad y descripción 
        self.dep["amount"] = amount
        self.dep["description"] = description
        # Añadir el depósito al saldo contable
        self.ledger.append(self.dep) 
    
    # Saldo total
    def get_balance(self):
        total=0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    # Te verifica si el saldo es menor o igual a una cantidad dada
    def check_funds(self, amount):
        if self.get_balance() < amount:
            resultado = False
        else:
            resultado = True
        return resultado
    
    # Sacar dinero
    def withdraw(self, amount, description = ""):
        # Si el saldo total es mayor que la cantidad
        if self.check_funds(amount):
            # Haz un deposito negativo
            self.deposit(-amount,description)
            # Se ha sacado dinero
            return True
        else:
            # No se ha sacado dinero
            return False
    
    # Transfiere dinero de una categoría a otra
    def transfer(self, amount, another_budget):
        # Saca dinero de la categoria actual
        var = self.withdraw(amount, "Transfer to " + str(another_budget.name))
        # Si se ha podido sacar la cantidad de dinero
        if var:
            # Deposita esta cantidad de dinero en la categoria another_budget
            another_budget.deposit(amount, "Transfer from " + str(self.name))
        # Si se ha podido realizar el proceso devuelve True, de lo contrario False
            return True
        else:
            return False
    
    # Imprime la cosas
    def __str__(self):
        longitud = len(self.name)
        aux = 30 - longitud
        lado = aux // 2
        title = '*'*lado + self.name + '*'*lado
        if len(title) != 30:
            title += '*'
        title += '\n'
        space = ' '
        items = ''
        total = 0
        for i in range(len(self.ledger)):
            descripcion = self.ledger[i]['description'][0:23]
            medida = 23 - len(descripcion)
            cantidad = f'{self.ledger[i]["amount"]:>7.2f}'
            items += descripcion + space*medida + cantidad + '\n'
            total += self.ledger[i]['amount']
        resultado = title + items + "Total: " + str(total)
        return resultado


#------------------------------------------------------------------------

# Cantidad de dinero sacado de una categoría
def total_withdraws(category):
    total = 0
    for item in category.ledger:
        if item["amount"] < 0:
            total += item["amount"]
    return total
            
# Porcentaje de dinero sacado de cada categoría en porcentaje respecto
# al total.
def percentages(categories):
    total = 0
    for category in categories:
        quantity = total_withdraws(category)
        total += quantity
    porcentajes = []
    for category in categories:
        porcen = (total_withdraws(category)/total)
        porcen = (int(porcen * 10) / 10)*100
        porcentajes.append(porcen)
    return porcentajes

#------------------------------------------------------------------------

def create_spend_chart(categories):
    vector_1 = [str(i*10) + '| ' for i in range(11)]
    for idx, entry in enumerate(vector_1):
        while len(entry) < 5:
            entry = ' ' + entry
            vector_1[idx] = entry
    vector_1 = reversed(vector_1)
    porcentajes = percentages(categories)
    
    vector = []
    for i in porcentajes:
        numero = int(i / 10 + 1)
        aux = ' '*(11-numero) + 'o'*numero
        vector.append(aux)
    
    lista = []
    for category in categories:
        lista.append(category.name)
    
    lista_lon = []
    for i in lista:
        lista_lon.append(len(i))
        
    numeraco = max(lista_lon)
    
    nombres = []
    for i in lista:
        aux = i + ' '*(numeraco-len(i))
        nombres.append(aux)
        
    resultado = 'Percentage spent by category\n'
    for idx, entry in enumerate(vector_1):
        resultado += entry
        for i in vector:
            resultado += i[idx] + '  '
        resultado += '\n'
    resultado += '    ----------\n'
    for i in range(numeraco):
        resultado += ' '*5
        for j in nombres:
            resultado += j[i] + '  '
        if i != numeraco-1:
            resultado += '\n'
        
    return resultado


    
