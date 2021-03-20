from serial import Serial

class HC_SR04:
    def __init__(self, channel = 1, direction = "left", port = '/dev/ttyUSB0'):
        self.channel = channel
        self.port = port
        self.direction = direction
    
    def setSerialPort(self, port):
        self.port = port

    def OpenSerial(self):
        self.serial =  Serial(self.port, 115200, timeout = 3)
    
    def CloseSerial(self):
        self.serial.close()

    def getData(self, separator=' '):
        return list(map(int, self.serial.readline().decode('utf-8').strip().split(separator)))

    def Test(self):
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
        self.left = HC_SR04(channel, direction="left", port = port_left)
        self.right = HC_SR04(channel, direction="right", port = port_right)
    
    def OpenSerial(self):
        self.left.OpenSerial()
        self.right.OpenSerial()
    
    def CloseSerial(self):
        self.left.CloseSerial()
        self.right.CloseSerial()
    
    def getData(self, separator=' '):
        pass
    
    def Test(self):
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
        return HC_SR04_quad.getLeftSensors + HC_SR04_quad.getRightSensors
