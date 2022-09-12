import pygame, sys, random
from tkinter import messagebox, Tk

# definir tamaño de la ventana
tam = (ancho, altura) = 600, 600

pygame.init()

ventana = pygame.display.set_mode(tam)

cols, filas = 50, 50


matriz = []
openSet, closeSet = [], []
camino = []

an = ancho//cols
al = altura//filas

class Lugar:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.vecinos = []
        self.anterior = None

        # determinar si una coordenada es un pared o no, generando el mapa de forma aleatoria
        self.pared = False
        if random.randint(0, 100) < 30:
            self.pared = True
        
    # funcion para colorear parte del mapa
    def mostrar(self, ventana, color):
        if self.pared == True:
            color = (0, 0, 0)
        pygame.draw.rect(ventana, color, (self.x*an, self.y*al, an-1, al-1))
    
    # funcion para agregar los veciones de cada coordenada, de manera adyacente
    def agregar_vecinos(self, matriz):
        if self.x < cols - 1:
            self.vecinos.append(matriz[self.x+1][self.y])
        if self.x > 0:
            self.vecinos.append(matriz[self.x-1][self.y])
        if self.y < filas - 1:
            self.vecinos.append(matriz[self.x][self.y+1])
        if self.y > 0:
            self.vecinos.append(matriz[self.x][self.y-1])
            
def f_heuristica(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y))

# creamos un matriz de adyacencia para simular el mapa y asi saber las coordenadas, lo cuales contendra la informacion del lugar.
for i in range(cols):
    arr = []
    for j in range(filas):
        arr.append(Lugar(i, j))
    matriz.append(arr)

# agregamos los vecinos a cada coordenada o lugar
for i in range(cols):
    for j in range(filas):
        matriz[i][j].agregar_vecinos(matriz)

# generamos de forma aleatoria la posicion del punto de inicio
while True:
    inicio = matriz[random.randint(0, filas)][random.randint(0, cols)]
    if inicio.pared == False:
        break

# generamos de forma aleatoria la posicion del punto objetivo
while True:
    final = matriz[random.randint(0, filas)][random.randint(0, cols)]
    if (final.pared == False) and (inicio != final):
        break

openSet.append(inicio)

def main():
    flag = False
    noflag = True
    startflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True

        if startflag:
            if len(openSet) > 0:
                winner = 0
                for i in range(len(openSet)):
                    if openSet[i].f < openSet[winner].f:
                        winner = i

                current = openSet[winner]
                
                if current == final:
                    temp = current
                    while temp.anterior:
                        camino.append(temp.anterior)
                        temp = temp.anterior 
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue

                if flag == False:
                    openSet.remove(current)
                    closeSet.append(current)

                    for neighbor in current.vecinos:
                        if neighbor in closeSet or neighbor.pared:
                            continue
                        tempG = current.g + 1

                        newPath = False
                        if neighbor in openSet:
                            if tempG < neighbor.g:
                                neighbor.g = tempG
                                newPath = True
                        else:
                            neighbor.g = tempG
                            newPath = True
                            openSet.append(neighbor)
                        
                        if newPath:
                            neighbor.h = f_heuristica(neighbor, final)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.anterior = current

            else:
                if noflag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    noflag = False

        ventana.fill((0, 20, 20))
        for i in range(cols):
            for j in range(filas):
                spot = matriz[j][i]
                spot.mostrar(ventana, (255, 255, 255))
                if flag and spot in camino:
                    spot.mostrar(ventana, (25, 120, 250))
                elif spot in closeSet:
                    spot.mostrar(ventana, (255, 0, 0))
                elif spot in openSet:
                    spot.mostrar(ventana, (0, 255, 0))
                try:
                    if spot == final:
                        spot.mostrar(ventana, (0, 120, 255))
                except Exception:
                    pass
                
        pygame.display.flip()

main()
