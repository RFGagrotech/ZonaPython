#Utiliza la biblioteca pygame (consulta las instrucciones de instalación de pip) para 
#implementar una interfaz gráfica (GUI) que resuelve automáticamente los rompecabezas de 
#Sudoku. 
#Para resolver un rompecabezas de Sudoku, puedes crear un programa que utilice un algoritmo 
#de retroceso (backtracking) que verifica incrementalmente soluciones, adoptando o 
#abandonando la solución actual si no es viable. 
#Este paso de abandonar una solución es la característica definitoria de un enfoque de 
#retroceso, ya que el programa retrocede para probar una nueva solución hasta que encuentra 
#una válida. Este proceso se lleva a cabo de manera incremental hasta que todo el tablero se 
#haya completado correctamente.

import pygame
import time

pygame.init()

WIDTH = 540
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku Solver")
FONT = pygame.font.SysFont("comicsans", 40)

# Ejemplo de tablero Sudoku (0 representa celdas vacías)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def draw_grid(win, board):
    win.fill((255, 255, 255))
    gap = WIDTH // 9
    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(win, (0,0,0), (0, i*gap), (WIDTH, i*gap), thickness)
        pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap, WIDTH), thickness)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = FONT.render(str(board[i][j]), True, (0,0,0))
                win.blit(text, (j*gap + 20, i*gap + 10))

    pygame.display.update()

def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and col != i:
            return False
        if board[i][col] == num and row != i:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(win, board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            draw_grid(win, board)
            pygame.time.delay(50)
            if solve(win, board):
                return True
            board[row][col] = 0
            draw_grid(win, board)
            pygame.time.delay(50)
    return False

def main():
    run = True
    while run:
        draw_grid(WIN, board)
        pygame.time.delay(500)
        solve(WIN, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()
