from abc import ABC, abstractmethod
from enum import Enum

class ACTIONS(Enum):
    TURN_ON = "turn_on"
    TURN_OFF = "turn_off"

# Receiver
class Light:
    def __init__(self):
        self._state = "off"

    def turn_on(self):
        self._state = "on"
        print(" > Light is ON")

    def turn_off(self):
        self._state = "off"
        print(" > Light is OFF")


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()


# Concrete Command
class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

# Another Concrete Command
class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light
    
    def execute(self) -> None:
        self._light.turn_off()

# Invoker
# Alternative1: the commands are explicitly specified as arguments,
# so they need to be set before execution
class RemoteControl():
    def __init__(self):
        self._command = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def press_button(self) -> None:
        if self._command:
            self._command.execute()


# Invoker
# Alternative2: the commands are predefined inside the invoker,
# so the caller only specified which one to execute by an identifier
class AnotherRemoteControl():
    def __init__(self, receiverLight: Light):
        self._commands = {
            ACTIONS.TURN_ON.value: TurnOnCommand(receiverLight),
            ACTIONS.TURN_OFF.value: TurnOffCommand(receiverLight),
        }

    def press_button(self, which_button: str) -> None:
        command = self._commands.get(which_button, None)

        if not command:
            print(f" > Button {which_button} not found.")
        
        command.execute()


# Caller
if __name__ == "__main__":

    a_light = Light()

    # Example - Alternative1
    remote_control = RemoteControl()

    turn_on_command = TurnOnCommand(a_light)
    turn_off_command = TurnOffCommand(a_light)

    remote_control.set_command(turn_on_command)
    remote_control.press_button()
    remote_control.set_command(turn_off_command)
    remote_control.press_button()
    
    # Example - Alternative2
    another_light = Light()

    another_remote_control = AnotherRemoteControl(another_light)
    another_remote_control.press_button(ACTIONS.TURN_ON.value)
    another_remote_control.press_button(ACTIONS.TURN_OFF.value)