from pythongame.core.common import Direction
from pythongame.core.game_data import register_entity_sprite_map, Sprite
from pythongame.core.view.image_loading import SpriteSheet


def register_decorations():
    _register_ground_decorations()
    _register_plant_decoration()


# FLOOR TILES

def _register_ground_decorations():
    sprite_sheet = SpriteSheet("resources/graphics/material_tileset.png")
    sprite_sheet_town2 = SpriteSheet("resources/graphics/town2.png")
    sprite_sheet_town3 = SpriteSheet("resources/graphics/town3.png")
    sprite_sheet_human1 = SpriteSheet("resources/graphics/human_tileset1.png")
    sprite_sheet_human3 = SpriteSheet("resources/graphics/human_material3.png")
    sprite_sheet_human4 = SpriteSheet("resources/graphics/human_material4.png")
    sprite_sheet_cute = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    original_sprite_size_stretch = (10, 22)
    original_sprite_size_stretch_2 = (16.5, 48)
    scaled_sprite_size = (50, 50)
    scaled_sprite_size_small = (30, 30)
    indices_by_dir = {Direction.DOWN: [(4, 4)]}
    

    register_entity_sprite_map(Sprite.DECORATION_GROUND_SIDEWALK, sprite_sheet_town2, original_sprite_size_stretch_2, scaled_sprite_size,
                                {Direction.DOWN: [(0, 1.37)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_STREET_LANES, sprite_sheet_town3, original_sprite_size_stretch, scaled_sprite_size,
                                {Direction.DOWN: [(20.3, 8.6)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_STONEBRIDGE, sprite_sheet_human1, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(1, 9)]}, (0, 0))
    
    register_entity_sprite_map(Sprite.DECORATION_GROUND_STONE, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_STONE_GRAY, sprite_sheet, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(0, 2)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_WATER, sprite_sheet_human4, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(1, 0)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_GRASS, sprite_sheet_human3, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(0, 0)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_GRASS_WATER_EDGE_LEFTC, sprite_sheet_human4, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(0, 7)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_GRASS_WATER_EDGE_RIGHTC, sprite_sheet_human4, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(1, 7)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_GRASS_EDGE, sprite_sheet_human3, original_sprite_size, scaled_sprite_size_small,
                                {Direction.DOWN: [(8, 6.1)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_GRASS_EDGE_2, sprite_sheet_human3, original_sprite_size, scaled_sprite_size_small,
                                {Direction.DOWN: [(8.95, 6.16)]}, (0, 0))
                                
    register_entity_sprite_map(Sprite.DECORATION_GROUND_PEPPLES, sprite_sheet_human3, original_sprite_size, scaled_sprite_size_small,
                                {Direction.DOWN: [(15, 5)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_PEPPLES_2, sprite_sheet_human3, original_sprite_size, scaled_sprite_size_small,
                                {Direction.DOWN: [(14, 5)]}, (0, 0))


    register_entity_sprite_map(Sprite.DECORATION_GROUND_STAIRS, sprite_sheet, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(6, 8)]}, (0, 0))

    register_entity_sprite_map(Sprite.DECORATION_GROUND_SMOOTH, sprite_sheet, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(6, 4)]}, (0, 0))

# MOUNTAIN SIDES

    register_entity_sprite_map(Sprite.DECORATION_GROUND_MOUNTAIN, sprite_sheet, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(1, 7)]}, (0, 0))

# BOXES

    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES1, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(9, 5)]}, (0, 0))
    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES2, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(9, 4)]}, (0, 0))
    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES3, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(8, 4)]}, (0, 0))
    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES4, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(8, 5)]}, (0, 0))
    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES5, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(5, 7)]}, (0, 0))
    register_entity_sprite_map(Sprite.DECORATION_GROUND_BOXES6, sprite_sheet_cute, original_sprite_size, scaled_sprite_size,
                                {Direction.DOWN: [(6, 9)]}, (0, 0))


def _register_plant_decoration():
    sprite_sheet = SpriteSheet("resources/graphics/human_tileset.png")
    original_sprite_size = (32, 32)
    scaled_sprite_size = (50, 50)
    indices_by_dir = {Direction.DOWN: [(12, 1)]}
    register_entity_sprite_map(Sprite.DECORATION_PLANT, sprite_sheet, original_sprite_size, scaled_sprite_size,
                               indices_by_dir, (3, 5))
