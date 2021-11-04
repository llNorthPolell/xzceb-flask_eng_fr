import unittest as test
import translator


class TestTranslator(test.TestCase):
    ## Should pass 
    def test_englishToFrench_pass(self):
        textToTranslate='Hello'
        expected = 'Bonjour'
        actual = translator.english_to_french(textToTranslate)
        self.verboseTest('test_englishToFrench_pass',textToTranslate,expected,actual)
        self.assertEqual(actual, expected)


    ## Should fail
    def test_englishToFrench_fail(self):
        textToTranslate='Hello'
        expected = 'Ni hao'
        actual = translator.english_to_french(textToTranslate)
        self.verboseTest('test_englishToFrench_fail',textToTranslate,expected,actual)
        self.assertNotEqual(actual, expected)


    ## Should pass 
    def test_frenchToEnglish_pass(self):
        textToTranslate='Bonjour'
        expected = 'Hello'
        actual = translator.french_to_english(textToTranslate)
        self.verboseTest('test_frenchToEnglish_pass',textToTranslate,expected,actual)
        self.assertEqual(actual, expected)


    ## Should fail
    def test_frenchToEnglish_fail(self):
        textToTranslate='Est-ce je peux aller aux toilettes?'
        expected = 'Hello'
        actual = translator.french_to_english(textToTranslate)
        self.verboseTest('test_frenchToEnglish_fail',textToTranslate,expected,actual)
        self.assertNotEqual(actual, expected)



    def verboseTest(self,testName,text,expected,actual):
        print ('\n---------------------------------')
        print ('\n '+ testName)
        print ('\n---------------------------------')
        print ('\nText to be Translated: ' + text)
        print ('\nExpected: '+ expected)
        print ('\nActual: ' + str(actual))
        print ('\n---------------------------------')

 

if __name__== '__main__':
   test.main()


