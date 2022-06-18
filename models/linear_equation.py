from dataclasses import dataclass
from typing import List

SIMBOLOS = ['+', '-']

@dataclass
class LinearEquation():
    values: List[int]
    symbols: List[str]
    result: int

    @staticmethod
    def fromString(equation:str):
        return convert_str_to_linearequation(equation)



def convert_str_to_linearequation(equacao: str) -> LinearEquation:
    """
    Converte uma equação em uma lista de dicionários.
    """
    # remove espaços em branco
    equacao_temp = equacao.replace(' ', '')
    # divide a string em um vetor
    equacao_temp_arr = equacao_temp.split('=')
    
    # divisão
    equation_after_equals = equacao_temp_arr[0]
    equation_before_equals = equacao_temp_arr[1]

    if str.isalpha(equation_after_equals[0]):
        equation_after_equals = '+' + equation_after_equals
    
    valores: list[int] = []
    variaveis: list[str] = []
    
    # separa os valores e as variáveis
    temp: str = ''

    for v in equation_after_equals:

        if str.isalpha(v) and not SIMBOLOS.__contains__(v):

            if len(temp) == 1:
                if temp.__contains__('1'):
                    valores.append(int(f'{temp}'))
                else:
                    valores.append(int(f'{temp}1'))


                variaveis.append(v)
                temp = ''
                continue
            else:
                valores.append(int(temp))
                variaveis.append(v)
                temp = ''
                continue
        temp += v
        
    return LinearEquation(valores, variaveis, equation_before_equals)
