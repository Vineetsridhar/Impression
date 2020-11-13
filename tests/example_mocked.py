import unittest
import unittest.mock as mock

import sys
sys.path.append("/home/ec2-user/environment/project2")

import app as app
import chatbot as chatbot

KEY_ID = 0
KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_RESPONSE = "response"

class MockedMessageRow():
    def __init__(self, user, text, time, i):
        self.username = user
        self.messageText = text
        self.timestamp = time
        self.imageUrl = i
        
class MockedUserRow():
    def __init__(self, username, imageUrl):
        self.username = username
        self.imageUrl = imageUrl

# Custom Exceptions
class ButlerCommandException(Exception):
    pass

class MockedTestCases(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_ID: 1,
                KEY_INPUT: "!!funtranslate You are a fool",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "Thee art a daw ",
                }
            },
            {
                KEY_ID: 2,
                KEY_INPUT: {'status': 0, 'username': "bobsmith@gmail.com", 'imageUrl': "https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png"},
                KEY_EXPECTED: {
                    KEY_RESPONSE: "No TypeErrors with Input",
                }
            },
            {
                KEY_ID: 3,
                KEY_INPUT: {'username': "bobsmith@gmail.com", 'messageText': "Hello World! I'm messageText", 'timestamp': "N/A"},
                KEY_EXPECTED: {
                    KEY_RESPONSE: "https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png",
                }
            },
            {
                KEY_ID: 4,
                KEY_INPUT: {'username': "adamsmith@gmail.com", 'messageText': "!!help", 'timestamp': "N/A"},
                KEY_EXPECTED: {
                    KEY_RESPONSE: "Butler Command Detected",
                }
            },
            {
                KEY_ID: 5,
                KEY_INPUT: "",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "TypeError",
                }
            },
        ]
    
    def mocked_funtranslate(self, url):
        mocked_request = mock.Mock()
        mocked_json = {'success': {'total': 1}, 'contents': {'translated': 'Thee%art%a%daw', 'text': 'You%are%a%fool', 'translation': 'shakespeare'}}
        mocked_request.json.return_value = mocked_json
        return mocked_request
        
    def mocked_funtranslate_empty_response(self, url):
        raise KeyError()
    
    def mocked_db_list(self):
        return [
            MockedUserRow("tedsmith@gmail.com", "https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png"),
            MockedUserRow("johnsmith@gmail.com", "https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png")
        ]
        
    def mocked_db_list_messages(self):
        return [
            MockedMessageRow("tedsmith@gmail.com","hello","N/A","https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png"),
            MockedMessageRow("johnsmith@gmail.com","hi","N/A","https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png")
        ]
    
    def mocked_db_add_user(self, value):
        mocked_row = mock.Mock()
        mocked_list = self.mocked_db_list()
        mocked_row.json.return_value = mocked_list
        return mocked_row
    
    def mocked_db_add_message(self, data):
        if not isinstance(data.username, str):
            raise TypeError
        if not isinstance(data.messageText, str):
            raise TypeError
        if not isinstance(data.timestamp, str):
            raise TypeError
        if data.messageText[0:2] == "!!":
            raise ButlerCommandException
        
    def mocked_emit_request_username_response(self, channel, data):
        if not isinstance(data["username"], str):
            raise TypeError
        if not isinstance(data, dict):
            raise TypeError
        if not isinstance(data["status"], int):
            raise TypeError
        
    def mocked_get_userimage(self, value):
        mocked_filter = mock.Mock()
        mocked_filter.first.return_value = MockedUserRow("tedsmith@gmail.com", "https://www.abc.net.au/cm/rimage/8654752-16x9-xlarge.png")
        return mocked_filter
        
    def empty(self):
        pass
    
    def mocked_db_query(self, value):
        if(type(value) == str):
            raise TypeError
        mocked_query = mock.Mock()
        mocked_query.order_by.all.return_value = self.mocked_db_list_messages()
        return mocked_query
        
    def mocked_emit_messages(self, channel, data):
        if not isinstance(data["allMessages"], dict):
            raise TypeError
    
    def test_success(self):
        for test_case in self.success_test_params:
            if(test_case[KEY_ID] == 1):
                with mock.patch('requests.get', self.mocked_funtranslate):
                    inp = chatbot.respond(test_case[KEY_INPUT])
                    
                expected = test_case[KEY_EXPECTED]
                
                self.assertEqual(inp, expected[KEY_RESPONSE])
            
            elif(test_case[KEY_ID] == 2):
                try:
                    with mock.patch('app.db.session.add', self.mocked_db_add_user):
                        with mock.patch('app.update_user_count', self.empty):
                            with mock.patch('app.update_messages', self.empty):
                                with mock.patch('app.update_user_count', self.empty):
                                    test = app.on_username_request(test_case[KEY_INPUT])
                                    result = "No TypeErrors with Input"
                except ValueError:
                    result = "ValueError"
                    
                expected = test_case[KEY_EXPECTED]
                self.assertEqual(result, expected[KEY_RESPONSE])
            
            elif(test_case[KEY_ID] == 3):
                try:
                    with mock.patch('sqlalchemy.orm.query.Query.filter', self.mocked_get_userimage):
                        with mock.patch('app.db.session.add', self.mocked_db_add_message):
                            with mock.patch('app.update_messages', self.empty):
                                result = app.handle_new_message(test_case[KEY_INPUT]).imageUrl
                except AttributeError:
                    result = "Attribute Error for Image"
                    
                expected = test_case[KEY_EXPECTED]
                self.assertEqual(result, expected[KEY_RESPONSE])
            
            elif(test_case[KEY_ID] == 4):
                try:
                    with mock.patch('sqlalchemy.orm.query.Query.filter', self.mocked_get_userimage):
                        with mock.patch('app.db.session.add', self.mocked_db_add_message):
                            with mock.patch('app.update_messages', self.empty):
                                result = app.handle_new_message(test_case[KEY_INPUT]).messageText
                except ButlerCommandException:
                    result = "Butler Command Detected"
                    
                expected = test_case[KEY_EXPECTED]
                self.assertEqual(result, expected[KEY_RESPONSE])
        
if __name__ == '__main__':
    unittest.main()