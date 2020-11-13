import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app as app
import chatbot as chatbot

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_RESPONSE = "response"

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "Oh dear! I'm sorry you're having trouble. I'll try as best I can to help you. These are the commands I recognize: !! about | !! help | !! funtranslate | !! chuck | !! dance",
                }
            },
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "My name is butler-bot! I'm a bot designed by my master Rami to suite everyone's needs!",
                }
            },
            {
                KEY_INPUT: "!!dance",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "*dances uncontrollably*\n...well sir/madam, I'm sorry you had to see that, but it was my best attempt.",
                }
            },
            {
                KEY_INPUT: "!! help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "Oh dear! I'm sorry you're having trouble. I'll try as best I can to help you. These are the commands I recognize: !! about | !! help | !! funtranslate | !! chuck | !! dance",
                }
            },
            {
                KEY_INPUT: "!! dance",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "*dances uncontrollably*\n...well sir/madam, I'm sorry you had to see that, but it was my best attempt.",
                }
            },
            {
                KEY_INPUT: "!!wow",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "I'm sorry! I don't recongize that command! Type \'!! help\' for possible options",
                }
            },
            {
                KEY_INPUT: "chuck",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "I'm sorry! I don't recongize that command! Type \'!! help\' for possible options",
                }
            },
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "!!aboout hello my name is Robert",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "My name is butler-bot! I'm a bot designed by my master Rami to suite everyone's needs!",
                }
            },
            {
                KEY_INPUT: "!about hello my name is Robert",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "My name is butler-bot! I'm a bot designed by my master Rami to suite everyone's needs!",
                }
            },
            {
                KEY_INPUT: "!!chuck",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "I'm sorry! I don't recongize that command! Type \'!! help\' for possible options",
                }
            },
            {
                KEY_INPUT: "!!  help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "I'm sorry! I don't recongize that command! Type \'!! help\' for possible options",
                }
            },
        ]
    def test_chatbot_message_success(self):
        for test in self.success_test_params:
            inp = chatbot.respond(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(inp, expected[KEY_RESPONSE])
            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)
            
    def test_chatbot_message_failure(self):
        for test in self.failure_test_params:
            inp = chatbot.respond(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(inp, expected[KEY_RESPONSE])

if __name__ == '__main__':
    unittest.main()