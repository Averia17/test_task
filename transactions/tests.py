from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from transactions.models import Transaction
from users.models import User


class TransactionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.test", password="TESTTEST"
        )
        self.list_url = reverse("transactions-list")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_create_deposit_transaction(self):
        data = {
            "amount": 1000,
            "category": self.user.categories.first().id,
            "organization": "xone",
            "description": "test",
            "is_deposit": True,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, 1000)

    def test_create_withdraw_transaction(self):
        self.user.balance = 1500
        self.user.save()
        data = {
            "amount": 500,
            "category": self.user.categories.first().id,
            "organization": "xone",
            "description": "test",
            "is_deposit": False,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, 1000)

    def test_create_withdraw_invalid_transaction(self):
        data = {
            "amount": 500,
            "category": self.user.categories.first(),
            "organization": "xone",
            "description": "test",
            "is_deposit": False,
        }
        response = self.client.post(self.list_url, data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 0)
