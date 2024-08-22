# parser.py
from bicycle import Bicycle

# Diccionario para almacenar bicicletas
bicycles = {}

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.advance()

    def advance(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def parse(self):
        while self.current_token:
            self.statement()

    def statement(self):
        if self.current_token[0] == 'ID':
            self.assignment()
        elif self.current_token[0] == 'PRINT':
            self.print_statement()
        elif self.current_token[0] == 'DISTANCE':
            self.calculate_distance()
        elif self.current_token[0] == 'MAINTENANCE':
            self.calculate_maintenance()
        elif self.current_token[0] == 'INVENTORY':
            self.check_inventory()
        elif self.current_token[0] == 'LIST_INVENTORY':  # Manejar listado de inventario
            self.list_inventory()
        elif self.current_token[0] == 'OWNER':
            self.assign_owner()
        else:
            raise ValueError(f"Error de sintaxis: token inesperado {self.current_token}")

    def assignment(self):
        name = self.current_token[1]
        self.advance()  # ID
        self.match('ASSIGN')
        bicycle = self.bicycle()
        bicycles[name] = bicycle
        self.match('SEMICOLON')
        print(f"Bicicleta '{name}' añadida al inventario.")

    def bicycle(self):
        self.match('COLOR')
        self.match('COLON')
        color = self.current_token[1].strip('"')
        self.advance()

        self.match('COMMA')

        self.match('TYPE')
        self.match('COLON')
        type = self.current_token[1].strip('"')
        self.advance()

        self.match('COMMA')

        self.match('WEAR')
        self.match('COLON')
        wear = int(self.current_token[1])
        self.advance()

        return Bicycle(color, type, wear)

    def print_statement(self):
        self.advance()  # PRINT
        self.match('LBRACE')
        name = self.current_token[1]
        self.advance()
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if name in bicycles:
            bicycle = bicycles[name]
            print(f"Bicicleta {name}: {bicycle}")
        else:
            print(f"Error: Bicicleta '{name}' no encontrada.")

    def calculate_distance(self):
        self.advance()  # DISTANCE
        self.match('LBRACE')
        name = self.current_token[1]
        self.advance()
        self.match('COMMA')
        distance = self.expression()
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if name in bicycles:
            bicycle = bicycles[name]
            wear = bicycle.calculate_wear(distance)
            print(f"Desgaste calculado para {name} tras {distance} km: {wear}%")
        else:
            print(f"Error: Bicicleta '{name}' no encontrada.")

    def calculate_maintenance(self):
        self.advance()  # MAINTENANCE
        self.match('LBRACE')
        name = self.current_token[1]
        self.advance()
        self.match('COMMA')
        distance = self.expression()
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if name in bicycles:
            bicycle = bicycles[name]
            next_maintenance = bicycle.calculate_next_maintenance(distance)
            print(f"Siguiente mantenimiento para {name}: {next_maintenance} km")
        else:
            print(f"Error: Bicicleta '{name}' no encontrada.")

    def check_inventory(self):
        self.advance()  # INVENTORY
        self.match('LBRACE')
        name = self.current_token[1]
        self.advance()
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if name in bicycles:
            bicycle = bicycles[name]
            print(f"Bicicleta en inventario: {bicycle}")
        else:
            print(f"Error: Bicicleta '{name}' no encontrada.")

    def list_inventory(self):  # Nuevo método para listar todo el inventario
        self.advance()  # LIST_INVENTORY
        self.match('LBRACE')
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if bicycles:
            print("Inventario de bicicletas:")
            for name, bicycle in bicycles.items():
                print(f"Bicicleta {name}: {bicycle}")
        else:
            print("El inventario está vacío.")

    def assign_owner(self):
        self.advance()  # OWNER
        self.match('LBRACE')
        name = self.current_token[1]
        self.advance()
        self.match('COMMA')
        owner = self.current_token[1].strip('"')
        self.advance()
        self.match('RBRACE')
        self.match('SEMICOLON')
        
        if name in bicycles:
            bicycles[name].owner = owner
            print(f"Propietario para {name} asignado: {owner}")
        else:
            print(f"Error: Bicicleta '{name}' no encontrada.")

    def expression(self):
        left = self.term()

        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            operator = self.current_token[0]
            self.advance()
            right = self.term()
            if operator == 'PLUS':
                left += right
            elif operator == 'MINUS':
                left -= right
        
        return left

    def term(self):
        left = self.factor()

        while self.current_token and self.current_token[0] in ('TIMES', 'DIVIDE'):
            operator = self.current_token[0]
            self.advance()
            right = self.factor()
            if operator == 'TIMES':
                left *= right
            elif operator == 'DIVIDE':
                left /= right
        
        return left

    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.advance()
            return int(token[1])
        elif token[0] == 'LPAREN':
            self.advance()
            result = self.expression()
            self.match('RPAREN')
            return result
        elif token[0] == 'ID':
            if token[1] in bicycles:
                self.advance()
                return bicycles[token[1]].wear
            else:
                raise ValueError(f"Error: Bicicleta '{token[1]}' no encontrada.")
        else:
            raise ValueError(f"Error de sintaxis: token inesperado {token}")

    def match(self, token_type):
        if self.current_token and self.current_token[0] == token_type:
            self.advance()
        else:
            raise ValueError(f"Error de sintaxis: se esperaba {token_type}, pero se encontró {self.current_token}")


