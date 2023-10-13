from testify import assert_equal, run, TestCase

class MyTest(TestCase):
    def test_addition(self):
        assert_equal(1 + 1, 2)

    def test_subtraction(self):
        assert_equal(3 - 1, 2)

if __name__ == "__main__":
    run()

