from typing import Any, Optional, Union
from pynotifier import Notification
from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform
import os
import sys
import threading

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

Number = Union[float, int]
PathStr = Union[str, Any]


class KNotifySound:
    """Clase utilizada para evitar la carga de un sonido cada vez que se vaya a
    utilizar para reproducir una notificación."""

    def __init__(
        self,
        sound: Union["KNotifySound", PathStr],
    ):
        # Inicializar el mixer de pygame
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()

        if isinstance(sound, KNotifySound):
            self._sound = sound._sound
        else:
            try:
                file_path = str(sound)
            except Exception as e:
                raise ValueError(
                    f"Error trying to convert the PathStr {sound} into str:\n{e}."
                )
            self._sound = pygame.mixer.Sound(file_path)

    def setter(
        self,
        sound: Union["KNotifySound", PathStr],
    ):
        if isinstance(sound, KNotifySound):
            self._sound = sound._sound
        else:
            try:
                file_path = str(sound)
            except Exception as e:
                raise ValueError(
                    f"Error trying to convert the PathStr {sound} into str:\n{e}."
                )
            self._sound = pygame.mixer.Sound(file_path)

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
        default_image: Optional[PathStr] = None,
        default_async_play: bool = False,
        default_sound: Optional[Union[KNotifySound, PathStr]] = None,
    ):
        # defaults
        self._default_title = default_title
        self._default_duration = default_duration
        self._default_image = self._convert_image_path(default_image)
        self._default_sound = None  # required before first read
        self._default_sound = self._read_sound_parameter(default_sound)
        self._default_image = default_image
        self._default_async_play = default_async_play

        # client
        self._client = NotificationClient()
        self._client.register_backend(platform.Backend())

    def send(
        self,
        msg: Optional[str] = None,
        title: Optional[str] = None,
        duration: Optional[Number] = None,
        image: Optional[PathStr] = None,
        async_play: Optional[bool] = None,
        sound: Optional[Union[KNotifySound, PathStr]] = None,
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

        sound = self._read_sound_parameter(sound)
        if sound is not None:  # default_sound can also be None
            sound.play(async_play)

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
    def default_sound(self, value: Optional[Union[KNotifySound, str]]):
        self._default_sound = self._read_sound_parameter(value)

    @property
    def default_async_play(self):
        return self._default_async_play

    @default_async_play.setter
    def default_async_play(self, value):
        self._default_async_play = value

    def _convert_image_path(self, path: Any):
        try:
            return str(path)
        except Exception as e:
            print(
                f"default_image debe ser un path o en general, cualquier cosa que pueda"
                f" ser convertida a str y sea una ubicación real de una imagen. Mensaje"
                f" de excepción:\n{e}"
            )

    def _read_sound_parameter(self, sound: Optional[Union[KNotifySound, PathStr]]):
        if sound is None:
            return self._default_sound
        return KNotifySound(sound)

    def _set_notify_defaults(
        self,
        title: Optional[str],
        msg: Optional[str],
        duration: Optional[Number],
        image: Optional[PathStr],
        async_play: Optional[bool],
        sound: Optional[Union[KNotifySound, str]],
    ):
        title = title if title is not None else self.default_title
        if title is None:
            title = self._get_app_name()
        msg = msg if msg is not None else ""
        if image is None:
            image = self._default_image
        else:
            image = self._convert_image_path(image)
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
