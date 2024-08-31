"""
Sample image paths and some KNotifySound(s)

SND_NOTIFY, SND_ERROR, SND_ERROR2
IMG_NOTIFY, IMG_ERROR
"""

import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
from .src.knotification import KNotifySound

SND_NOTIFY = KNotifySound(f"{PACKAGE_DIR}/sound/notification.wav")
SND_ERROR = KNotifySound(f"{PACKAGE_DIR}/sound/error.wav")
SND_ERROR2 = KNotifySound(f"{PACKAGE_DIR}/sound/error2.aiff")

IMG_NOTIFY = f"{PACKAGE_DIR}/image/info.png"
IMG_ERROR = f"{PACKAGE_DIR}/image/error.png"
