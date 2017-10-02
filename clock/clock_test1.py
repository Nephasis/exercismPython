import unittest

from clock import Clock


class ClockTest(unittest.TestCase):
    # Test creating a new clock with an initial time.
    def test_on_the_hour(self):
        self.assertEqual('08:00', str(Clock(8, 0)))

    def test_past_the_hour(self):
        self.assertEqual('11:09', str(Clock(11, 9)))

    def test_midnight_is_zero_hours(self):
        self.assertEqual('00:00', str(Clock(24, 0)))

    def test_hour_rolls_over(self):
        self.assertEqual('01:00', str(Clock(25, 0)))

    def test_hour_rolls_over_continuously(self):
        self.assertEqual('04:00', str(Clock(100, 0)))

    def test_sixty_minutes_is_next_hour(self):
        self.assertEqual('02:00', str(Clock(1, 60)))

    def test_minutes_roll_over(self):
        self.assertEqual('02:40', str(Clock(0, 160)))

    def test_minutes_roll_over_continuously(self):
        self.assertEqual('04:43', str(Clock(0, 1723)))

    def test_hour_and_minutes_roll_over(self):
        self.assertEqual('03:40', str(Clock(25, 160)))

    def test_hour_and_minutes_roll_over_continuously(self):
        self.assertEqual('11:01', str(Clock(201, 3001)))

    def test_hour_and_minutes_roll_over_to_exactly_midnight(self):
        self.assertEqual('00:00', str(Clock(72, 8640)))

    def test_negative_hour(self):
        self.assertEqual('23:15', str(Clock(-1, 15)))

    def test_negative_hour_rolls_over(self):
        self.assertEqual('23:00', str(Clock(-25, 0)))

    def test_negative_hour_rolls_over_continuously(self):
        self.assertEqual('05:00', str(Clock(-91, 0)))

    def test_negative_minutes(self):
        self.assertEqual('00:20', str(Clock(1, -40)))

    def test_negative_minutes_roll_over(self):
        self.assertEqual('22:20', str(Clock(1, -160)))

    def test_negative_minutes_roll_over_continuously(self):
        self.assertEqual('16:40', str(Clock(1, -4820)))

    def test_negative_hour_and_minutes_both_roll_over(self):
        self.assertEqual('20:20', str(Clock(-25, -160)))

    def test_negative_hour_and_minutes_both_roll_over_continuously(self):
        self.assertEqual('22:10', str(Clock(-121, -5810)))

if __name__ == '__main__':
    unittest.main()
