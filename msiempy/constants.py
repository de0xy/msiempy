# -*- coding: utf-8 -*-
""" 
    msiem constants
"""
POSSIBLE_FIELD_TYPES = [ 'BOOLEAN',
            'STRING',
            'CUSTOM',
            'INT2',
            'INT4',
            'INT8',
            'INT32',
            'INT64',
            'UINT8',
            'UINT16',
            'UINT32',
            'UINT64',
            'IPV4',
            'FLOAT',
            'SIGID',
            'SSTRING',
            'IPTYPE',
            'IP',
            'GUID',
            'MAC_ADDRESS',
            'LONG_CUSTOM',
            'HSTRING',
            'STRLIT',
            'AGG',
            'TIME4',
            'TIME8']

POSSIBLE_ALARM_STATUS=[
        ('acknowledged', 'ack',),
        ('unacknowledged', 'unack',),
        ('', None, 'all', 'both')
    ]

ALARM_FILTER_FIELDS = [('id',),
('summary','sum'),
('assignee','user'),
('severity','sever'),
('triggeredDate','trigdate'),
('acknowledgedDate','ackdate'),
('acknowledgedUsername','ackuser'),
('alarmName','name'),
]

ALARM_EVENT_FILTER_FIELDS=[("eventId",),
#"severity", duplicated in ALARM_FILTER_FIELD
#("severity", "eventseverity",),
("ruleMessage",'msg','rulemsg'),
("eventCount",'count'),
("sourceIp",'srcip'),
("destIp",'dstip'),
("protocol",'prot'),
("lastTime",'date'),
("eventSubType",'subtype')]

ALARM_DEFAULT_FIELDS=['triggeredDate','alarmName','status','sourceIp','destIp','ruleMessage']