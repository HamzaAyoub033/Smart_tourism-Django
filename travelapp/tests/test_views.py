from utils.setup_test import TestSetup
from authentication.models import User
from travelapp.models import travelapp
from django.urls import reverse


class TestModel(TestSetup):

    def test_should_create_atravelapp(self):

        user = self.create_test_user()
        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })

        travelapps = travelapp.objects.all()

        self.assertEqual(travelapps.count(), 0)

        response = self.client.post(reverse('create-travelapp'), {
            'owner': user,
            'title': "Hello do this",
            'description': "Remember to do this"
        })

        updated_travelapps = travelapp.objects.all()

        self.assertEqual(updated_travelapps.count(), 1)

        self.assertEqual(response.status_code, 302)
