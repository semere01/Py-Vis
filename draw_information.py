import math


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 155, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]


    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst, pg):
        self.FONT = pg.font.SysFont('comicsans', 30)
        self.LARGE_FONT = pg.font.SysFont('comicsans', 40)
        self.width = width
        self.height = height
        self.pygame = pg

        self.window = self.pygame.display.set_mode((width, height))
        self.pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
