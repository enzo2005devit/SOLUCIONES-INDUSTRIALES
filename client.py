from pyModbusTCP.client import ModbusClient
import time

# Create a Modbus client
client = ModbusClient(host="192.168.1.130", port=502)


while True:
   if client.open():
    print("Connected to Modbus server")
    # read 10 registers at address 0, store result in regs list
    success = client.read_holding_registers(2)

    if success:
        xd = client.write_single_register(2,15)
        print(f" valor {xd}")
    else:
        print("Failed to write value") 
   # sleep 2s before next polling
time.sleep(2)