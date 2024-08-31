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

# Install && Dependencies

```bash
pip install knotification

# Installed automatically (dependencies of knotification)
# pip install py-notifier
# pip install pygame
# pip install WinToaster (in windows)

# Manual installation required
# Linux (Arch/Debian)
sudo pacman -S libnotify
sudo apt-get install libnotify-bin

# Other Linux distributions/Mac
# I'm sorry but I'm still not sure.
```

# Sample Usage

```python
from knotification import KNotification
from knotification.sample import (
    SND_NOTIFY,
    SND_ERROR,
    SND_ERROR2,
    IMG_NOTIFY,
    IMG_ERROR,
)
import time

notify = KNotification(
    default_title="KNotification",
    default_sound=SND_NOTIFY,
    default_image=f"{IMG_NOTIFY}",
)
error = KNotification(default_sound=SND_ERROR, default_image=f"{IMG_ERROR}")

notify.send("Thanks for using my software")
time.sleep(1)
error.send(f"[!] Error: Not enough resources.\n\nCheck the manual.")
time.sleep(1)
error.send(f"[!] Error: Not enough notifies.", duration=20, sound=SND_ERROR2)
```

# KNotifySound

Optionally used to store sounds in variables, preload them, and avoid
specifying the path to the sound each time you use a different sound than the
default one set in KNotification (if you choose to set a default sound).

# KNotification

Used to create a notification object where you can set default settings,
though you can always specify the details of the notification explicitly for
each dispatch. You can also create different notification objects, for
example, one for errors and another for informational messages, allowing you
to define different default details for each.

# More Credits (All License: Creative Commons 0)

- **Notification Sound** (yfjesse): [Freesound Link](https://freesound.org/people/yfjesse/sounds/235911/)
- **Error.wav** (Isaac200000): [Freesound Link](https://freesound.org/people/Isaac200000/sounds/188013/)
- **SeriousError01f.aif** (Kuru23): [Freesound Link](https://freesound.org/people/Kuru23/sounds/145287/)
- **Notification Image**: [Openverse](https://openverse.org/image/953731c5-25c6-43d5-910c-36f4200d4925?q=information)
- **Error Image**: [Openverse](https://openverse.org/image/eb77d859-8cf7-45ce-aaf3-00d2067882bc?q=error.png)
"""

from .src.knotification import KNotifySound, KNotification
