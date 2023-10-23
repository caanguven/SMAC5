from lewansoul_servo_bus import ServoBus
from time import sleep 

#my_serial = serial.Serial(port='/dev/cu.usbserial-0001', baudrate=115200, timeout=1.0)
servo_bus = ServoBus('/dev/cu.usbserial-0001')


#servo_bus.move_time_write(1, 90, 1.0)
# servo_1 = servo_bus.get_servo(1)
# servo_1.move_time_write(180, 2)
#servo_1 = servo_bus.id_write(2,10)



servo_1 = servo_bus.get_servo(10)
servo_1.move_speed_write(180,120,True)
# servo_1.move_time_write(180, 2)

#error = False
# errors = 0

# sleep(2)
# servo_bus.serial_conn.reset_input_buffer()
sleep(0.05)  # sleep for 50 milliseconds

# degrees = servo_1.pos_read()
sleep(0.05)  # sleep for 50 milliseconds

# print(degrees)
#try:
     
#except Exception as e:
        #print(f'Error: {e}')
        #error = True
        #errors += 1

