class Tools:
    def __init__(self, lista):
        self.lista = lista

    def Verificar_Primo(self):
        for L in self.lista:
            if (self.__Verificar_Primo(L)):
                print(f'El número {L} SÍ es primo.')
            else:
                print(f'El número {L} NO es primo.')

    def Conversion_grados(self, medida_origen, medida_destino):
        for L in self.lista:
            ans = self.__Conversion_grados(L, medida_origen, medida_destino)

    def Factorial(self):
        for L in self.lista:
            ans = self.__Factorial(L)
            print(f'El factorial de {L} es {ans}')

    def __Verificar_Primo(self, n_max):
        if n_max > 1:
            # Creamos la lista completa
            lista = [i for i in range(2, n_max + 1)]
            pn = 0
            while pn < n_max:
                # obtenemos el primer valor de la lista (siempre primo)
                pn = lista[0]
                # Evaluamos si el valor dado es primo
                if pn == n_max:
                    return True
                # Cribamos para el primer valor de la lista anterior
                criba = []
                for lis in lista:
                    if lis % pn != 0:
                        criba.append(lis)
                lista = criba
                # si llegamos al punto de lista vacia se termina el proceso
                if lista == []:
                    return False
                    break

    def Valor_modal(self, op):
        repetidos = []
        for lis in self.lista:
            repetidos.append(self.lista.count(lis))
        if op == 0:
            idx_min = repetidos.index(min(repetidos))
            idx_min
            print(f'El numero que menos se repite es {self.lista[idx_min]} y se repite {repetidos[idx_min]} veces')
            return (self.lista[idx_min], repetidos[idx_min])
        elif op == 1:
            idx_max = repetidos.index(max(repetidos))
            idx_max
            print(f'El numero que más se repite es {self.lista[idx_max]} y se repite {repetidos[idx_max]} veces')
            return (self.lista[idx_max], repetidos[idx_max])

    def __Conversion_grados(self, val, medida_origen, medida_destino):
        # Para grados Celsius
        if medida_origen == 'C':
            if medida_destino == 'C':
                ans = val
                print(f'{val}°C son {round(val, 2)}°C')
            if medida_destino == 'F':
                ans = (9 * val / 5) + 32
                print(f'{val}°C son {round(ans, 2)}°F')
            if medida_destino == 'K':
                ans = 273.15 + val
                print(f'{val}°C son {round(ans, 2)}°K')

        # Para grados Farenheit
        if medida_origen == 'F':
            if medida_destino == 'F':
                ans = val
                print(f'{val}°F son {round(val, 2)}°F')
            if medida_destino == 'C':
                ans = (5 / 9) * (val - 32)
                print(f'{val}°F son {round(ans, 2)}°C')
            if medida_destino == 'K':
                ans0 = (5 / 9) * (val - 32)
                ans = 273.15 + ans0
                print(f'{val}°F son {round(ans, 2)}°K')

        # Para grados Kelvin
        if medida_origen == 'K':
            if medida_destino == 'K':
                ans = val
                print(f'{val}°K son {round(val, 2)}°K')
            if medida_destino == 'C':
                ans = val - 273.15
                print(f'{val}°K son {round(ans, 2)}°C')
            if medida_destino == 'F':
                ans0 = val - 273.15
                ans = (9 * ans0 / 5) + 32
                print(f'{val}°K son {round(ans, 2)}°F')
        return round(ans, 2)

    def __Factorial(self, n):
        if type(n) == float:
            print('Error, el numero ingresado no es entero')
            return None
        elif n < 0:
            print('Error, el numero ingresado es negativo')
            return None
        else:
            x = 1
            for i in range(1, n + 1):
                x *= i
            return x
