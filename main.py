import json
import threading
import queue
import time
from pathlib import Path

import rtmidi

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pulsectl

from data import update_data

###############################################################################
#
# CONFIGURATION
#
CONFIG_PATH = Path.cwd().joinpath('config.json')


midi_event_queue = queue.Queue()

mapping = {}

pulse = pulsectl.Pulse('MidiMixer')

sinks_raw = pulse.sink_list()
sink_inputs_raw = pulse.sink_input_list()
sources_raw = pulse.source_list()
source_outputs_raw = pulse.source_output_list()
cards_raw = pulse.card_list()

midi_in = rtmidi.MidiIn()
in_ports_raw = midi_in.get_ports()

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
        print("File modified")
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
    update_data()

if __name__ == "__main__":
    main()
