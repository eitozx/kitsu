import dataclasses

@dataclasses.dataclass
class Title:
    en : str = None
    en_jp : str = None
    en_us : str = None
    ja_jp : str = None

    def __str__(self):
        return self.en or self.en_us or self.en_jp


class PosterImage:
    def __init__(self, kwargs):
        self._data = kwargs

    @property
    def tiny(self):
         return self._data.get('tiny')

    @property
    def small(self):
         return self._data.get('small')
         
    @property
    def medium(self):
         return self._data.get('medium')

    @property
    def large(self):
         return self._data.get('large')

    @property
    def original(self):
         return self._data.get('original')

    def __str__(self):
        return self.original


class CoverImage:
    def __init__(self, kwargs):
        self._data = kwargs

    @property
    def tiny(self):
         return self._data.get('tiny')

    @property
    def small(self):
         return self._data.get('small')

    @property
    def large(self):
         return self._data.get('large')

    @property
    def original(self):
         return self._data.get('original')

    def __str__(self):
        return self.original