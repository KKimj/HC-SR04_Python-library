from serial import Serial

class importClass:
    def test(self):
        print('Hello')

class _SerialDevice:
    def __init__(self, port, baudrate, timeout = 3, open = False):
        '''
        init method
        if open is set True then call open_serial()
        '''
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None
        if open:
            self.open_serial()

    def set_port(self, port, open = False):
        '''
        set port method
        if serial is opened then Close serial
        if open is set True then call open_serial()
        '''
        if not self.serial:
            self.close_serial()
        self.port = port
        if open:
            self.open_serial()
    
    def open_serial(self):
        if not self.serial:
            self.close_serial()
        try:
            self.serial = Serial(self.port, self.baudrate, self.timeout)
        except:
            print('Error : Can not open Serial, Retry!')

    def close_serial(self):
        if self.serial:
            self.serial.close()
        self.serial = None

    def write(self, message):
        if self.serial:
            if type(message) is not str:
                message = str(message)
            self.serial.write(bytes(message.encode()))
    
    def readline(self):
        if self.serial:
            return self.serial.readline().decode('utf-8').strip()

    def test(self):
        '''
        Print out status
        '''
        if self:
            if self.serial:
                print('Serial is opened')
            else:
                print('Serial is not opened')
            if self.port:
                print('Port : %s'%(self.port))
            if self.baudrate:
                print('Baudrate : %s'%(self.baudrate))
            if self.timeout:
                print('Timeout : %s'%(self.timeout))
