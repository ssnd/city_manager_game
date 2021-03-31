from abc import ABC, abstractmethod


class Builder(ABC):

    # @abstractmethod
    def set_color(self, color):
        pass

    # @abstractmethod
    def set_tile(self, image):
        pass

    @abstractmethod
    def render(self):
        pass
