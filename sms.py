# This is pyserial which is needed to communicate with the dongle
# coding=utf-8
import serial
import io
import binascii
# Set up the connection to the dongle
dongle = serial.Serial(port="/dev/tty.HUAWEIMobile-Modem",baudrate=115200,timeout=2,rtscts=0,xonxoff=0)
# sio = io.TextIOWrapper(io.BufferedRWPair(dongle, dongle))
print "Connected!"
def getResponse():
    sb = []
    sb.append(dongle.read())
    sb.append(dongle.read(dongle.inWaiting()))
    return ''.join(sb)


# This sends the command to the dongle
# put the dongle into text mode
dongle.write('ATE0\r')
print getResponse()
# dongle.write('AT+CMGF?\r')
# print getResponse()
# read()
# time.sleep(0.5)
# dongle.flush()
# sio.write(unicode("AT\n"))
# sio.flush()
# print sio.readline()

#dongle.write('\r\r\rAT Z\r')
#print getResponse()

dongle.write('AT+CMGF=1\r')
print getResponse()

# dongle.write('AT+CSCS=?\r')
# print getResponse()

# dongle.write('AT+CSCS="USC2"')
# print getResponse()

# print 'Number = ' + binascii.hexlify('0739332499'.encode('utf16'))

# Set the telephone number we want to send to
dongle.write('AT+CMGS="' + '0739332499' + '"\r')
print getResponse()

# print 
 
#### Set the message we want to send
try:
    dongle.write('Hej Pjeksa!')
except:
 	print "Unexpected error"

# Pass the CTRL+Z character to let the dongle know we're done
dongle.write(chr(26))
print getResponse()
# Close the connection
dongle.close()