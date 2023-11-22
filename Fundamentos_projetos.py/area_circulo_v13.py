#! python
from math import pi
import sys

def help(): 
    print ("É necessario informar o o raio do circulo.")
    print ("Sintaxe: {} <raio>" .format(sys.argv[0] [2:]))     


def circulo(raio):
    return pi * float(raio) ** 2


if __name__=="__main__":
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print ("Area do circulo", area)

 