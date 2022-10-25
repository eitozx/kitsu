from .data import Title, PosterImage, CoverImage


class Anime:
    def __init__(self, **kwargs):
        self._data = kwargs['data'][0]
        self._meta = kwargs['meta']
        self._links = kwargs['links']

        self._attributes = self._data['attributes']

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def type(self) -> str:
        return self._data.get('type')

    @property
    def createdAt(self):
        return self._attributes.get('createdAt')

    @property
    def updatedAt(self):
        return self._attributes.get('updatedAt')
    
    @property
    def slug(self) -> str:
        return self._attributes.get('slug')

    @property
    def synopsis(self) -> str:
        return self._attributes.get('synopsis')


    @property
    def description(self) -> str:
        return self._attributes.get('description')

    @property
    def titles(self) -> Title:
        return Title(
            self._attributes['titles'].get('en'),
            self._attributes['titles'].get('en_jp'),
            self._attributes['titles'].get('en_us'),
            self._attributes['titles'].get('ja_jp')
        )
    
    @property
    def canonicalTitle(self) -> str:
        return self._attributes.get('canonicalTitle')
    
    @property
    def abbreviatedTitles(self):
        return self._attributes.get('abbreviatedTitles')

    @property
    def averageRating(self) -> float:
        return float(self._attributes.get('averageRating'))

    @property
    def userCount(self) -> int:
        return self._attributes.get('userCount')

    @property
    def favoritesCount(self) -> int:
        return self._attributes.get('favoritesCount')

    @property
    def startDate(self):
        return self._attributes.get('startDate')

    @property
    def endDate(self):
        return self._attributes.get('endDate')

    @property
    def nextRelease(self):
        return self._attributes.get('nextRelease')

    @property
    def popularityRank(self) -> int:
        return self._attributes.get('popularityRank')

    @property
    def ratingRank(self) -> int:
        return self._attributes.get('ratingRank')

    @property
    def ageRating(self):
        return self._attributes.get('ageRating')

    @property
    def ageRatingGuide(self):
        return self._attributes.get('ageRatingGuide')

    @property
    def subtype(self):
        return self._attributes.get('subtype')

    @property
    def status(self):
        return self._attributes.get('status')

    @property
    def tba(self):
        return self._attributes.get('tba')

    @property
    def episodeCount(self) -> int:
        return self._attributes.get('episodeCount')

    @property
    def episodeLength(self) -> int:
        return self._attributes.get('episodeLength')

    @property
    def totalLength(self) -> int:
        return self._attributes.get('totalLength')

    @property
    def youtubeVideoId(self) -> str:
        return self._attributes.get('youtubeVideoId')

    @property
    def showType(self) -> str:
        return self._attributes.get('showType')

    @property
    def nsfw(self) -> bool:
        return self._attributes.get('nsfw')

    @property
    def posterImage(self):
        return PosterImage(self._attributes.get('posterImage'))

    @property
    def coverImage(self):
        return CoverImage(self._attributes.get('coverImage'))

    def __str__(self):
        return self.canonicalTitle


class Manga:
    def __init__(self, **kwargs):
        self._data = kwargs['data'][0]
        self._meta = kwargs['meta']
        self._links = kwargs['links']

        self._attributes = self._data['attributes']

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def type(self) -> str:
        return self._data.get('type')

    @property
    def createdAt(self):
        return self._attributes.get('createdAt')

    @property
    def updatedAt(self):
        return self._attributes.get('updatedAt')
    
    @property
    def slug(self) -> str:
        return self._attributes.get('slug')

    @property
    def synopsis(self) -> str:
        return self._attributes.get('synopsis')


    @property
    def description(self) -> str:
        return self._attributes.get('description')

    @property
    def titles(self) -> Title:
        return Title(
            self._attributes['titles'].get('en'),
            self._attributes['titles'].get('en_jp'),
            self._attributes['titles'].get('en_us'),
            self._attributes['titles'].get('ja_jp')
        )
    
    @property
    def canonicalTitle(self) -> str:
        return self._attributes.get('canonicalTitle')
    
    @property
    def abbreviatedTitles(self):
        return self._attributes.get('abbreviatedTitles')

    @property
    def averageRating(self) -> float:
        return float(self._attributes.get('averageRating'))

    @property
    def userCount(self) -> int:
        return self._attributes.get('userCount')

    @property
    def favoritesCount(self) -> int:
        return self._attributes.get('favoritesCount')

    @property
    def startDate(self):
        return self._attributes.get('startDate')

    @property
    def endDate(self):
        return self._attributes.get('endDate')