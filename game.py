import pygame
import os
import random
import time
from constants import TILE_MINE, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, LIGHT_BLUE

class Minesweeper:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.is_mouse_down = False

        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Minesweeper")
        
        self.load_assets()
        self.reset()

    def load_assets(self):
        roboto_font = os.path.join("assets", "Roboto")
        self.roboto_24_bold = pygame.font.Font(os.path.join(roboto_font, "Roboto-Bold.ttf"), 24)
        self.roboto_16_regular = pygame.font.Font(os.path.join(roboto_font, "Roboto-Black.ttf"), 16)

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_mouse_down = True
                    print("Mouse down:", pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.is_mouse_down = False
                    print("Mouse up:", pygame.mouse.get_pos())

            self.draw()
            pygame.display.update()

    def draw(self):
        win_width, win_height = pygame.display.get_surface().get_size()

        # Background color
        self.window.fill(COLORS["background"])

        # Title text
        title_text = self.roboto_24_bold.render("Minesweeper", True, COLORS["text"])
        self.window.blit(title_text, title_text.get_rect(center=(win_width / 2, 25)))

        # Game board
        board_size = max(0.85 * win_height, 425)
        pygame.draw.rect(self.window, LIGHT_BLUE, pygame.Rect(24, 50, board_size, board_size))

        # Game tiles

        # Difficulty
        difficulty_text = self.roboto_16_regular.render("Difficulty: Hard", True, COLORS["text"])
        difficulty_left = 24 + board_size
        difficulty_right = win_width - 24
        self.window.blit(difficulty_text, difficulty_text.get_rect(center=(difficulty_left + (difficulty_right - difficulty_left) / 2, 60)))

        # Reset button

    def reset(self):
        self.tile = 24
        self.total_mines = 99
        self.board = [[0 for i in range(self.tile)] for j in range(self.tile)]

        # Randomize mines
        current_mine = 0
        while current_mine < self.total_mines:
            rand_num = random.randint(0, self.tile * self.tile - 1)
            rand_x, rand_y = rand_num // 24, rand_num % 24
            if self.board[rand_x][rand_y] == 0:
                self.board[rand_x][rand_y] = TILE_MINE
                current_mine += 1

        # Calculate neighbor mines
        delta_x = [-1, 0, 1, 1, 1, 0, -1, -1]
        delta_y = [-1, -1, -1, 0, 1, 1, 1, 0]
        for i in range(self.tile):
            for j in range(self.tile):
                if self.board[i][j] == TILE_MINE:
                    for dx, dy in zip(delta_x, delta_y):
                        neighbor_x = i + dx
                        neighbor_y = j + dy
                        if self.is_valid_idx(neighbor_x, neighbor_y) and self.board[neighbor_x][neighbor_y] != TILE_MINE:
                            self.board[neighbor_x][neighbor_y] += 1
        
        self.print_board()

    def is_valid_idx(self, x, y):
        return x >= 0 and y >= 0 and x < self.tile and y < self.tile

    def mouse_pos(self, mouse_x, mouse_y):
        board_left = 24
        board_top = 50
        

    def print_board(self):
        for i in range(self.tile):
            for j in range(self.tile):
                if self.board[i][j] == TILE_MINE:
                    print("x", end=" | ")
                else:
                    print(self.board[i][j], end=" | ")
            print()

if __name__ == "__main__":
    game = Minesweeper()
    game.play()