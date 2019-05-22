import minimalmodbus
import serial
import postgresql
import datetime,time

port = '/dev/ttyUSB0' # serial port
x = 0 #Температура
z = 0
start = True
vla = 0 #Влажность
slave_adress = 16 # 10cc
## Number of the first register 0x0102 16cc or 258 10cc ##
dec_name_number = 100
register_number = dec_name_number
number_of_decimals = 2 # temperature value from -4000 to +12000 C
baudrate = 19200 # from datasheet
bytesize = 8 # from datasheet
stopbits = 1 # from datasheet
timeout = 1 # where to get it from?

while start==True:
    
    print("starting version 1.1.6...")
    try:
        minimalmodbus.BAUDRATE = baudrate
        minimalmodbus.TIMEOUT = timeout
        instrument = minimalmodbus.Instrument(port, slave_adress, mode='rtu')
        
        #instrument.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
        x = instrument.read_register(register_number, numberOfDecimals=0, functioncode=3, signed=True)
        print(list("{0:b}".format(x)))
        instrument.debug = False
        instrument.close_port_after_each_call=True
        time.sleep(5)
    except:
        print('Error comunication mode')
        time.sleep(25)
        z = z + 1
        if z > 5 :
            exit(0)
        
    
    
	#db = postgresql.open('pq://postgres:postgres@172.16.100.87:5432/ok_sreda')
	#update = db.prepare("UPDATE up_contr_cur SET udtm=$1, co2=$2, n2=$3 WHERE id_up_contr_inf=3")
	#update(round(time.time()),x,vla)
	#print(round(time.time()))
