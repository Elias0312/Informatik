from enum import Enum

class MediaType(Enum):
    VIDEO = "Video"
    AUDIO = "Audio"
    IMAGE = "Image"

class MediaAsset:
    def __init__(self, title: str, size_mb: float, media_type: MediaType):
        self.title = title
        self.size_mb = size_mb
        self.media_type = media_type

    def describe(self):
        print (f"{self.title}({self.size_mb}mb, {self.media_type.value})")

    
class AudioAsset(MediaAsset):
    def __init__(self, title, size_mb, duration_min: str, artist: str):
        super().__init__(title, size_mb, MediaType.AUDIO)
        self.duration_min = duration_min
        self.artist = artist

    def describe(self):
        print (f"{self.title}, {self.artist} ({self.size_mb}mb, {self.media_type.value}, {self.duration_min})")

class VideoAsset(MediaAsset):
    def __init__(self, title, size_mb, resolution: str, fps: int):
        super().__init__(title, size_mb, MediaType.VIDEO)
        self.resolution = resolution
        self.fps = fps

    def describe(self):
        print (f"{self.title}({self.size_mb}mb, {self.resolution}, {self.fps}fps {self.media_type.value})")

class ImageAsset(MediaAsset):
    def __init__(self, title, size_mb, resolution, color_space):
        super().__init__(title, size_mb, MediaType.IMAGE)
        self.resolution = resolution
        self.color_space = color_space

    def describe(self):
        print (f"{self.title}({self.size_mb}mb, {self.resolution}, color_space: {self.color_space}, {self.media_type})")

class MediaArchive:
    def __init__(self):
        self.assets = []

    def add_assets(self, asset: MediaAsset):
        self.assets.append(asset)

    def list_assets(self):
        for i in self.assets:
            i.describe()

    def find_by_type(self, type: MediaType):
        for i in self.assets:
            if i.media_type == type:
                i.describe()

    def total_storage(self):
        total = 0
        for i in self.assets:
            total += i.size_mb
        return total
    