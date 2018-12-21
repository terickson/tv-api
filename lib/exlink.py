import time
import serial
from serial.tools import list_ports


class ExLink():
    def __init__(self, port, type):
        self.ser = serial.Serial(port, baudrate=9600, bytesize=8, timeout=3)
        self.type = type

    def ListPorts(self):
        ports = list_ports.comports()
        for port in ports:
            print port

    def SetPort(self, port):
        self.ser.port = port
        self.ser.open()

    def crc(self, command):
        crc = 0x100
        for char in command:
            crc -= char
        return crc

    def PowerOff(self):
        self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0xd5])

    def PowerOn(self):
        if self.type == 'old':
            self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x02, 0xd6])
        else:
            self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x02, 0xd4])

    def PowerToggle(self):
        if self.type == 'old':
            self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x02, 0xd6])
        else:
            self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x02, 0xd4])

    def Volume(self, volume):
        if volume < 0 or volume > 100:
            print "Volume must be within the range of 0-100"
            return
        cmd = [0x08, 0x22, 0x01, 0x00, 0x00, volume]
        cmd.append(self.crc(cmd))
        self.ser.write(cmd)

    def Channel(self, channel):
        if channel < 0 or channel > 255:
            print "Channel must be within the range of 0-255"
            return
        cmd = [0x08, 0x22, 0x04, 0x00, 0x00, channel]
        cmd.append(self.crc(cmd))
        self.ser.write(cmd)

    def VolumeUp(self):
        self.ser.write([0x08, 0x22, 0x01, 0x00, 0x01, 0x00, 0xd4])

    def VolumeDown(self):
        self.ser.write([0x08, 0x22, 0x01, 0x00, 0x02, 0x00, 0xd3])

    def Mute(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x02, 0x00, 0x00, 0x00, 0xd4])

    def ChannelUp(self):
        self.ser.write([0x08, 0x22, 0x03, 0x00, 0x01, 0x00, 0xd2])

    def ChannelDown(self):
        self.ser.write([0x08, 0x22, 0x03, 0x00, 0x02, 0x00, 0xd1])

    def PreviousChannel(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x13, 0xB6])

    def InputTV(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x00, 0x00, 0xcc])

    def InputAV1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x00, 0xcb])

    def InputAV2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x01, 0xca])

    def InputAV3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x02, 0xc9])

    def InputSVideo1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xca])

    def InputSVideo2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xc9])

    def InputSVideo3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xc8])

    def InputComponent1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc9])

    def InputComponent2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc8])

    def InputComponent3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc7])

    def InputPC1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc8])

    def InputPC2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc7])

    def InputPC3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc6])

    def DVI1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc6])

    def DVI2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc5])

    def DVI3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc4])

    def HDMI1(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x00, 0xc7])

    def HDMI2(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x01, 0xc6])

    def HDMI3(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x02, 0xc5])

    def HDMI4(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x03, 0xc4])

    def Netflix(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0xF3, 0xD6])

    def Amazon(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0xF4, 0xD5])

    def Size169(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x00, 0xc0])

    def SizeZoom1(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x01, 0xbf])

    def SizeZoom2(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x02, 0xbe])

    def SizeWideFit(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x03, 0xbd])

    def Size43(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x04, 0xbc])

    def SizeScreenFit(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x05, 0xbb])

    def SizeSmartView1(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x06, 0xba])

    def SizeSmartView2(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x07, 0xb9])

    def ResetPicture(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0b, 0x00, 0x070, 0xc0])

    def Enter(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x68, 0x61])

    def Up(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x60, 0x69])

    def Down(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x61, 0x68])

    def Right(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x62, 0x67])

    def Left(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x65, 0x64])

    def Play(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x47, 0x82])

    def Pause(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x4A, 0x7F])

    def Stop(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x46, 0x83])

    def Rewind(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x45, 0x84])

    def FastForward(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x48, 0x81])

    def SkipBack(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x50, 0x79])

    def SkipForward(self):
        self.ser.write([0x08, 0x22, 0x0d, 0x00, 0x00, 0x4E, 0x7B])

    def Test(self):
        print "PowerOn"
        self.PowerOn()
        time.sleep(5)

        print "VolumeUp"
        self.VolumeUp()
        time.sleep(2)

        print "VolumeDown"
        self.VolumeDown()
        time.sleep(2)

        print "Mute"
        self.Mute()
        time.sleep(2)

        print "Volume(25)"
        self.Volume(25)
        time.sleep(2)

        print "InputTV"
        self.InputTV()
        time.sleep(3)

        print "ChannelUp"
        self.ChannelUp()
        time.sleep(3)

        print "ChannelDown"
        self.ChannelDown()
        time.sleep(3)

        print "HDMI1"
        self.HDMI1()
        time.sleep(3)

        print "HDMI2"
        self.HDMI2()
        time.sleep(3)

        print "HDMI3"
        self.HDMI3()
        time.sleep(3)

        print "HDMI4"
        self.HDMI4()
        time.sleep(3)

        print "Zoom1"
        self.SizeZoom1()
        time.sleep(2)

        print "16:9"
        self.Size169()
        time.sleep(2)

        print "Smart View I"
        self.SizeSmartView1()
        time.sleep(2)

        print "Smart View II"
        self.SizeSmartView2()
        time.sleep(2)

        print "Screen Fit"
        self.SizeScreenFit()
        time.sleep(2)

        print "ResetPicture"
        self.ResetPicture()
        time.sleep(2)

        print "HDMI1"
        self.HDMI1()
        time.sleep(3)

        print "PowerOff"
        self.PowerOff()
        time.sleep(5)

        print "PowerToggle"
        self.PowerToggle()
        time.sleep(5)
