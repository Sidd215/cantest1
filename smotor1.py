import can
import time

bus = can.interface.Bus(channel='can0', bustype='socketcan')

def send_motor_cmd(direction, speed):
    """
    direction: 0 = stop, 1 = forward, 2 = reverse
    speed: 0–255
    """
    msg = can.Message(
        arbitration_id=0x100,
        data=[direction, speed],
        is_extended_id=False
    )
    bus.send(msg)

# Examples
send_motor_cmd(1, 200)   # Forward at ~78% speed
time.sleep(3)
send_motor_cmd(2, 128)   # Reverse at 50% speed
time.sleep(3)
send_motor_cmd(0, 0)     # Stop
