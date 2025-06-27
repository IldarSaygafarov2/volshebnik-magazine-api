import os

from core.shop.settings import IMAGES_PATH


class ImageService:

    def get_images_from_dir(self):
        result = {}
        dir_items = os.listdir(IMAGES_PATH)

        for _dir in dir_items:
            item_path = os.path.join(IMAGES_PATH, _dir)
            result[_dir] = []
            if os.path.isdir(item_path):
                dir_inner_items = os.listdir(item_path)
                for inner_item in dir_inner_items:
                    result[_dir].append(os.path.join(IMAGES_PATH, inner_item))
        return result


image_service = ImageService()
