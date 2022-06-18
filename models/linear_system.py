from dataclasses import dataclass
from typing import Set, List
from models.linear_equation import LinearEquation


@dataclass
class LinearSystem():
    _matriz_coeficientes: List[List[int]]
    _matriz_variaveis: Set[str] 
    _termos_independentes: List[int]
    _normal: bool


    def __init__(self, linear_equations: List[LinearEquation]) -> None:
        self._matriz_coeficientes = []
        self._matriz_variaveis = set()
        self._termos_independentes = []
        for linear_equation in linear_equations:
            self._matriz_coeficientes.append(linear_equation.values)
            self._matriz_variaveis.update(linear_equation.symbols)
            self._termos_independentes.append(linear_equation.result)

        self._normal = len(linear_equations) == len(self._matriz_variaveis)

    def print_matrix(self):
        print(self._matriz_coeficientes)
        print(self._matriz_variaveis)
        print(self._termos_independentes)
        print(self._normal)


    @property
    def matriz_coeficientes(self) -> List[List[int]]:
        return self._matriz_coeficientes

    @property
    def matriz_variaveis(self) -> Set[str]:
        return self._matriz_variaveis
    
    @property
    def termos_independentes(self) -> List[int]:
        return self._termos_independentes
    
    @property
    def normal(self) -> bool:
        return self._normal
