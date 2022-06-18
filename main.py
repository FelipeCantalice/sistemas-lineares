


from models.linear_equation import LinearEquation
from models.linear_system import LinearSystem


equacao1_str: str = '-2x + 3y - w = 5'
equacao2_str: str = 'x -3y = 0'

equacao1: LinearEquation = LinearEquation.Builder(equacao1_str)


equacao2: LinearEquation = LinearEquation.Builder(equacao1_str)

linear_system = LinearSystem([equacao1, equacao2])