"""
Test the Generate External Ids Management command.
"""

from django.core.management import call_command
from django.test import TestCase
from student.tests.factories import UserFactory

from openedx.core.djangoapps.external_user_ids.models import (
    ExternalId,
    GenerateExternalIdsConfig
)
from openedx.core.djangoapps.external_user_ids.tests.factories import ExternalIDTypeFactory


class TestGenerateExternalIds(TestCase):
    """
    Test generating ExternalIDs for Users.
    """
    def setUp(self):
        self.users = UserFactory.create_batch(10)
        self.user_id_list = [str(user.id) for user in self.users]

    def test_generate_ids_for_all_users(self):
        GenerateExternalIdsConfig.objects.create(
            user_list=','.join(self.user_id_list),
            external_id_type=ExternalIDTypeFactory.create(),
        )

        assert ExternalId.objects.count() == 0
        call_command('generate_external_ids')
        assert ExternalId.objects.count() == 10

    def test_no_new_for_existing_users(self):
        id_type = ExternalIDTypeFactory.create()
        GenerateExternalIdsConfig.objects.create(
            user_list=','.join(self.user_id_list),
            external_id_type=id_type,
        )

        for user in self.users:
            ExternalId.objects.create(
                user=user,
                external_id_type=id_type
            )

        assert ExternalId.objects.count() == 10
        call_command('generate_external_ids')
        assert ExternalId.objects.count() == 10
