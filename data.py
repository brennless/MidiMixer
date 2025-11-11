# data.py
import json
import rtmidi
import pulsectl

###############################################################################
#
# DATA JSON
#
def list_to_dict(l):
    res = {}
    for e in l:
        res[e.name] = e.index
    return res


def update_data():
    
    with pulsectl.Pulse('Updater') as pulse:
        sinks_raw = pulse.sink_list()
        sink_inputs_raw = pulse.sink_input_list()
        sources_raw = pulse.source_list()
        source_outputs_raw = pulse.source_output_list()
        cards_raw = pulse.card_list()

        midi_in = rtmidi.MidiIn()
        in_ports_raw = midi_in.get_ports()

        sinks = list_to_dict(sinks_raw)
        sources = list_to_dict(sources_raw)
        sink_inputs = list_to_dict(sink_inputs_raw)
        source_outputs = list_to_dict(source_outputs_raw)
        in_ports = {}
        for i, m in enumerate(in_ports_raw):
            in_ports[m] = i

        data = {
                "output_devices":sinks,
                "input_devices":sources, 
                "playback":sink_inputs,
                "record":source_outputs,
                "midi_in":in_ports
                }

        json_data = json.dumps(data, indent=4)
        print(json_data)
        with open("data.json", "w") as f:
            f.write(json_data)
