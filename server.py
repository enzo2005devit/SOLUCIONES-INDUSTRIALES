from pyModbusTCP.server import ModbusServer, DataBank
from datetime import datetime


class MyDataBank(DataBank):
    """A custom ModbusServerDataBank for override get_holding_registers method."""

    def __init__(self):
        # turn off allocation of memory for standard modbus object types
        # only "holding registers" space will be replaced by dynamic build values.
        super().__init__(virtual_mode=True)


    def get_holding_registers(self, address, number=1, srv_info=None):
        """Get virtual holding registers."""
        # populate virtual registers dict with current datetime values
        now = datetime.now()
        v_regs_d = {0: now.day, 1: now.month, 2: now.year,
                    3: now.hour, 4: now.minute, 5: now.second}
        # build a list of virtual regs to return to server data handler
        # return None if any of virtual registers is missing
        try:
            return [v_regs_d[a] for a in range(address, address+number)]
        except KeyError:
            return
        
        
    def set_holding_registers(self, address, values, srv_info=None):
        """Set virtual holding registers."""
        # Handle the writing of values to holding registers
        try:
            for i, value in enumerate(values):
                self.write_register(2,15)
        except Exception as e:
            print(f"Error writing to holding registers: {e}")

        return True

Var = 0
xd = 0

server = ModbusServer(host='192.168.1.130', port=502, no_block=True, data_bank=MyDataBank())#, data_bank=MyDataBank())

try:
    while(Var == 0):
       print(MyDataBank.get_holding_registers(2,15))
       if(xd == 0):
        print('starting')
        server.start()
        print('is online')
        xd = 1

        
except Exception as algo:
    print('Unexpected error:')
    print(algo)
        
    
    