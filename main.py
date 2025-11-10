import json
import threading
import queue
import time
from pathlib import Path

import rtmidi
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pydbus import SessionBus

###############################################################################
#
# CONFIGURATION
#
CONFIG_PATH = Path.cwd().joinpath('config.json')


midi_event_queue = queue.Queue()

mapping = {}

bus = SessionBus()

###############################################################################
#
# MIDI CALLBACK
#
def midi_callback(message, data):
    """Will process midi messages"""


###############################################################################
#
# DISPATCHER
#
def dispatcher():
    """Will coordinate everyone"""

def handler():
    """Will transmit data to pipewire"""


###############################################################################
#
# CONFIG WATCHER
#
class ConfigHandler(FileSystemEventHandler):
    def __init__(self, config_path):
        self.config_path = Path(config_path)

    def on_modified(self, event):
        if Path(event.src_path) == self.config_path:
            load_config()

def load_config():
    """Will load the config file"""


###############################################################################
#
# MAIN I GUESS
#
def main():
    """Startup"""

if __name__ == "__main__":
    main()
