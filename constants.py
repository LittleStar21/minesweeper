from enum import Enum

# Colors
COLORS = {
    "background": "#293241",
    "text": "#ffffff",
}
LIGHT_BLUE = "#E0FBFC"

# Screen
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 500

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