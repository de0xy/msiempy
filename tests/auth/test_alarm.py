import msiempy
import msiempy.alarm
import unittest
import pprint


class T(unittest.TestCase):


    def test_no_detailed_filter(self):

        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            page_size=5,
            status_filter='unacknowledged')

        alarms.load_data(no_detailed_filter=True)
        
        self.assertEqual(type(alarms), msiempy.alarm.AlarmManager, 'Type error')

        self.assertEqual(len(alarms), 5, 'Alarm list lenght differ from page_size property')

        for alarm in alarms : 

            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            #self.assertEqual(type(alarm['events']), str, 'Type error')
            
            self.assertEqual(alarm['acknowledgedDate'], '', "status_filter is unacknowledged but alarm's acknowledgedDate has a value")
            self.assertEqual(alarm['acknowledgedUsername'], '', "status_filter is unacknowledged but alarm's acknowledgedUsername has a value")
            self.assertEqual(alarm.keys(), alarms.keys, "Alarms's key property is wrong")

        print(alarms)
   
    def test_alarm_filter(self):

        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            filters=[('severity', [80,90])],
            max_query_depth=0,
            page_size=50
            )
            
        alarms.load_data()

        self.assertGreater(51,len(alarms), "The filter don't seem to have filtered any alarm from the list")

        for alarm in alarms :
            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            self.assertEqual(type(alarm['events'][0]), msiempy.event.Event, 'Type error')
            self.assertEqual(type(alarm['events']), msiempy.NitroList, 'Type error')

            self.assertRegex(str(alarm['severity']), '50|80|85|90|95|100', 'Filtering alarms is not working')

        print(alarms.json)
            
    def test_events_filter(self):

        #old way to pass event filters
        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            filters=[('srcIp', ['10','159.33'])],
            max_query_depth=0,
            page_size=50
        )   
        alarms.load_data()

        for alarm in alarms :
            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            self.assertEqual(type(alarm['events'][0]), msiempy.event.Event, 'Type error')
            self.assertRegex(str(alarm['events'][0]['srcIp']), '10|159.33', 'Filtering alarms is not working')

        #new way to pass event filters
        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            filters=[],
            event_filters=[('srcIp', ['10','159.33'])],
            max_query_depth=0,
            page_size=50
            )
            
        alarms.load_data()

        for alarm in alarms :
            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            self.assertEqual(type(alarm['events'][0]), msiempy.event.Event, 'Type error')

            self.assertRegex(str(alarm['events'][0]['srcIp']), '10|159.33', 'Filtering alarms is not working')

    def test_events_filter_using_query(self):

        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            filters=[('Alert.SrcIP', ['10','159.33'])],
            max_query_depth=0,
            page_size=50
            )
            
        alarms.load_data(use_query=True)

        for alarm in alarms :
            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            self.assertEqual(type(alarm['events'][0]), msiempy.event.Event, 'Type error')
            self.assertRegex(str(alarm['events'][0]['Alert.SrcIP']), '10|159.33', 'Filtering alarms is not working')
        
    def test_print_and_compare(self):

        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            max_query_depth=0,
            page_size=2
        )
        
        alarms_without_events_nor_details = list(alarms.load_data(alarms_details=False))
        alarms_without_events_but_with_details = list(alarms.load_data(events_details=False))
        alarms_with_query_events = list(alarms.load_data(use_query=True))
        alarms_with_alert_data_events = list(alarms.load_data())

        """
        self.assertGreater(len(alarms_without_events),0)
   
        self.assertEqual(len(alarms_without_events), len(alarms_with_query_events), "The two lists doesn't have the same lenght")

        for i in range(len(alarms)):

            self.assertEqual(alarms_without_events[i]['alarmName'], alarms_with_query_events[i]['alarmName'], 'Loading events changed list order')

            if len(alarms_without_events[i]['events']) >0:
                event_sum=alarms_without_events[i]['events'][0]
                event_genuine=alarms_with_query_events[i]['events'][0]
                self.assertEqual(event_sum['ruleMessage'], event_genuine['Rule.msg'], 'getting event details is in trouble')
            """

        print('ALARMS WITHOUT EVENTS NOR DETAILS')
        pprint.pprint(alarms_without_events_nor_details)
        print('ALARMS WITHOUT EVENTS BUT WITH DETAILS')
        pprint.pprint(alarms_without_events_but_with_details)
        print('ALARMS WITH QUERYIED EVENTS')
        pprint.pprint(alarms_with_query_events)
        print('ALARMS WITH ALERT DATA EVENTS')
        pprint.pprint(alarms_with_alert_data_events)

    def test_paged_request(self):
        alarms = msiempy.alarm.AlarmManager(
            time_range='CURRENT_YEAR',
            filters=[('Alert.SrcIP', ['10','159.33'])],
            page_size=10
            )
        alarms.load_data(use_query=True, pages=3)
        for alarm in alarms :
            self.assertEqual(type(alarm), msiempy.alarm.Alarm, 'Type error')
            self.assertEqual(type(alarm['events'][0]), msiempy.event.Event, 'Type error')
            self.assertRegex(str(alarm['events'][0]['Alert.SrcIP']), '10|159.33', 'Filtering alarms is not working')


