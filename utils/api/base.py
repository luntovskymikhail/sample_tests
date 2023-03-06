from abc import ABC
from utils.injector import injector


class API(ABC):
    @injector.inject
    def __init__(self, settings):
        self.api_path = settings.url
