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
pip install py-notifier
pip install pygame
# Windows
    pip install WinToaster

# Linux (no pip, requires manual install)
ArchLinux: sudo pacman -S libnotify
Debian : sudo apt-get install libnotify-bin

Usage:
There are two classes: KNotifySound, KNotification
```

# Sample Usage
``````

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
- **Notification Image**: https://openverse.org/image/953731c5-25c6-43d5-910c-36f4200d4925?q=information 
- **Error Image**: https://openverse.org/image/eb77d859-8cf7-45ce-aaf3-00d2067882bc?q=error.png
"""

from .src.knotification import KNotifySound, KNotification
