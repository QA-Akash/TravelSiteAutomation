class Utils:   # allstop1 and any value to verify text
    def assert_list_item_text(self, list1, value):
        """

        :param list1: Accept list as argument
        :param value: Value that can be verified
        :return: Assertion is passed else failed
        """

        for stop in list1:
            print("The Text is: ", stop.text)
            try:
                assert stop.text == value
                print("Assertion Pass")
            except:
                print("Assertion is failed")

# Now create the object of this class in the test_caseone.py file
