from os import sep

PATH_RESOURCES = "resources" + sep


class Path:
    """Path manager for the entire game"""

    AUDIO_SUFFIX = ".ogg"
    IMAGE_SUFFIX = ".png"
    DATA_SUFFIX = ".json"
    FONT_SUFFIX = ".otf"

    @staticmethod
    def resources():
        """Return resources path"""
        return PATH_RESOURCES

    @staticmethod
    def styles():
        """Return style's directory path"""
        return PATH_RESOURCES + "styles" + sep

    @staticmethod
    def soundtracks():
        """Return soundtrack's directory path"""
        return PATH_RESOURCES + "soundtracks" + sep

    @staticmethod
    def fonts():
        """Return font's directory path"""
        return PATH_RESOURCES + "fonts" + sep

    @staticmethod
    def images():
        """Return image's directory path"""
        return PATH_RESOURCES + "images" + sep

    @staticmethod
    def sounds():
        """Return sound's directory path"""
        return PATH_RESOURCES + "sounds" + sep
