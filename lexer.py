# lexer.py
import re

# --- Definir Tokens ---
TOKENS = {
   'ASSIGN': r'=',
    'COLON': r':',
    'COMMA': r',',
    'SEMICOLON': r';',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'PLUS': r'\+',
    'MINUS': r'-',
    'TIMES': r'\*',
    'DIVIDE': r'/',
    'PRINT': r'print',
    'COLOR': r'color',
    'TYPE': r'type',
    'WEAR': r'wear',
    'DISTANCE': r'distance',
    'MAINTENANCE': r'maintenance',
    'OWNER': r'owner',
    'INVENTORY': r'inventory',
    'LIST_INVENTORY': r'list_inventory',  # Nuevo token para listar el inventario
    'ID': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'NUMBER': r'\d+',
    'STRING': r'\".*?\"',
    'COMMENT': r'//.*',
}

def tokenize(code):
    tokens = []
    code = code.strip()
    
    while code:
        matched = False
        
        for token_name, token_regex in TOKENS.items():
            match = re.match(token_regex, code)
            if match:
                token_value = match.group(0)
                if token_name != 'COMMENT':
                    tokens.append((token_name, token_value))
                code = code[len(token_value):].strip()
                matched = True
                break

        if not matched:
            raise ValueError(f"Error léxico en: {code}")
    
    return tokens

