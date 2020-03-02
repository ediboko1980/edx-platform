"""
Tests for management command backfill_sso_verifications_for_old_account_links
"""

from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError

from student.tests.factories import UserFactory


class TestBackfillSSOVerificationsCommand(TestCase):
    """
    Tests for management command for backfilling SSO verification records
    """

    def setUp(self):
        super(TestBackfillSSOVerificationsCommand, self).setUp()
        self.user1 = UserFactory.create()

    def test_fails_without_required_param(self):
        with self.assertRaises(CommandError):
            call_command('backfill_sso_verifications_for_old_account_links')

    def test_fails_without_named_provider_config(self):
        with self.assertRaises(CommandError):
            call_command('backfill_sso_verifications_for_old_account_links', '--provider-slug', 'gatech')

    def test_successful_
