class Rect():
    '''
    A class to define postions and dimensions

    Attributes
    ----------
    x: int
        The x position of the rect
    y: int
        The y position of the rect
    w, width: int
        The width of the rect
    h, height: int
        The height of the rect
    '''

    x: int
    y: int
    w, width: int
    h, height: int
    
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = self.width = w
        self.h = self.height = h