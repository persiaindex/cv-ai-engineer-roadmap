from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Alert, Machine


class DashboardSummaryApiTest(APITestCase):
    def setUp(self):
        Machine.objects.create(machine_id="M-500", name="API Machine", location="Aachen")
        Alert.objects.create(
            alert_id="A-500",
            source_type="inspection",
            source_id="I-500",
            message="Test alert",
            severity="high",
            is_open=True,
        )

    def test_dashboard_summary_returns_counts(self):
        response = self.client.get("/api/dashboard/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("machine_count", response.data)
        self.assertIn("open_alert_count", response.data)


class AlertCloseApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="apiuser", password="testpass123")
        self.alert = Alert.objects.create(
            alert_id="A-501",
            source_type="inspection",
            source_id="I-501",
            message="Close me",
            severity="medium",
            is_open=True,
        )

    def test_close_alert_requires_authentication(self):
        response = self.client.post(f"/api/alerts/{self.alert.id}/close/")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_authenticated_user_can_close_alert(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(f"/api/alerts/{self.alert.id}/close/")
        self.alert.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.alert.is_open)