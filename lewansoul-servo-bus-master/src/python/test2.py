from lewansoul_servo_bus import ServoBus
from time import sleep 

servo_bus = ServoBus('/dev/cu.usbs erial-0001')

#servo_bus.move_time_write(1, 90, 1.0)
servo_1 = servo_bus.get_servo(10)
servo_1.move_time_write(100, 2)

sleep(2)

pose = servo_1.pos_read()
print(pose)

# Move servo with ID 2 to 180 degrees in 2.0 seconds
# servo_2 = servo_bus.get_servo(2)
# servo_2.move_time_write(180, 2)
