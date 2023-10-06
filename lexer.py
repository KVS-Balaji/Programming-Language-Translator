from enum import Enum

class Tokens(Enum):
    TOKEN_ERR = 0
    TOKEN_INC = 1
    TOKEN_INT = 2
    TOKEN_CHAR = 3
    TOKEN_FLOAT = 4
    TOKEN_MAIN = 5
    TOKEN_OB = 6
    TOKEN_CB = 7
    TOKEN_OCB = 8
    TOKEN_CCB = 9
    TOKEN_LT = 10
    TOKEN_GT = 11
    TOKEN_SEMICOL = 12
    TOKEN_RET = 13
    TOKEN_NUM = 14
    TOKEN_VAR = 15
    TOKEN_ADD = 16
    TOKEN_SUB = 17
    TOKEN_MUL = 18
    TOKEN_DIV = 19
    TOKEN_ASSIGNMENT = 20
    TOKEN_IF = 21
    TOKEN_ELSE = 22
    TOKEN_ELIF = 23
    TOKEN_LIB = 24
    TOKEN_PRINT = 25
    TOKEN_SCAN = 26
    TOKEN_STRLIT = 27
    TOKEN_SPECIFIER = 28


class TokenType:
    type = 0
    lexeme = None


def getCharToken(index):
    token_type = (Tokens)
    start = index
    token = TokenType()

    char_to_token = {
        '<': token_type(10).name,
        '>': token_type(11).name,
        '(': token_type(6).name,
        ')': token_type(7).name,
        '{': token_type(8).name,
        '}': token_type(9).name,
        ';': token_type(12).name,
        '+': token_type(16).name,
        '-': token_type(17).name,
        '*': token_type(18).name,
        '/': token_type(19).name,
        '=': token_type(20).name
    }

    if text[index] == '#':
        index += 1
        while text[index].isalpha():
            index += 1
        ident = text[start:index]
        if ident == '#include':
            token.type = token_type(1).name
            token.lexeme = ident
            return token, index

    if text[index] in char_to_token:
        token.type = char_to_token[text[index]]
        token.lexeme = text[index]
        return token, index

    if text[index] == '"':
        index += 1
        while text[index] != '"':
            if text[index] == '\\' and (text[index+1] == 'n' or text[index+1] == 't'):
                index += 2
            else:
                index += 1
        ident = text[start:index+1]
        if ident == '"%d"':
            token.type = token_type(28).name
            token.lexeme = ident
        else:
            token.type = token_type(27).name
            token.lexeme = ident
        return token, index+1

    index = start
    while text[index].isalpha():
        index += 1
    ident = text[start:index]
    if text[index] == '.' and text[index+1:index+2] == 'h':
        token.type = token_type(24).name
        token.lexeme = ident + '.' + text[index+1:index+2]
        return token, index + 2
    if ident == 'else' and text[index] == ' ' and text[index+1:index+3] == 'if':
        token.type = token_type(23).name
        token.lexeme = ident + ' ' + text[index+1:index+3]
        return token, index + 3

    if ident in {'int', 'char', 'float', 'main', 'if', 'else', 'printf', 'scanf', 'return'}:
        if ident == 'int':
            token.type = token_type(2).name
            token.lexeme = ident
        elif ident == 'char':
            token.type = token_type(3).name
            token.lexeme = ident
        elif ident == 'float':
            token.type = token_type(4).name
            token.lexeme = ident
        elif ident == 'main':
            token.type = token_type(5).name
            token.lexeme = ident
        elif ident == 'if':
            token.type = token_type(21).name
            token.lexeme = ident
        elif ident == 'else':
            token.type = token_type(22).name
            token.lexeme = ident
        elif ident == 'printf':
            token.type = token_type(25).name
            token.lexeme = ident
        elif ident == 'scanf':
            token.type = token_type(26).name
            token.lexeme = ident
        elif ident == 'return':
            token.type = token_type(13).name
            token.lexeme = ident
        return token, index

    index = start
    if text[index].isdigit():
        index += 1
        while text[index].isdigit():
            index += 1
        ident = text[start:index]
        token.type = token_type(14).name
        token.lexeme = ident
        return token, index

    index = start
    if text[index].isalnum():
        while text[index].isalnum():
            index += 1
        ident = text[start:index]
        token.type = token_type(15).name
        token.lexeme = ident
        return token, index

    token.type = token_type(0).name
    token.lexeme = None
    return token, index

def lex(index):
    tkn, index = getCharToken(index)
    return tkn, index

tok_type = (Tokens)
fptr = open('test.c', 'r')
text = fptr.read()
text_len = len(text)
count = 0
token_list = []
token_tup = ()

i = 0
while i < text_len:
    Token = TokenType()
    Token.type = tok_type(0).name
    Token.lexeme = None
    if text[i] in {'\n', ' '}:
        i += 1
        continue
    Token, ind = lex(i)
    if ind != i:
        i = ind
        token_tup = (Token.type, Token.lexeme)
        token_list.append(token_tup)
        continue
    i += 1
    token_tup = (Token.type, Token.lexeme)
    token_list.append(token_tup)

print(token_list)