import SimulatedGenericI2cController
from numpy import *
import time

#
# Utility function to prepare I2C address byte value
#

def WriteTo(slaveAddr : uint8) -> uint8:
    return slaveAddr << 1

def ReadFrom(slaveAddr : uint8) -> uint8:
    return (slaveAddr << 1) | 0x01

#
# Generic I2C utility functions
#

def prepareSet8bitAddrRegisterPacketHeader(slaveAddr, addrRegisterValue):
    return [WriteTo(slaveAddr), uint8(addrRegisterValue)]

#
# I2C read from a slave device at given address
#
def i2cRead(i2cBus, slaveAddr, bytesToRead):
    i2cBus.send([ReadFrom(slaveAddr)])
    data = i2cBus.receive(bytesToRead)
    return data

#
# 8-bit I2C memory writes
#

def i2c8bitMemoryWrite(i2cBus, slaveAddr, byteAddr, dataToWrite):
    packet = prepareSet8bitAddrRegisterPacketHeader(slaveAddr, byteAddr)
    packet += dataToWrite
    bytesAcked = i2cBus.send(packet)
    if bytesAcked < 2:
        return -1
    else:
        return bytesAcked - 2

def i2c8bitMemoryWriteByte(i2cBus, slaveAddr, byteAddr, byteValue):
    return i2c8bitMemoryWrite(i2cBus, slaveAddr, byteAddr, [uint8(byteValue)])

#
# 8-bit I2C memory reads
#

def i2c8bitMemoryRead(i2cBus, slaveAddr, byteAddr, bytesToRead):
    packet = prepareSet8bitAddrRegisterPacketHeader(slaveAddr, byteAddr)
    bytesAcked = i2cBus.send(packet)
    if bytesAcked != len(packet):
        return []
    else:
        return i2cRead(i2cBus, slaveAddr, bytesToRead)

def i2c8bitMemoryReadByte(i2cBus, slaveAddr, byteAddr):
    return i2c8bitMemoryRead(i2cBus, slaveAddr, byteAddr, 1)[0]

#
# Write to an 8-bit register in 8-bit address space
# (actually the same communication protocol as for an 8-bit I2C RAM with 8-bit words)
#
def i2cWrite8bitRegister(i2cBus, slaveAddr, regAddr, regValue):
    return i2c8bitMemoryWriteByte(i2cBus, slaveAddr, regAddr, regValue)

def i2cRead8bitRegister(i2cBus, slaveAddr, regAddr):
    return i2c8bitMemoryReadByte(i2cBus, slaveAddr, regAddr)

#
# ### MAIN PROGRAM ###
#

# NOTE: Uncomment the following line to enable log messages from inside of the I2C bus and device simulation:
SimulatedGenericI2cController.enableLog = True
i2c = SimulatedGenericI2cController.I2c()

# TODO: Add your implementation here - display two letter text "PJ"

 
i2c.send([0x20 << 1 | 0, 0x06, 0x00])
i2c.send([0x20 << 1 | 0, 0x02, 0x7E])

i2c.send([0x20 << 1 | 0, 0x07, 0x00])
i2c.send([0x20 << 1 | 0, 0x03, 0x1E])

i2c.send([0x21 << 1 | 0, 0x06, 0x00])
i2c.send([0x21 << 1 | 0, 0x02, 0x3C])

i2c.send([0x21 << 1 | 0, 0x07, 0x00])
i2c.send([0x21 << 1 | 0, 0x03, 0x7E])

i2c.send([0x22 << 1 | 0, 0x06, 0x00])
i2c.send([0x22 << 1 | 0, 0x02, 0x5E])

i2c.send([0x22 << 1 | 0, 0x07, 0x00])
i2c.send([0x22 << 1 | 0, 0x03, 0x3E])

i2c.send([0x23 << 1 | 0, 0x06, 0x00])
i2c.send([0x23 << 1 | 0, 0x02, 0x37])

i2c.send([0x23 << 1 | 0, 0x07, 0x00])
i2c.send([0x23 << 1 | 0, 0x03, 0x78])






# NOTE: Program will display "Tcl_AsyncDelete: async handler deleted by the wrong thread" message
# when ending - this is expected behavior. Implementation of display visualization had to be
# simplified in order to have the main program simple enough to be easily readable be programming beginners.
# In order to do that, we are using TkInter knowningly incorrectly (not from the main thread), which results
# in this bug - however it has no influence on the main program behavior.
