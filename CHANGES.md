# 0.1.0.2

We had to remove support for adjusting the sound volume in notifications for both
PygameSound and KNotification, as well as the stop() function in PygameSound
due to pygame's planned removal of these features.

https://github.com/pygame/pygame/blob/dc69e5d027b392aeca47ee01bc3cfbf9ee1d5bfa/buildconfig/stubs/pygame/mixer.pyi#L59

This means that at any moment, that update could happen, forcing me to impose a
specific version of pygame in order to continue using KNotification while I find
an alternative.

However, this does not prevent these or similar features from being re-incorporated
in the future.

Thanks.
