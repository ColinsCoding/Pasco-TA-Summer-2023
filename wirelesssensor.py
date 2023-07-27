from pasco import PASCOBLEDevice
from pasco import CodeNodeDevice, Icons
import pandas as pd
import time

# my_sensor = PASCOBLEDevice()
# found_devices = my_sensor.scan()



# print('\nDevices Found')
# for i, ble_device in enumerate(found_devices):
#     display_name = ble_device.name.split('>')
#     print(f'{i}: {display_name[0]}')

# # Auto connect if only one sensor found
# selected_device = input('Select a device: ') if len(found_devices) > 1 else 0
# ble_device = found_devices[int(selected_device)]

# my_sensor.connect(ble_device)

# # get sensor info 
# measurement_list = my_sensor.get_measurement_list()
# print(measurement_list)

# sensor_list = my_sensor.get_sensor_list()
# print(sensor_list)

# #sensor_info = my_sensor.get_sensor_info()
# #print(sensor_info)



# # Loop that will read/display the data 100 times
# for i in range(100):
#     current_position = my_sensor.read_data('Position')
#     print(f'The current distance is {current_position}')
    

# my_sensor.disconnect()

# create data frame 
motionsensor_df = pd.DataFrame(columns=['Time', 'Position', 'Velocity', 'Acceleration'])

def main():
    
    my_sensor = PASCOBLEDevice()
    
    try:
        found_devices = my_sensor.scan()

        print('\nDevices Found')
        for _, ble_device in enumerate(found_devices):
            display_name = ble_device.name.split('>')
            print(f'{_}: {display_name[0]}')

        # Auto connect if only one sensor found
        selected_device = input('Select a device: ') if len(found_devices) > 1 else 0
        ble_device = found_devices[int(selected_device)]

        my_sensor.connect(ble_device)
    except:
        my_sensor.connect_by_id("232-435")

    #my_sensor.TIME_DELAY = 5
    measurements = (my_sensor.get_measurement_list())

    for i in range(100):
        for m in measurements:
            print(f'{m} : {my_sensor.read_data(m)}')

            # store individual data points in motionsensor_df, the motion sensor data frame
            if m == 'Time':
                motionsensor_df.loc[i, 'Time'] = my_sensor.read_data(m)
            elif m == 'Position':
                motionsensor_df.loc[i, 'Position'] = my_sensor.read_data(m)
            elif m == 'Velocity':
                motionsensor_df.loc[i, 'Velocity'] = my_sensor.read_data(m)
            elif m == 'Acceleration':
                motionsensor_df.loc[i, 'Acceleration'] = my_sensor.read_data(m)
            else:
                print('Error: no measurement found')
        
        #time.sleep(.5)

    print(motionsensor_df)

    my_sensor.disconnect()




if __name__ == "__main__":
    main()