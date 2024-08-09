from pythongame.core.common import ItemType, Sprite, UiIconSprite
from pythongame.game_data.items.register_items_util import register_quest_item


def register_portal_key_cult_item():
    register_quest_item(
        item_type=ItemType.PORTAL_KEY_CULT,
        ui_icon_sprite=UiIconSprite.ITEM_PORTAL_KEY_CULT,
        sprite=Sprite.ITEM_PORTAL_KEY_CULT,
        image_file_path="resources/graphics/item_torn_document.png",
        name="Torn cult document",
        description_lines=["Grants access to the secret meeting under the town square!"]
    )
