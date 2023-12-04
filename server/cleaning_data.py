from sound_to_text_converter import call_converter
sample_data = "Hello World right".split()
needed_inputs = [
    'right',
    'left',
    'forward',
    'back',
    'stop',
    'break'
]
def command_func():
    command = call_converter().split()
    for name in needed_inputs:
        if name in command:
            print(f"Comand: {name}")
            return name
        else:
            continue