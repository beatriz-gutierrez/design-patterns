from PIL import Image
from abc import ABC, abstractmethod
from enum import Enum
import os


class ImageStratery(ABC):

    @abstractmethod
    def __call__(self, img_file, desktop_size):
        raise NotImplementedError


class TiledStrategy(ImageStratery):

    def __init__(self):
        self.name = Strategy.titled

    def __call__(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        num_tiles = [o // i + 1 for o, i in zip(out_img.size, in_img.size)]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x + 1),
                        in_img.size[1] * (y + 1),
                    ),
                )
        return out_img


class CenteredStrategy(ImageStratery):

    def __init__(self):
        self.name = Strategy.centered

    def __call__(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new("RGB", desktop_size)
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(in_img, (left, top, left + in_img.size[0], top + in_img.size[1]))
        return out_img


class ScaledStrategy(ImageStratery):

    def __init__(self):
        self.name = Strategy.scaled

    def __call__(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = in_img.resize(desktop_size)
        return out_img


class Strategy(Enum):
    titled = TiledStrategy
    centered = CenteredStrategy
    scaled = ScaledStrategy


class User():

    def __init__(self, image, desktop_size):
        self.image = image
        self.desktop_size = desktop_size

    def select_strategy(self, strategy: Strategy):
        strategy_class = strategy.value
        strat = strategy_class() 
        print(f"Using the {strat.name} strategy.")
        return strat(self.image, self.desktop_size)

if __name__ == "__main__":

    user = User(os.path.join("strategy", "tree.png"), [600, 800])
    image = user.select_strategy(Strategy.scaled)
    image.show()
    
