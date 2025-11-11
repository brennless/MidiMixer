# main.py
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


"""sinks_raw = pulse.sink_list()
sink_inputs_raw = pulse.sink_input_list()
sources_raw = pulse.source_list()
source_outputs_raw = pulse.source_output_list()
cards_raw = pulse.card_list()"""

###############################################################################
#
# MIDI CALLBACK
#
def midi_callback(message, device):
    """Will process midi messages"""
    msg = (message, device)
    midi_event_queue.put(msg)

def midi_handler():
    while True:
        try:
            msg = midi_event_queue.get(timeout=1)
            status, cc, velocity = msg[0][0]
            channel = status & 0x0F
            command = status & 0xF0
            print(f"Device:{msg[1]} ", end="")
            if command == 176:
                print(f"Knob {cc} to {velocity}")
            elif command == 128:
                print(f"Unmute {cc}")
            elif command == 144:
                print(f"Mute {cc}")
        except queue.Empty:
            continue


###############################################################################
#
# DISPATCHER
#
def dispatcher(pulse):
    """Will coordinate everyone"""



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

    config_handler = ConfigHandler(CONFIG_PATH)
    observer = Observer()
    observer.schedule(config_handler, CONFIG_PATH, recursive=False)
    observer.start()

    with pulsectl.Pulse('MidiMixer') as pulse:
        
        # Dispatcher
        dispatcher_thread = threading.Thread(target=dispatcher, args=(pulse,), daemon=True)
        dispatcher_thread.start()
        

        # Midi
        midi_inputs = []
        ports = rtmidi.MidiIn().get_ports()

        for i, name in enumerate(ports):
            midi_in = rtmidi.MidiIn()
            midi_in.open_port(i)
            midi_in.set_callback(midi_callback)
            midi_inputs.append(midi_in)
            print(f"[MIDI] Opened input: {name}") 
        midi_in.set_callback(lambda message, data, device=name: midi_callback(message, device))
        midi_thread = threading.Thread(target=midi_handler, daemon=True)
        midi_thread.start()


        while True:
            """"""

if __name__ == "__main__":
    main()
