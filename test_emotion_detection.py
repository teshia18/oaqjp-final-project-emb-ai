import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # 1. Joy Assertion check boundaries
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # 2. Anger Assertion check boundaries
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # 3. Disgust Assertion check boundaries
        result_3 = emotion_detector("I am disgusted with this hear")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # 4. Sadness Assertion check boundaries
        result_4 = emotion_detector("I am sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # 5. Fear Assertion check boundaries
        result_5 = emotion_detector("I am really scared of this")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
