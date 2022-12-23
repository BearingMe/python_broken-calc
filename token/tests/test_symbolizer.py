import unittest 

from src import Symbolizer

class TestSymbolizer(unittest.TestCase):
    def setUp(self) -> None:
        self.symbolizer = Symbolizer()

    def test_validate_input(self):
        # Test empty input
        result = self.symbolizer.validate_input("")
        self.assertFalse(result)

        # Test unbalanced parentheses
        result = self.symbolizer.validate_input("(1 + 2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + 2)")
        self.assertFalse(result)

        # Test invalid characters
        result = self.symbolizer.validate_input("1 + 2 $ 3")
        self.assertFalse(result)

        # Test two operators in a row
        result = self.symbolizer.validate_input("1 + ++ 2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + */ 2")
        self.assertFalse(result)

        # Test two minus signs in a row
        result = self.symbolizer.validate_input("1 + -- 2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + --2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + -- -2")
        self.assertFalse(result)


        # Test starting or ending with an operator
        result = self.symbolizer.validate_input("*1 + 2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + 2*")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + 2+")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + 2-")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("/1 + 2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1 + 2/")
        self.assertFalse(result)

        # Test invalid numerical sequences
        result = self.symbolizer.validate_input("1.2.3")
        self.assertFalse(result)
        result = self.symbolizer.validate_input("1..2")
        self.assertFalse(result)
        result = self.symbolizer.validate_input(".1.2")
        self.assertFalse(result)

        # Test valid input
        result = self.symbolizer.validate_input("+1 + 2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("-1 + 2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1 + 2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1.5 + 2.5")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1.0 + 2.0")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1 + 2 * (3 - 4) / 5")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1 + -2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1.5+-4.5")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1 + (2 + 3) * 4")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1 + (2 + 3) * -4")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1") 
        self.assertTrue(result)
        result = self.symbolizer.validate_input("15.0")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("12.0 + 1")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("1.0 + 45.0 - 1.0")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("7.0 + 21 - 1.0 * 19.0")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("71.0 + 215 - 91.5 * 19.0 / 2.0")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("+1") 
        self.assertTrue(result)
        result = self.symbolizer.validate_input("-1")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("--2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("2--2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("2+-2")
        self.assertTrue(result)
        result = self.symbolizer.validate_input("(1 + 2) * 3 - 4 / 5")
        self.assertTrue(result)

        # more invalid input
        self.assertFalse(self.symbolizer.validate_input("(1 + 2 * 3 - 4 / 5"))
        self.assertFalse(self.symbolizer.validate_input("  ")) 
        self.assertFalse(self.symbolizer.validate_input("hello world")) 
        self.assertFalse(self.symbolizer.validate_input("1.0 + 45.0 - 1.0 * 19.0 / 2.0 +")) 
        self.assertFalse(self.symbolizer.validate_input("++++")) 
        self.assertFalse(self.symbolizer.validate_input("+++1")) 
        self.assertFalse(self.symbolizer.validate_input("15..0")) 
        self.assertFalse(self.symbolizer.validate_input("15........0")) 
        self.assertFalse(self.symbolizer.validate_input("-----"))
        self.assertFalse(self.symbolizer.validate_input("-----2"))
        self.assertFalse(self.symbolizer.validate_input("---2"))
        self.assertFalse(self.symbolizer.validate_input("--"))
        self.assertFalse(self.symbolizer.validate_input("*-2"))
        self.assertFalse(self.symbolizer.validate_input("***"))
        self.assertFalse(self.symbolizer.validate_input("***43"))
        self.assertFalse(self.symbolizer.validate_input("//"))
        self.assertFalse(self.symbolizer.validate_input("//rewr"))
        self.assertFalse(self.symbolizer.validate_input("*"))
        self.assertFalse(self.symbolizer.validate_input("*1"))
        self.assertFalse(self.symbolizer.validate_input("/1"))
        self.assertFalse(self.symbolizer.validate_input("1.5.0")) 

        # especial cases
        self.assertTrue(self.symbolizer.validate_input("+1"))
        self.assertTrue(self.symbolizer.validate_input("-1"))
        self.assertFalse(self.symbolizer.validate_input("*1"))
        self.assertFalse(self.symbolizer.validate_input("/1"))


    def test_create_symbol(self):
        self.assertEqual(self.symbolizer.create_symbol("1+4"), [1.0, "+", 4.0])
        self.assertEqual(self.symbolizer.create_symbol("1.5+4.5"), [1.5, "+", 4.5])
        self.assertEqual(self.symbolizer.create_symbol("1.0 + 2.0"), [1.0, "+", 2.0])        
        self.assertEqual(self.symbolizer.create_symbol("1 + 2 * (3 - 4) / 5"), [1.0, "+", 2.0, "*", "(", 3.0, "-", 4.0, ")", "/", 5.0])
        self.assertEqual(self.symbolizer.create_symbol("1 + -2"),  [1.0, "+", -2.0])
        self.assertEqual(self.symbolizer.create_symbol("1.5+-4.5"), [1.5, "+", -4.5])
        self.assertEqual(self.symbolizer.create_symbol("1 + 2 * (3 - 4) / 5"), [1.0, "+", 2.0, "*", "(", 3.0, "-", 4.0, ")", "/", 5.0])
        self.assertEqual(self.symbolizer.create_symbol("5.5"), [5.5])
        self.assertEqual(self.symbolizer.create_symbol("1234567890"), [1234567890.0])
        self.assertEqual(self.symbolizer.create_symbol("1+2+3+4+5"), [1.0, "+", 2.0, "+", 3.0, "+", 4.0, "+", 5.0])
        self.assertEqual(self.symbolizer.create_symbol("((1+2)+(3+4))+(5+6)"), ["(", "(", 1.0, "+", 2.0, ")", "+", "(", 3.0, "+", 4.0, ")", ")", "+", "(", 5.0, "+", 6.0, ")"])
        self.assertEqual(self.symbolizer.create_symbol("1+2+3+4+5+"), [1.0, '+', 2.0, '+', 3.0, '+', 4.0, '+', 5.0, '+'])
        
        self.assertNotEqual(self.symbolizer.create_symbol("1+4"), [1, "+", 5])

        with self.assertRaises(ValueError):
            self.assertEqual(self.symbolizer.create_symbol("1.0.0 + 2.0"), [])

        # special cases    
        self.assertEqual(self.symbolizer.create_symbol("+1"), [1])
        self.assertEqual(self.symbolizer.create_symbol("-1"), [-1])
        self.assertNotEqual(self.symbolizer.create_symbol("*1"), [1])
        self.assertNotEqual(self.symbolizer.create_symbol("/1"), [1])
