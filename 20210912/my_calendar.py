import datetime
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # python's datetime library treats Monday as 0 and sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test if tuesday is a weekday

assert is_weekday()

# Mock .today() to treturn Saturday
datetime.datetime.today.return_value = saturday
# Test if saturday is a weekday
# assert is_weekday()


# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        # Set the side effect of .get()
        requests.get.side_effect = [Timeout, response_mock]
        # Test that the first request raises a Timeout
        with self.assertRaises(Timeout):
            get_holidays()
        # Now retry, expecting a successsful response
        assert get_holidays()["12/25"] == "Christmas"
        # Finally, assert .get() was called twice
        assert requests.get.call_count == 2


if __name__ == "__main__":
    unittest.main()
