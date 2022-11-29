from enum import Enum

# Mouse Location
class MouseLoc(Enum):
    RESET: 0
    BOARD: 1

# Colors
COLORS = {
    "background": "#293241",
    "text": "#ffffff",
    "reset_background": "#ee6c4d",
    "reset_text": "#e0fbfc",
    "tile": "#3d5a80"
}
LIGHT_BLUE = "#E0FBFC"

# Screen
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 570

# Board
BOARD_WIDTH = 500

# Difficulties
DIFFICULTIES = {
    "easy": {
        "width": 9,
        "height": 9,
        "mines": 10
    },
    "medium": {
        "width": 16,
        "height": 16,
        "mines": 40
    },
    "hard": {
        "width": 24,
        "height": 24,
        "mines": 99
    }
}

TILE_MINE = -1
TILE_WIDTH = 20 # Minim