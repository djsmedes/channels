from django.apps import AppConfig


class ChannelsConfig(AppConfig):

    name = "channels"
    verbose_name = "Channels"

    def ready(self):
        try:
            import daphne.server
        except:
            pass
        else:
            assert daphne.server
            # Do django monkeypatches
            from .hacks import monkeypatch_django

            monkeypatch_django()
