from pythongame.core.common import ItemType, Sprite, UiIconSprite, HeroStat
from pythongame.core.item_inventory import ItemEquipmentCategory
from pythongame.game_data.items.register_items_util import register_randomized_stat_modifying_item


def register_fire_wand_item():
    register_randomized_stat_modifying_item(
        item_type=ItemType.FIRE_WAND,
        item_level=4,
        ui_icon_sprite=UiIconSprite.ITEM_FIRE_WAND,
        sprite=Sprite.ITEM_FIRE_WAND,
        image_file_path="resources/graphics/item_fire_wand.png",
        item_equipment_category=ItemEquipmentCategory.MAIN_HAND,
        name="Fire wand",
        stat_modifier_intervals={HeroStat.MANA_REGEN: [0.2, 0.3, 0.4], HeroStat.MAGIC_DAMAGE: [0.09, 0.1, 0.11]}
    )
