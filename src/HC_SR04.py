from serial import Serial

class HC_SR04:
    def __init__(self, channel = 1, direction = "left", port = '/dev/ttyUSB0'):
        self.channel = channel
        self.port = port
        self.direction = direction
    
    def setSerialPort(self, port):
        '''
        Setter to Serial-port
        '''
        self.port = port

    def OpenSerial(self):
        '''
        Open Serial connection
        '''
        self.serial =  Serial(self.port, 115200, timeout = 3)
    
    def CloseSerial(self):
        '''
        Close Serial connection
        '''
        self.serial.close()

    def getData(self, separator=' '):
        '''
        Getter to data from serial
        Must call OpenSerial() before to use this method
        '''
        return list(map(int, self.serial.readline().decode('utf-8').strip().split(separator)))

    def Test(self):
        '''
        Print out Sensors data
        '''
        print('Test method of HC_SR04 Class')
        if self:
            if self.port:
                print('Port : %s'%(self.port))
            if self.channel:
                print('Channel : %s'%(self.channel))
            if self.direction:
                print('Direction : %s'%(self.port))

class HC_SR04_fair:
    def __init__(self, channel = 1, port_left = '/dev/ttyUSB0', port_right = '/dev/ttyUSB1'):
        '''
        left : Left Sensors
        right : Right Sensors
        '''
        self.channel = channel
        self.left = HC_SR04(self.channel, direction="left", port = port_left)
        self.right = HC_SR04(self.channel, direction="right", port = port_right)
    
    def setSerialPort(self, port_left, port_right):
        self.left.CloseSerial()
        self.right.CloseSerial()
        
        self.left = HC_SR04(self.channel, direction="left", port = port_left)
        self.right = HC_SR04(self.channel, direction="right", port = port_right)


    def OpenSerial(self):
        self.left.OpenSerial()
        self.right.OpenSerial()
    
    def CloseSerial(self):
        self.left.CloseSerial()
        self.right.CloseSerial()
    
    def Switch(self):
        '''
        Swtich left to right, right to left
        '''
        tmp = self.left
        self.left = self.right
        self.right = tmp       
    
    def getData(self, separator=' '):
        return self.left.getData() + self.right.getData()

    def getLeftSensors(self):
        return self.left.getData()
    
    def getRightSensors(self):
        return self.right.getData()
    
    def getFront(self):
        '''
        Front Sensor are 1, 2, 3 ...
        '''
        return self.left.getData()[:self.channel//2]+ self.right.getData()[:self.channel//2]
    
    def getLeftside(self):
        '''
        Side sensors are ... 5 6 7 8
        '''
        return self.left.getData()[self.channel//2:]
    
    def getRightside(self):
        return self.right.getData()[self.channel//2:]
    
    
    def Test(self):
        '''
        Print out Sensors data
        '''
        print('Test method of HC_SR04_fair')
        if self.left:
            self.left.Test()
        if self.right:
            self.right.Test()
        
class HC_SR04_quad:
    leftPort = '/dev/ttyUSB0'
    rightPort = '/dev/ttyUSB1'
    
    left_sensors = None
    right_sensors = None
    

    @staticmethod
    def setSerialPort(leftPort = '/dev/ttyUSB0', rightPort = '/dev/ttyUSB1'):
        HC_SR04_quad.CloseSerial()

        HC_SR04_quad.leftPort = leftPort
        HC_SR04_quad.rightPort = rightPort

        HC_SR04_quad.OpenSerial()
                    
    @staticmethod
    def OpenSerial():
        HC_SR04_quad.left_sensors = Serial(HC_SR04_quad.leftPort, 115200, timeout = 3)
        HC_SR04_quad.right_sensors = Serial(HC_SR04_quad.rightPort, 115200, timeout = 3)
    
    @staticmethod
    def CloseSerial():
        HC_SR04_quad.left_sensors.close()
        HC_SR04_quad.right_sensors.close()

    @staticmethod
    def Switch():
        HC_SR04_quad.setSerialPort(leftPort=HC_SR04_quad.rightPort, rightPort=HC_SR04_quad.leftPort)
    
        
    @staticmethod
    def getLeftSensors():
        return list(map(int, HC_SR04_quad.left_sensors.readline().decode('utf-8').strip().split()))

    @staticmethod
    def getRightSensors():
        return list(map(int, HC_SR04_quad.right_sensors.readline().decode('utf-8').strip().split()))
        
    @staticmethod
    def getFront():
        return HC_SR04_quad.getLeftSensors()[:2] + HC_SR04_quad.getRightSensors()[:2]
    
    @staticmethod
    def getLeftside():
        return HC_SR04_quad.getLeftSensors()[2:]
    
    @staticmethod
    def getRightside():
        return HC_SR04_quad.getRightSensors()[2:]
    
    @staticmethod
    def getTotalData():
        return HC_SR04_quad.getLeftSensors() + HC_SR04_quad.getRightSensors()
