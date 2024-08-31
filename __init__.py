"""
This library is designed to easily implement notifications with images and
sounds in your Python scripts.

Please note that the number of imports is considerable, and users of the script
will need to install some dependencies depending on their operating system.
Additionally, the design may change.

# Credits

- **py-notifier**: https://github.com/YuriyLisovskiy/pynotifier
- **WinToaster**: https://github.com/MaliciousFiles/WinToaster
- **pygame**: https://github.com/pygame/pygame
- **libnotify**: https://github.com/GNOME/libnotify

# Dependencies

```bash
pip install py-notifier
pip install pygame
# Windows
    pip install WinToaster

# Linux (no pip, requires manual install)
ArchLinux: sudo pacman -S libnotify
Debian : sudo apt-get install libnotify-bin

Usage:
There are two classes: PygameSound, KNotification
```

# PygameSound

Optionally used to store sounds in variables, preload them, and avoid
specifying the path to the sound each time you use a different sound than the
default one set in KNotification (if you choose to set a default sound).

# KNotification

Used to create a notification object where you can set default settings,
though you can always specify the details of the notification explicitly for
each dispatch. You can also create different notification objects, for
example, one for errors and another for informational messages, allowing you
to define different default details for each."""

from typing import Optional, Union
from pynotifier import Notification
from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
import os
import sys
import threading

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

Number = Union[float, int]


class PygameSound:
    def __init__(
        self,
        sound: Optional[Union[str, "PygameSound", pygame.mixer.Sound]],
    ):
        """
        Initializes the sound object.

        :param sound: Path to the sound file (str), another PygameSound object, or a
            pygame sound object.
        """

        pygame.mixer.init()  # Inicializar el mezclador de pygame

        if isinstance(sound, PygameSound):
            self._sound = sound._sound
        elif isinstance(sound, pygame.mixer.Sound):
            self._sound = sound
        elif isinstance(sound, str):
            self.file_path = sound
            self._sound = pygame.mixer.Sound(self.file_path)
        else:
            raise ValueError(
                "The 'sound' parameter must be a file path (str), a PygameSound object, or a pygame.mixer.Sound object."
            )

    def setter(
        self,
        sound: Optional[Union[str, "PygameSound", pygame.mixer.Sound]],
    ):
        """
        Configures the sound object after initialization.

        :param sound: Path to the sound file (str), another PygameSound object, or a
            pygame sound object.
        """
        if isinstance(sound, PygameSound):
            self._sound = sound._sound
        elif isinstance(sound, pygame.mixer.Sound):
            self._sound = sound
        elif isinstance(sound, str):
            self.file_path = sound
            self._sound = pygame.mixer.Sound(self.file_path)
        else:
            raise ValueError(
                "default_sound have to be PygameSound or a str with the file_path but it is {type(default_sound)}"
            )

    def play(self, async_play=False):
        def play_sound():
            pygame.mixer.Channel(0).play(self._sound)
            while pygame.mixer.Channel(0).get_busy():
                pygame.time.wait(10)  # Esperar a que termine la reproducción

        if async_play:
            pygame.mixer.Channel(0).play(self._sound)
            self._play_thread = threading.Thread(target=play_sound)
            self._play_thread.start()
        else:
            pygame.mixer.Channel(0).play(self._sound)
            while pygame.mixer.Channel(0).get_busy():
                pygame.time.wait(10)  # Esperar a que termine la reproducción


class KNotification:
    def __init__(
        self,
        *,
        default_title: Optional[str] = None,
        default_duration: Number = 10,
        default_image: Optional[str] = None,
        default_async_play: bool = False,
        default_sound: Optional[Union[PygameSound, str]] = None,
    ):
        # defaults
        self._default_title = default_title
        self._default_duration = default_duration
        self._default_image = default_image
        self._default_sound = self._read_sound_parameter(default_sound)
        self._default_image = default_image
        self._default_async_play = default_async_play

        # client
        self._client = NotificationClient()
        self._client.register_backend(platform.Backend())

    def _read_sound_parameter(self, default_sound: Optional[Union[PygameSound, str]]):
        if default_sound is None:
            return
        if isinstance(default_sound, (PygameSound, pygame.mixer.Sound, str)):
            return PygameSound(default_sound)
        raise ValueError(
            f"default_sound have to be PygameSound or a str with the file_path but it is {type(default_sound)}"
        )

    @property
    def default_title(self):
        return self._default_title

    @default_title.setter
    def default_title(self, value):
        self._default_title = value

    @property
    def default_duration(self):
        return self._default_duration

    @default_duration.setter
    def default_duration(self, value):
        self._default_duration = value

    @property
    def default_sound(self):
        return self._default_sound

    @default_sound.setter
    def default_sound(self, value: Optional[Union[PygameSound, str]]):
        self._default_sound = self._read_sound_parameter(value)

    @property
    def default_async_play(self):
        return self._default_async_play

    @default_async_play.setter
    def default_async_play(self, value):
        self._default_async_play = value

    def send(
        self,
        msg: Optional[str] = None,
        title: Optional[str] = None,
        duration: Optional[Number] = None,
        image: Optional[str] = None,
        async_play: Optional[bool] = None,
        sound: Optional[Union[PygameSound, str]] = None,
    ):
        title, msg, duration, image, async_play, sound = self._set_notify_defaults(
            title, msg, duration, image, async_play, sound
        )

        notification = Notification(
            title=title,
            message=msg,
            icon_path=image,
            duration=duration,
        )
        self._client.notify_all(notification)

        sound = self._default_sound if sound is None else sound
        if sound is not None:  # default_sound can also be None
            sound.play(async_play)

    def _set_notify_defaults(
        self,
        title: Optional[str],
        msg: Optional[str],
        duration: Optional[Number],
        image: Optional[str],
        async_play: Optional[bool],
        sound: Optional[Union[PygameSound, str]],
    ):
        title = title if title is not None else self.default_title
        if title is None:
            title = self._get_app_name()
        msg = msg if msg is not None else ""
        image = image if image is not None else self._default_image
        duration = duration if duration is not None else self.default_duration
        async_play = async_play if async_play is not None else self.default_async_play
        sound = self._read_sound_parameter(sound)
        return title, msg, duration, image, async_play, sound

    def _get_app_name(self) -> str:
        """
        Obtiene el nombre del archivo ejecutable o script.
        :return: Nombre del archivo ejecutable o script.
        """
        return sys.argv[0]
