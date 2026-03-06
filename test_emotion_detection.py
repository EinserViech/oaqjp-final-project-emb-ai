"""
Unit tests for the EmotionDetection package.
"""

import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Test cases for the emotion_detector function.
    """

    def test_joy(self):
        """
        Test joy.
        """
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        """
        Test anger.
        """
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        """
        Test disgust.
        """
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_sadness(self):
        """
        Test sadness.
        """
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        """
        Test fear.
        """
        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()