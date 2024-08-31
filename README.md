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

- **Notification Sound** (yfjesse): [Freesound Link](https://freesound.org/people/yfjess
  e/sounds/235911/) (Creative Commons 0)
  _I decreased the volume a bit to 0.65._

- **Discrete Error** (distillerystudio): [Freesound Link](https://freesound.org/people/d
  istillerystudio/sounds/327737/) (Attribution 3.0)  
  _I decreased the volume a bit to 0.80._

# Sample Sounds

You can use the sample sounds

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
There are two classes: KNotifySound, KNotification
```
