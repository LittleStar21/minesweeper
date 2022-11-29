import pygame
import os
import random
from constants import TILE_MINE, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, LIGHT_BLUE, BOARD_WIDTH

class Minesweeper:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.is_mouse_down = False

        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minesweeper")
        
        self.load_assets()
        self.reset()

    def load_assets(self):
        roboto_font = os.path.join("assets", "Roboto")
        self.roboto_12_regular = pygame.font.Font(os.path.join(roboto_font, "Roboto-Black.ttf"), 12)
        self.roboto_24_bold = pygame.font.Font(os.path.join(roboto_font, "Roboto-Bold.ttf"), 24)
        self.roboto_16_regular = pygame.font.Font(os.path.join(roboto_font, "Roboto-Black.ttf"), 16)

    def play(self):
        running = True
        self.reset()
        mouse_down_location = None
        mouse_up_location = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_mouse_down = True
                    mouse_down_location = self.handle_mouse_loc()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.is_mouse_down = False
                    mouse_up_location = self.handle_mouse_loc()
            
            if mouse_up_location is not None and mouse_down_location == mouse_up_location:
                if mouse_down_location == "reset":
                    self.reset()
                elif mouse_down_location == "board":
                    print("board clicked")
                mouse_up_location = None

            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    def draw(self):
        win_width, win_height = pygame.display.get_surface().get_size()

        # Background color
        self.window.fill(COLORS["background"])

        # Title text
        title_text = self.roboto_24_bold.render("Minesweeper", True, COLORS["text"])
        self.window.blit(title_text, title_text.get_rect(center=(win_width / 2, 25)))

        # Game board background
        pygame.draw.rect(self.window, LIGHT_BLUE, pygame.Rect(24, 50, BOARD_WIDTH, BOARD_WIDTH))

        # Game tiles
        tile_gap = 2
        tile_size = (BOARD_WIDTH - ((self.tile + 1) * tile_gap)) / self.tile
        for i in range(self.tile):
            for j in range(self.tile):
                if self.board[i][j] != -1:
                    pygame.draw.rect(self.window, COLORS["tile"], pygame.Rect(
                        24 + (i + 1) * tile_gap + i * tile_size,
                        50 + (j + 1) * tile_gap + j * tile_size,
                        tile_size,
                        tile_size
                    ))

                    tile_text = self.roboto_12_regular.render(str(self.board[i][j]), True, (255, 255, 255))
                    self.window.blit(tile_text, tile_text.get_rect(center=(
                        24 + (i + 1) * tile_gap + i * tile_size + 0.5 * tile_size,
                        50 + (j + 1) * tile_gap + j * tile_size + 0.5 * tile_size
                    )))
                else:
                    pygame.draw.rect(self.window, COLORS["reset_background"], pygame.Rect(
                        24 + (i + 1) * tile_gap + i * tile_size,
                        50 + (j + 1) * tile_gap + j * tile_size,
                        tile_size,
                        tile_size
                    ))


        # Difficulty
        difficulty_text = self.roboto_16_regular.render("Difficulty: Hard", True, COLORS["text"])
        difficulty_left = 24 + BOARD_WIDTH
        difficulty_right = win_width
        difficulty_center = max(550, difficulty_left + (difficulty_right - difficulty_left) / 2)
        self.window.blit(difficulty_text, difficulty_text.get_rect(center=(difficulty_center, 60)))

        # Reset button
        reset_text = self.roboto_16_regular.render("Reset", True, COLORS["reset_text"])
        reset_background = pygame.Rect(0, 0, 120, 40)
        reset_background.center = (difficulty_center, 475 - 20)
        pygame.draw.rect(self.window, COLORS["reset_background"], reset_background)
        self.window.blit(reset_text, reset_text.get_rect(center=(difficulty_center, 475 - 20)))

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

    def handle_mouse_loc(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 23 and mouse_x <= 450 and mouse_y >= 50 and mouse_y <= 475:
            return "board"
        elif mouse_x >= 489.5 and mouse_x <= 639.5 and mouse_y >= 435 and mouse_y <= 475:
            return "reset"
        return None

    def get_pos_from_mouse(self, mouse_x, mouse_y):
        pass

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