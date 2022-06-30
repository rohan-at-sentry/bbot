import atexit
import shutil
import logging
from pathlib import Path
from threading import Lock

from . import misc
from .dns import DNSHelper
from .diff import HttpCompare
from .wordcloud import WordCloud
from ..threadpool import as_completed
from .depsinstaller import DepsInstaller

log = logging.getLogger("bbot.core.helpers")


class ConfigAwareHelper:

    from .web import request, download
    from .command import run, run_live, tempfile, feed_pipe, _feed_pipe
    from .cache import cache_get, cache_put, cache_filename, is_cached
    from . import regexes

    def __init__(self, config, scan=None):
        self.config = config
        self._scan = scan
        self.home = Path(self.config.get("home", "~/.bbot")).expanduser().resolve()
        self.cache_dir = self.home / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir = self.home / "temp"
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.tools_dir = self.home / "tools"
        self.tools_dir.mkdir(parents=True, exist_ok=True)
        atexit.register(self.empty_temp_dir)
        # holds requests CachedSession() objects for duration of scan
        self.cache_sessions = dict()
        self._futures = set()
        self._future_lock = Lock()

        self.dns = DNSHelper(self)
        self.depsinstaller = DepsInstaller(self)
        self.word_cloud = WordCloud(self)

    def http_compare(self, url):

        return HttpCompare(url, self)

    def temp_filename(self):
        """
        temp_filename() --> Path("/home/user/.bbot/temp/pgxml13bov87oqrvjz7a")
        """
        return self.temp_dir / self.rand_string(20)

    def empty_temp_dir(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    @property
    def scan(self):
        if self._scan is None:
            from bbot.scanner import Scanner

            self._scan = Scanner()
        return self._scan

    @staticmethod
    def as_completed(*args, **kwargs):
        return as_completed(*args, **kwargs)

    def __getattribute__(self, attr):
        """
        Allow static functions from .misc to be accessed via ConfigAwareHelper class
        """
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            try:
                return getattr(misc, attr)
            except AttributeError:
                try:
                    return getattr(self.dns, attr)
                except AttributeError:
                    raise AttributeError(f'Helper has no attribute "{attr}"')
