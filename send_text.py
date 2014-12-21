# This is pyserial which is needed to communicate with the dongle
import serial
import io
import binascii
import sys

port =    sys.argv[1] # /dev/tty.HUAWEIMobile-Modem
number =  sys.argv[2] # +46708123456
message = sys.argv[3] # 'Hi phone!'

# Make sure the message is ASCII friendly. Throws error if not.
message.decode('ascii')

# Set up the connection to the dongle
dongle = serial.Serial(port=port,baudrate=115200,timeout=2,rtscts=0,xonxoff=0)

print "Connected!"

# Wait for response. Must be called after each execution that returns an answer.
def getResponse():
    sb = []
    sb.append(dongle.read())
    sb.append(dongle.read(dongle.inWaiting()))
    return ''.join(sb)


# Tell dongle not to echo back commands.
dongle.write('ATE0\r')
print getResponse()

# Put dongle in text mode
dongle.write('AT+CMGF=1\r')
print getResponse()

# Set the telephone number we want to send to
dongle.write('AT+CMGS="' + number + '"\r')
print getResponse()

#### Set the message we want to send
try:
    dongle.write(message)
except:
 	print "Unexpected error"

# Pass the CTRL+Z character to let the dongle know we're done
dongle.write(chr(26))
print getResponse()

# Close the connection
dongle.close()