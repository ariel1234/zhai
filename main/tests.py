from django.test import TestCase
import datetime
from django.utils import timezone
from .models import House
# Create your tests here.

class HouseMethodTests(TestCase):
    def test_was_created_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_house = House(name="test", created=time)
        self.assertEqual(future_house.was_created_recently(), False)
