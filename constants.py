__all__ = [
    'ORDER_SEARCH_POSSIBILITIES',
    'HEURISTICS_IDS',
    'MOVE_RIGHT',
    'MOVE_DOWN',
    'MOVE_LEFT',
    'MOVE_UP'
]

ORDER_SEARCH_POSSIBILITIES = [
    'LRUD',
    'LRDU',
    'LURD',
    'LUDR',
    'LDUR',
    'LDRU',
    'URLD',
    'URDL',
    'UDRL',
    'UDLR',
    'ULRD',
    'ULDR',
    'RULD',
    'RUDL',
    'RLUD',
    'RLDU',
    'RDUL',
    'RDLU',
    'DURL',
    'DULR',
    'DLUR',
    'DLRU',
    'DRLU',
    'DRUL'
]

HEURISTICS_IDS = [
    '1', '2', '3'
]

MOVE_RIGHT = (0, 1)
MOVE_DOWN = (1, 0)
MOVE_LEFT = (0, -1)
MOVE_UP = (-1, 0)
