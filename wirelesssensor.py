from pasco import PASCOBLEDevice
from pasco import CodeNodeDevice, Icons


my_sensor = PASCOBLEDevice()
found_devices = my_sensor.scan()



print('\nDevices Found')
for i, ble_device in enumerate(found_devices):
    display_name = ble_device.name.split('>')
    print(f'{i}: {display_name[0]}')

# Auto connect if only one sensor found
selected_device = input('Select a device: ') if len(found_devices) > 1 else 0
ble_device = found_devices[int(selected_device)]

my_sensor.connect(ble_device)

# get sensor info 
measurement_list = my_sensor.get_measurement_list()
print(measurement_list)

sensor_list = my_sensor.get_sensor_list()
print(sensor_list)

#sensor_info = my_sensor.get_sensor_info()
#print(sensor_info)



# Loop that will read/display the data 100 times
# for i in range(100):
#     current_temp = my_sensor.read_data('Position')
#     print(f'The current distance is {current_temp}')
#     # 

my_sensor.disconnect()

