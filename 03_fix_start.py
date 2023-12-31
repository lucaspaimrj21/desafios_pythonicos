"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""

def fix_start(s):
    # primeiro_caracter = s[0]
    # resto_da_string = s[1:]

    # s = primeiro_caracter + resto_da_string.replace(primeiro_caracter, '*')
    # return s

# ------------------------------------------------------------------------------ #
    # if len(s) <= 1:
    #     return s

    # first_char = s[0]
    # substituted = first_char

    # for char in s[1:]:
    #     if char == first_char:
    #         substituted += '*'
    #     else:
    #         substituted += char

    # return substituted

# ------------------------------------------------------------------------------ #

    if len(s) <= 1:
        return s

    first_char = s[0]
    count = 0
    substituted = ''

    for char in s:
        if char == first_char and count > 0:
            substituted += '*'
        else:
            substituted += char

        count += 1

    return substituted
        
        

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
