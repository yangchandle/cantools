#!/usr/bin/env python3
#

from __future__ import print_function

from cantools.db import Database
from cantools.db import Message
from cantools.db import Signal
from cantools.db.formats.dbc import AttributeDefinition
from cantools.db.formats.dbc import Attribute


# Create a general database with one message.
signal = Signal(name='TheSignal',
                start=0,
                length=8,
                receivers=['Vector__XXX'],
                byte_order='big_endian',
                scale=1.0,
                offset=10,
                minimum=10.0,
                maximum=100.0,
                unit='m/s')

message = Message(frame_id=37,
                  name='TheMessage',
                  length=8,
                  senders=['Vector__XXX'],
                  signals=[signal],
                  send_type='cyclic',
                  cycle_time=1000,
                  comment='')

database = Database(messages=[message])

# Add DBC specific data.
message.dbc.attributes = [
    Attribute('TheHexAttribute', 5),
    Attribute('TheFloatAttribute', 58)
]

attribute_definitions = [
    AttributeDefinition('TheHexAttribute', 'HEX', (0, 8), 4),
    AttributeDefinition('TheFloatAttribute', 'FLOAT', (5, 87), 55),
    AttributeDefinition('TheNodeAttribute', 'INT', (50, 150), 100),
    AttributeDefinition('NodeLayerModules',
                        'STRING',
                        default='CANoeILNLVector.dll'),
    AttributeDefinition('GenMsgStartDelayTime', 'INT', (0, 65535), 0),
    AttributeDefinition('NWM-WakeupAllowed', 'ENUM',  ['No','Yes']),
    AttributeDefinition('NmMessage', 'ENUM', ['no','yes'], 'no'),
    AttributeDefinition('GenMsgILSupport', 'ENUM', ['No', 'Yes'], 'Yes'),
    AttributeDefinition('NmNode', 'ENUM', ['no', 'yes'], 'no'),
    AttributeDefinition('NmStationAddress', 'INT', (0, 63)),
    AttributeDefinition('NmBaseAddress', 'HEX', (1024, 1087), 1024),
    AttributeDefinition('GenMsgCycleTimeFast', 'INT', (0, 50000), 0),
    AttributeDefinition('BusType', 'STRING'),
    AttributeDefinition('GenMsgCycleTime', 'INT', (0, 50000), 0),
    AttributeDefinition('GenMsgDelayTime', 'INT', (0, 1000), 0),
    AttributeDefinition('GenMsgNrOfRepetition', 'INT', (0, 999999), 0),
    AttributeDefinition('GenMsgSendType',
                        'ENUM',
                        ['Cyclic', 'NotUsed', 'NotUsed', 'NotUsed', 'NotUsed',
                         'NotUsed', 'NotUsed', 'IfActive', 'NoMsgSendType',
                         'NotUsed', 'vector_leerstring'],
                        'NoMsgSendType'),
    AttributeDefinition('GenSigInactiveValue', 'INT', (0, 100000), 0),
    AttributeDefinition('GenSigSendType',
                        'ENUM',
                        ['Cyclic', 'OnWrite', 'OnWriteWithRepetition', 'OnChange',
                         'OnChangeWithRepetition', 'IfActive',
                         'IfActiveWithRepetition', 'NoSigSendType', 'NotUsed',
                         'NotUsed', 'NotUsed', 'NotUsed', 'NotUsed'],
                        'Cyclic'),
    AttributeDefinition('GenSigStartValue', 'FLOAT', (0, 100000000000), 0),
]

database.dbc.attribute_definitions = attribute_definitions

# Access an attribute definition.
print(database.dbc.get_attribute_definition('NmMessage'))

# Access a message attribute.
print(message.dbc.get_attribute('TheHexAttribute'))

# Print the database in the DBC file format.
print(database.as_dbc_string())
