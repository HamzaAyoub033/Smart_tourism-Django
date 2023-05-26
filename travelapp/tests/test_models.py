from utils.setup_test import TestSetup
from authentication.models import User
from travelapp.models import travelapp


class TestModel(TestSetup):

    def test_should_create_user(self):
        user = self.create_test_user()
        travelapp = travelapp(owner=user, title="Buy milk", description='get it done')
        travelapp.save()
        self.assertEqual(str(travelapp), 'Buy milk')
