from render.entity.apperance import Apperance
from entity.rect import Rect


class Entity():
    '''
    The base class for all entity types.

    Attributes
    ----------
    _apperance: Apperance
        The apperance of the entity
    rect: Rect
        The position and dimension of the entity

    Methods
    -------
    set_apperance:
        sets the apperance of the entity
    '''

    _apperance: Apperance
    rect: Rect

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self._apperance = Apperance()
        self.rect = Rect(x, y, w, h)

    def set_apperance(self, apperance: Apperance) -> None:
        '''
        Sets the apperance of the entity
        '''

        self._apperance = apperance
