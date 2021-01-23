from phonebook.phonebook import PhoneBook
import unittest


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # Example of where you clean up resource
    def tearDown(self) -> None:
        return super().tearDown()

    def setUpPhoneBookWith(self, name, phone_no):
        self.phonebook.add(name, phone_no)

    def test_add_creates_a_phone_book_entry(self):
        self.setUpPhoneBookWith("Bob", "1234")

        self.assertEqual(len(self.phonebook.phoneNumbers), 1)
        self.assertDictEqual(self.phonebook.phoneNumbers, {"Bob": "1234"})

    def test_lookup_by_name(self):
        self.setUpPhoneBookWith("Bob", "12345")

        number = self.phonebook.lookup("Bob")

        self.assertEqual("12345", number)

    def test_raises_key_error_when_name_not_found(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("UserThatDoesNotExist")

    # @unittest.skip("Showcase the skip mechanism")
    def test_is_consistent_when_there_are_no_duplicates(self):
        self.setUpPhoneBookWith(name="Bob", phone_no="12345")

        self.setUpPhoneBookWith("Sue", "23456")

        self.assertTrue(self.phonebook.isConsistent())

    def test_is_not_consistent_when_there_are_duplicate_values(self):
        self.setUpPhoneBookWith(name="Bob", phone_no="12345")
        self.assertTrue(self.phonebook.isConsistent())

        self.setUpPhoneBookWith("Jane", "12345")

        self.assertFalse(self.phonebook.isConsistent())