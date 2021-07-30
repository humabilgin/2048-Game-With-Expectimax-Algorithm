import math
import time
import numpy as np

UP, DOWN, LEFT, RIGHT = range(4)

class Expectimax():

    def get_move(self, board):
        best_move, _ = self.maximize(board)
        return best_move


    #degerlendirme fonksiyonu
    def evaluationFunction(self, board, n_empty): 
        grid = board.grid

        empty_w = 50000  # bos karelerin saglayacagi fayda degeri
        loss_w = 2  # kareler arasindaki farkin verecegi zarar degerinin alıncagi üstel deger
        utility = 0 #fayda
        loss = 0 #zarar

        p_grid = np.sum(np.power(grid, 2)) # grid 4*4luk bir matrix. Hepsinin ikinci kuvveti alınıp toplanıyor.
        s_grid = np.sqrt(grid) # gridin kök alınmış hali
        # kök alınmış matrisin yan yana olan satır ve sütunlarının farklarının mutlak değerleri toplanıyor
        loss  = -np.sum(np.abs(s_grid[::,0] - s_grid[::,1])) -np.sum(np.abs(s_grid[::,1] - s_grid[::,2])) - np.sum(np.abs(s_grid[::,2] - s_grid[::,3]))
        loss  += -np.sum(np.abs(s_grid[0,::] - s_grid[1,::])) -np.sum(np.abs(s_grid[1,::] - s_grid[2,::])) -np.sum(np.abs(s_grid[2,::] - s_grid[3,::]))
        #negatif bir sayı oluşur

        loss_u = loss ** loss_w # kareler arasindaki farkin verecegi toplam zarar degeri
        empty_u = n_empty * empty_w  # bos karelerin verecegi toplam utility degeri 
        p_grid_u = p_grid
        utility += (p_grid + empty_u + loss_u)
        #utility toplami icin bos karelerin faydasi, smoothness degerlerinin verdigi zarar ve matrixin 
        #değerlerinin buyuklugu toplanir.

        return (utility, empty_u, loss_u, p_grid_u)


    # subtreelerden gelen degerlerin en buyugunun secildiği fonksiyon
    def maximize(self, board, depth = 0):
        moves = board.get_available_moves() #yapilabilecek hamleler alinir
        moves_boards = []

        for m in moves:
            m_board = board.clone() # o anki hamle uygulanırsa olusacak boardu olusturacagiz
            m_board.move(m) # move fonksiyonu ile olusturuyoruz
            moves_boards.append((m, m_board)) # tüm hamlelerin boardlarının tutuldugu listeye ekliyoruz

        best_utility = (float('-inf'),0,0,0) # tüm utilityler arasında en iyi olani tutulacak
        best_direction = None

        for mb in moves_boards:
            utility = self.chance(mb[1], depth + 1) # her hamlenin tahtasinin chance degeri hesaplanir

            if utility[0] >= best_utility[0]: # bu degerlerin en buyugu secilir
                best_utility = utility
                best_direction = mb[0]

        return best_direction, best_utility # en iyi hamle donulur


    # bir sonraki elde yapılabilecek hamlelerin optimal olmadigi kabul edilir ve her subtreenin ortalamasi alinir.
    def chance(self, board, depth = 0):
        empty_cells = board.get_available_cells() # bos hucreler listesi
        noOfEmpty = len(empty_cells) # bos hucre sayisi

        #if n_empty >= 7 and depth >= 5:
        #    return self.eval_board(board, n_empty)

        if noOfEmpty >= 6 and depth >= 3:  # bos hucre sayisi 6dan buyukse ve derinlik 3ten buyukse 
            return self.evaluationFunction(board, noOfEmpty) # utility degerlerini dondur
        if 6 > noOfEmpty >= 0 and depth >= 5:  # bos hucre sayisi 6-0 arasindaysa ve derinlik 5ten buyukse
            return self.evaluationFunction(board, noOfEmpty) # utility degerlerini dondur

        # bos hucre sayisi arttıkca derinlik artıyor. Bunun sebebi oyunun zorlasmasıdır. Bir diger sebebi ise 
        # oyun kolayken buyuk bir derinlik vermenin sureyi uzatacak olmasidir. Bu yüzden zorlastikca derinlik artıyor.

        if noOfEmpty == 0:
            _, utility = self.maximize(board, depth + 1)  #yon ignore edilir
            return utility

        possible_tiles = []
        # her el yeni bir sayi tahtaya eklenir
        chanceOf2 = (.95 * (1 / noOfEmpty))  # random olarak 2 gelme olasiligi daha cok
        chanceOf4 = (.05 * (1 / noOfEmpty))  # random olarak 4 gelme olasiligi daha az
        
        for empty_cell in empty_cells:
            possible_tiles.append((empty_cell, 2, chanceOf2))
            possible_tiles.append((empty_cell, 4, chanceOf4))

        totalUtility = [0, 0, 0, 0]

        for t in possible_tiles:
            t_board = board.clone()
            t_board.insert_tile(t[0], t[1])  # 4 ya da 2 eklenir
            _, utility = self.maximize(t_board, depth + 1)

            for i in range(4):
                totalUtility[i] += utility[i] * t[2]

        return tuple(totalUtility)
