from pythongame.core.common import WallType, Sprite, Direction
from pythongame.core.game_data import register_wall_data, WallData, register_entity_sprite_map, \
    register_entity_sprite_initializer
from pythongame.core.view.image_loading import SpriteSheet, SpriteInitializer


def register_walls():
    _register_plant_tree_palm()
    _register_plant_tree_fat()
    _register_home_wall_side()
    _register_home_wall()
    _register_home_wall_end1()
    _register_home_wall_end2()
    _register_home_wall_bookshelf_1()
    _register_home_wall_small_well()
    _register_home_wall_oven()
    _register_home_wall_table()
    _register_home_wall_cottage_1()
    _register_home_wall_cottage_2()
    _register_home_wall_cottage_3()
    _register_home_wall_cottage_4()
    _register_home_wall_cottage_5()
    _register_home_wall_window_open()
    _register_home_wall_window_planter()
    _register_wall_watertower()
    _register_wall_stone_water()
    _register_wall_water()
    _register_wall()
    _register_wall_stonebridge_left()
    _register_wall_stonebridge_right()
    _register_statue()
    _register_directional_walls()
    _register_patio_table()
    _register_patio_table_2()
    _register_patio_table_3()
    _register_altar()
    _register_patio_chair_1()
    _register_patio_chair_2()
    _register_patio_chair_3()
    _register_chair_black_1()
    _register_chair_black_2()
    _register_chair_black_3()
    _register_chair_black_4()
    _register_chairs()
    _register_shelves()
    _register_barrels()
    _register_baskets()
    _register_boxes()
    _register_stone_crosses()
    _register_signs()
    _register_weapon_rack()
    _register_pillar()
    _register_light_pole()
    _register_well()
    _register_bench_mirror()
    _register_beds()
    _register_pillows()
    _register_decorated_table()
    

# PLANTS

def _register_plant_tree_fat():
    sprite = Sprite.PLANT_TREE_FAT
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 62)
    scaled_sprite_size = (50, 74)
    indices_by_dir = {Direction.DOWN: [(0, 4.67)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -50))
    register_wall_data(WallType.PLANT_TREE_FAT, WallData(sprite, (50, 25)))

def _register_plant_tree_palm():
    sprite = Sprite.PLANT_TREE_PALM
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (65, 110)
    scaled_sprite_size = (47, 100)
    indices_by_dir = {Direction.DOWN: [(2.958, 3.8)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (-12, -58))
    register_wall_data(WallType.PLANT_TREE_PALM, WallData(sprite, (25, 25)))

# WOOD HOUSE

def _register_home_wall():
    sprite = Sprite.HOME_WALL
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 125)
    indices_by_dir = {Direction.DOWN: [(15, 0)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.HOME_WALL, WallData(sprite, (50, 125)))

def _register_home_wall_side():
    sprite = Sprite.HOME_WALL_SIDE
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (100, 25)
    indices_by_dir = {Direction.DOWN: [(15, 3)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.HOME_WALL_SIDE, WallData(sprite, (100, 25)))

def _register_home_wall_end1():
    sprite = Sprite.HOME_WALL_END1
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(14, 0)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.HOME_WALL_END1, WallData(sprite, (50, 50)))
    
def _register_home_wall_end2():
    sprite = Sprite.HOME_WALL_END2
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(13, 0)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.HOME_WALL_END2, WallData(sprite, (50, 50)))

def _register_home_wall_bookshelf_1():
    sprite = Sprite.HOME_WALL_BOOKSHELF_1
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 62)
    scaled_sprite_size = (50, 100)
    indices_by_dir = {Direction.DOWN: [(3, 1.6)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -80))
    register_wall_data(WallType.HOME_WALL_BOOKSHELF_1, WallData(sprite, (50, 20)))

def _register_home_wall_small_well():
    sprite = Sprite.HOME_WALL_SMALL_WELL
    sprite_sheet_tileset1 = SpriteSheet("resources/graphics/human_tileset1.png")
    original_sprite_size = (32, 72)
    scaled_sprite_size = (50, 100)
    indices_by_dir = {Direction.DOWN: [(3, 1.24)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset1, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -60))
    register_wall_data(WallType.HOME_WALL_SMALL_WELL, WallData(sprite, (50, 40)))

def _register_home_wall_oven():
    sprite = Sprite.HOME_WALL_OVEN
    sprite_sheet_tileset1 = SpriteSheet("resources/graphics/human_tileset1.png")
    original_sprite_size = (32, 46)
    scaled_sprite_size = (50, 70)
    indices_by_dir = {Direction.DOWN: [(10, 3.85)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset1, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -40))
    register_wall_data(WallType.HOME_WALL_OVEN, WallData(sprite, (50, 30)))

def _register_home_wall_table():
    sprite = Sprite.HOME_WALL_TABLE
    sprite_sheet_tileset1 = SpriteSheet("resources/graphics/human_tileset1.png")
    original_sprite_size = (59, 26)
    scaled_sprite_size = (100, 50)
    indices_by_dir = {Direction.DOWN: [(5.5, 13.595)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset1, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -18))
    register_wall_data(WallType.HOME_WALL_TABLE, WallData(sprite, (100, 30)))

# COTTAGE HOME

def _register_home_wall_cottage_1():
    sprite = Sprite.HOME_WALL_COTTAGE_1
    sprite_sheet_tileset2 = SpriteSheet("resources/graphics/human_tileset2.png")
    original_sprite_size = (95, 95)
    scaled_sprite_size = (100, 80)
    indices_by_dir = {Direction.DOWN: [(0, 4.45)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset2, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -34))
    register_wall_data(WallType.HOME_WALL_COTTAGE_1, WallData(sprite, (100, 45)))

def _register_home_wall_cottage_2():
    sprite = Sprite.HOME_WALL_COTTAGE_2
    sprite_sheet_tileset2 = SpriteSheet("resources/graphics/human_tileset2.png")
    original_sprite_size = (130, 95)
    scaled_sprite_size = (100, 80)
    indices_by_dir = {Direction.DOWN: [(0, 3.4)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset2, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -34))
    register_wall_data(WallType.HOME_WALL_COTTAGE_2, WallData(sprite, (100, 45)))

def _register_home_wall_cottage_3():
    sprite = Sprite.HOME_WALL_COTTAGE_3
    sprite_sheet_tileset2 = SpriteSheet("resources/graphics/human_tileset2.png")
    original_sprite_size = (95, 95)
    scaled_sprite_size = (100, 80)
    indices_by_dir = {Direction.DOWN: [(1, 4.45)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset2, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -34))
    register_wall_data(WallType.HOME_WALL_COTTAGE_3, WallData(sprite, (100, 45)))

def _register_home_wall_cottage_4():
    sprite = Sprite.HOME_WALL_COTTAGE_4
    sprite_sheet_tileset2 = SpriteSheet("resources/graphics/human_tileset2.png")
    original_sprite_size = (95, 95)
    scaled_sprite_size = (100, 80)
    indices_by_dir = {Direction.DOWN: [(1.68, 2.7)]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset2, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -34))
    register_wall_data(WallType.HOME_WALL_COTTAGE_4, WallData(sprite, (0, 0)))

def _register_home_wall_cottage_5():
    sprite = Sprite.HOME_WALL_COTTAGE_5
    sprite_sheet_tileset2 = SpriteSheet("resources/graphics/human_tileset2.png")
    original_sprite_size = (45, 85)
    scaled_sprite_size = (70, 80)
    indices_by_dir = {Direction.DOWN: [(2.5, 5 )]}
    register_entity_sprite_map(sprite, sprite_sheet_tileset2, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -34))
    register_wall_data(WallType.HOME_WALL_COTTAGE_5, WallData(sprite, (100, 45)))

# WINDOWS

def _register_home_wall_window_open():
    sprite = Sprite.HOME_WALL_WINDOW_OPEN
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (35, 40)
    indices_by_dir = {Direction.DOWN: [(3, 5)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -50))
    register_wall_data(WallType.HOME_WALL_WINDOW_OPEN, WallData(sprite, (0, 0)))

def _register_home_wall_window_planter():
    sprite = Sprite.HOME_WALL_WINDOW_PLANTER
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (35, 40)
    indices_by_dir = {Direction.DOWN: [(5, 5)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -50))
    register_wall_data(WallType.HOME_WALL_WINDOW_PLANTER, WallData(sprite, (0, 0)))

    # DOOR 

    # FRAMED PICTURES

    #CHIMNEY

    #SECRET GRAVE WITH ELDER WAND FOR ENDGAME MWAHAHAHA

# WATER TOWER

def _register_wall_watertower():
    sprite = Sprite.WALL_WATERTOWER
    sprite_sheet = SpriteSheet("resources/graphics/town3.png")
    original_sprite_size = (52, 92)
    scaled_sprite_size = (100, 140)
    indices_by_dir = {Direction.DOWN: [(3.8, 3.2)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -90))
    register_wall_data(WallType.WALL_WATERTOWER, WallData(sprite, (100, 30)))

# ELVEN CASTLE

def _register_wall_stone_water():
    sprite = Sprite.WALL_STONE_WATER
    sprite_sheet = SpriteSheet("resources/graphics/human_material4.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(0, 9)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.WALL_STONE_WATER, WallData(sprite, (50, 50)))

def _register_wall():
    size = (26, 26)
    sprite = Sprite.WALL
    sprite_sheet = SpriteSheet("resources/graphics/stone_tile.png")
    original_sprite_size = (300, 300)
    scaled_sprite_size = (size[0] - 1, size[1] - 1)
    indices_by_dir = {
        Direction.DOWN: [(0, 0)]
    }
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir,
                               (1, 1))
    register_wall_data(WallType.WALL, WallData(sprite, size))

# STONE BRIDGE

def _register_wall_stonebridge_left():
    sprite = Sprite.WALL_STONEBRIDGE_LEFT
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset1.png")
    original_sprite_size = (32, 120)
    scaled_sprite_size = (30, 175)
    indices_by_dir = {Direction.DOWN: [(0, 2.15)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -20))
    register_wall_data(WallType.WALL_STONEBRIDGE_LEFT, WallData(sprite, (30, 155)))

def _register_wall_stonebridge_right():
    sprite = Sprite.WALL_STONEBRIDGE_RIGHT
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset1.png")
    original_sprite_size = (32, 120)
    scaled_sprite_size = (30, 175)
    indices_by_dir = {Direction.DOWN: [(2.08, 2.15)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, -20))
    register_wall_data(WallType.WALL_STONEBRIDGE_RIGHT, WallData(sprite, (30, 155)))

# DIRECTIONAL WALLS

def _register_directional_walls():
    _register_directional_wall(WallType.WALL_DIRECTIONAL_N, Sprite.WALL_DIRECTIONAL_N,
                               "resources/graphics/hyrule_wall_top_corner.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_NE, Sprite.WALL_DIRECTIONAL_NE,
                               "resources/graphics/hyrule_wall_top_corner.png", [1, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_E, Sprite.WALL_DIRECTIONAL_E,
                               "resources/graphics/hyrule_wall_right_corner.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_SE, Sprite.WALL_DIRECTIONAL_SE,
                               "resources/graphics/hyrule_wall_right_corner.png", [0, 1])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_S, Sprite.WALL_DIRECTIONAL_S,
                               "resources/graphics/hyrule_wall_left_corner_bot.png", [1, 1])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_SW, Sprite.WALL_DIRECTIONAL_SW,
                               "resources/graphics/hyrule_wall_left_corner_bot.png", [0, 1])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_W, Sprite.WALL_DIRECTIONAL_W,
                               "resources/graphics/hyrule_wall_left_corner_bot.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_NW, Sprite.WALL_DIRECTIONAL_NW,
                               "resources/graphics/hyrule_wall_corner.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_POINTY_NE, Sprite.WALL_DIRECTIONAL_POINTY_NE,
                               "resources/graphics/hyrule_wall_pointy_corner_ne.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_POINTY_SE, Sprite.WALL_DIRECTIONAL_POINTY_SE,
                               "resources/graphics/hyrule_wall_pointy_corner_se.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_POINTY_SW, Sprite.WALL_DIRECTIONAL_POINTY_SW,
                               "resources/graphics/hyrule_wall_pointy_corner_sw.png", [0, 0])
    _register_directional_wall(WallType.WALL_DIRECTIONAL_POINTY_NW, Sprite.WALL_DIRECTIONAL_POINTY_NW,
                               "resources/graphics/hyrule_wall_pointy_corner_nw.png", [0, 0])


def _register_directional_wall(wall_type, sprite, sprite_sheet_path, sprite_sheet_index):
    register_entity_sprite_map(
        sprite, SpriteSheet(sprite_sheet_path), (21, 21), (25, 25),
        {Direction.DOWN: [sprite_sheet_index]}, (0, 0))
    register_wall_data(wall_type, WallData(sprite, (25, 25)))

# STATUE

def _register_statue():
    sprite = Sprite.WALL_STATUE
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 64)
    scaled_sprite_size = (50, 100)
    indices_by_dir = {Direction.DOWN: [(13, 3)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (-4, -54))
    register_wall_data(WallType.STATUE, WallData(sprite, (42, 46)))

# STONE CROSSES

def _register_stone_crosses():
    sprites = [Sprite.WALL_STONE_CROSS_FLOWERS]
    wall_types = [WallType.STONE_CROSS_FLOWERS]
    indices = [(15, 3)]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 64)
    scaled_sprite_size = (50, 100)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (-7, -54))
        register_wall_data(wall_types[i], WallData(sprites[i], (42, 39)))

# TABLES

def _register_patio_table():
    sprite = Sprite.WALL_PATIO_TABLE
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(4, 6.5)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_TABLE, WallData(sprite, (50, 20))) 

def _register_patio_table_2():
    sprite = Sprite.WALL_PATIO_TABLE_2
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(5, 6.5)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_TABLE_2, WallData(sprite, (50, 20))) 

def _register_patio_table_3():
    sprite = Sprite.WALL_PATIO_TABLE_3
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(3, 6.5)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_TABLE_3, WallData(sprite, (50, 20))) 

def _register_altar():
    sprite = Sprite.WALL_ALTAR
    sprite_sheet = SpriteSheet("resources/graphics/wall_altar.png")
    original_sprite_size = (88, 38)
    scaled_sprite_size = (100, 50)
    indices_by_dir = {Direction.DOWN: [(0, 0)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -13))
    register_wall_data(WallType.ALTAR, WallData(sprite, (100, 25)))  # table is roughly 13px tall

# CHAIRS

def _register_patio_chair_1():
    sprite = Sprite.WALL_PATIO_CHAIR_1
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 42)
    scaled_sprite_size = (20, 50)
    indices_by_dir = {Direction.DOWN: [(10.1, 4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_CHAIR_1, WallData(sprite, (20, 20))) 

def _register_patio_chair_2():
    sprite = Sprite.WALL_PATIO_CHAIR_2
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 42)
    scaled_sprite_size = (20, 50)
    indices_by_dir = {Direction.DOWN: [(11, 4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_CHAIR_2, WallData(sprite, (20, 20))) 

def _register_patio_chair_3():
    sprite = Sprite.WALL_PATIO_CHAIR_3
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 42)
    scaled_sprite_size = (20, 50)
    indices_by_dir = {Direction.DOWN: [(9, 4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -30))
    register_wall_data(WallType.PATIO_CHAIR_3, WallData(sprite, (20, 20)))

def _register_chair_black_1():
    sprite = Sprite.WALL_CHAIR_BLACK_1
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 22)
    scaled_sprite_size = (20, 40)
    indices_by_dir = {Direction.DOWN: [(7, 8.4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -10))
    register_wall_data(WallType.CHAIR_BLACK_1, WallData(sprite, (20, 30))) 

def _register_chair_black_2():
    sprite = Sprite.WALL_CHAIR_BLACK_2
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 22)
    scaled_sprite_size = (20, 40)
    indices_by_dir = {Direction.DOWN: [(6, 8.4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -10))
    register_wall_data(WallType.CHAIR_BLACK_2, WallData(sprite, (20, 30)))  

def _register_chair_black_3():
    sprite = Sprite.WALL_CHAIR_BLACK_3
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 22)
    scaled_sprite_size = (25, 40)
    indices_by_dir = {Direction.DOWN: [(4.1, 8.4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -20))
    register_wall_data(WallType.CHAIR_BLACK_3, WallData(sprite, (25, 20)))

def _register_chair_black_4():
    sprite = Sprite.WALL_CHAIR_BLACK_4
    sprite_sheet = SpriteSheet("resources/graphics/town2.png")
    original_sprite_size = (16, 22)
    scaled_sprite_size = (25, 40)
    indices_by_dir = {Direction.DOWN: [(5.075, 8.4)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size, indices_by_dir, (0, -20))
    register_wall_data(WallType.CHAIR_BLACK_4, WallData(sprite, (25, 20)))  

def _register_chairs():
    sprites = [Sprite.WALL_CHAIR_DOWN, Sprite.WALL_CHAIR_UP, Sprite.WALL_CHAIR_RIGHT, Sprite.WALL_CHAIR_LEFT]
    wall_types = [WallType.CHAIR_DOWN, WallType.CHAIR_UP, WallType.CHAIR_RIGHT, WallType.CHAIR_LEFT]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices = [(4, 0), (5, 0), (6, 0), (7, 0)]
    for i in range(len(sprites)):
        indices_by_dir = {Direction.DOWN: [indices[i]]}
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   indices_by_dir, (0, 0))
        register_wall_data(wall_types[i], WallData(sprites[i], (50, 50)))


def _register_shelves():
    sprites = [Sprite.WALL_SHELF_EMPTY, Sprite.WALL_SHELF_HELMETS, Sprite.WALL_SHELF_ARMORS]
    wall_types = [WallType.SHELF_EMPTY, WallType.SHELF_HELMETS, WallType.SHELF_ARMORS]
    indices = [(1, 0), (1, 1), (1, 2)]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (64, 32)
    scaled_sprite_size = (100, 50)
    for i in range(3):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -25))
        register_wall_data(wall_types[i], WallData(sprites[i], (100, 25)))


def _register_barrels():
    sprites = [Sprite.WALL_BARREL_1, Sprite.WALL_BARREL_2, Sprite.WALL_BARREL_3, Sprite.WALL_BARREL_4,
               Sprite.WALL_BARREL_5, Sprite.WALL_BARREL_6]
    wall_types = [WallType.BARREL_1, WallType.BARREL_2, WallType.BARREL_3, WallType.BARREL_4, WallType.BARREL_5,
                  WallType.BARREL_6]
    indices = [(3, 11), (3, 12), (4, 11), (4, 12), (5, 11), (5, 12)]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -25))
        register_wall_data(wall_types[i], WallData(sprites[i], (50, 25)))


def _register_baskets():
    sprites = [Sprite.WALL_BASKET_EMPTY, Sprite.WALL_BASKET_FRUIT]
    wall_types = [WallType.BASKET_EMPTY, WallType.BASKET_FRUIT]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    indices = [(4, 15), (5, 15)]
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -25))
        register_wall_data(wall_types[i], WallData(sprites[i], (50, 25)))

def _register_boxes():
    sprites = [Sprite.WALL_BOX_EMPTY, Sprite.WALL_BOX_FRUIT, Sprite.WALL_BOX_FISH]
    wall_types = [WallType.BOX_EMPTY, WallType.BOX_FRUIT, WallType.BOX_FISH]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    indices = [(9, 4), (10, 4), (9, 5)]
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -25))
        register_wall_data(wall_types[i], WallData(sprites[i], (50, 25)))


def _register_signs():
    sprites = [Sprite.WALL_SIGN_SMALL, Sprite.WALL_SIGN_MULTI, Sprite.WALL_SIGN_LARGE_EMPTY,
               Sprite.WALL_SIGN_LARGE_NOTES]
    wall_types = [WallType.SIGN_SMALL, WallType.SIGN_MULTI, WallType.SIGN_LARGE_EMPTY, WallType.SIGN_LARGE_NOTES]
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    indices = [(14, 2), (13, 2), (13, 1), (14, 1)]
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -25))
        register_wall_data(wall_types[i], WallData(sprites[i], (50, 25)))


def _register_weapon_rack():
    register_entity_sprite_initializer(Sprite.WALL_WEAPON_RACK,
                                       SpriteInitializer("resources/graphics/wall_weapon_rack.png", (50, 100)),
                                       (0, -70))
    register_wall_data(WallType.WEAPON_RACK, WallData(Sprite.WALL_WEAPON_RACK, (50, 30)))


def _register_pillar():
    register_entity_sprite_initializer(Sprite.WALL_PILLAR,
                                       SpriteInitializer("resources/graphics/wall_pillar.png", (55, 110)),
                                       (0, -60))
    register_wall_data(WallType.PILLAR, WallData(Sprite.WALL_PILLAR, (50, 50)))


def _register_light_pole():
    register_entity_sprite_initializer(Sprite.WALL_LIGHT_POLE,
                                       SpriteInitializer("resources/graphics/wall_lightpole.png", (35, 105)),
                                       (0, -80))
    register_wall_data(WallType.LIGHT_POLE, WallData(Sprite.WALL_LIGHT_POLE, (35, 25)))


def _register_well():
    register_entity_sprite_initializer(Sprite.WALL_WELL,
                                       SpriteInitializer("resources/graphics/wall_well.png", (85, 75)),
                                       (0, -10))
    register_wall_data(WallType.WELL, WallData(Sprite.WALL_WELL, (75, 65)))


def _register_bench_mirror():
    register_entity_sprite_initializer(Sprite.WALL_BENCH_MIRROR,
                                       SpriteInitializer("resources/graphics/wall_bench_mirror.png", (35, 70)),
                                       (0, -50))
    register_wall_data(WallType.BENCH_MIRROR, WallData(Sprite.WALL_BENCH_MIRROR, (35, 20)))


def _register_beds():
    sprites = [Sprite.WALL_BED_1, Sprite.WALL_BED_2, Sprite.WALL_BED_3]
    wall_types = [WallType.BED_1, WallType.BED_2, WallType.BED_3]
    sprite_sheet = SpriteSheet("resources/graphics/wall_beds.png")
    indices = [(0, 0), (2, 0), (3, 0)]
    original_sprite_size = (32, 80)
    scaled_sprite_size = (36, 90)
    for i in range(len(sprites)):
        register_entity_sprite_map(sprites[i], sprite_sheet, original_sprite_size, scaled_sprite_size,
                                   {Direction.DOWN: [indices[i]]}, (0, -20))
        register_wall_data(wall_types[i], WallData(sprites[i], (36, 70)))


def _register_pillows():
    register_entity_sprite_initializer(Sprite.WALL_PILLOW,
                                       SpriteInitializer("resources/graphics/wall_pillow.png", (40, 30)),
                                       (0, 0))
    register_wall_data(WallType.PILLOW, WallData(Sprite.WALL_PILLOW, (40, 30)))
    register_entity_sprite_initializer(Sprite.WALL_PILLOWS_2,
                                       SpriteInitializer("resources/graphics/wall_pillows_2.png", (40, 35)),
                                       (0, -5))
    register_wall_data(WallType.PILLOWS_2, WallData(Sprite.WALL_PILLOWS_2, (40, 30)))


def _register_decorated_table():
    register_entity_sprite_initializer(Sprite.WALL_DECORATED_TABLE,
                                       SpriteInitializer("resources/graphics/wall_table_candles.png", (100, 75)),
                                       (-5, -35))
    register_wall_data(WallType.DECORATED_TABLE, WallData(Sprite.WALL_DECORATED_TABLE, (90, 40)))

# ELEMENTS

def _register_wall_water():
    sprite = Sprite.WALL_WATER
    sprite_sheet = SpriteSheet("resources/graphics/human_material4.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(1, 0)]}
    register_entity_sprite_map(sprite, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))
    register_wall_data(WallType.WALL_WATER, WallData(sprite, (50, 50)))