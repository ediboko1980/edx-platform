"""
Management command to backfill verification records for preexisting account links

Meant to facilitate the alteration of a particular
third_party_auth_samlproviderconfig to flip on the
enable_sso_id_verification bit, which would ordinarily leave any
preexisting account links without the corresponding resultant ID
verification record.
"""

from django.core.management.base import BaseCommand, CommandError

from third_party_auth.provider import Registry


class Command(BaseCommand):
    """
    Management command to backfill verification records for preexisting account links

    Meant to facilitate the alteration of a particular
    third_party_auth_samlproviderconfig to flip on the
    enable_sso_id_verification bit, which would ordinarily leave any
    preexisting account links without the corresponding resultant ID
    verification record.

    Example usage:
        $ ./manage.py lms backfill_sso_verifications_for_old_account_links --provider-slug=saml-gatech
    """
    help = 'Backfills SSO verification records for the given SAML provider slug'

    def add_arguments(self, parser):
        parser.add_argument(
            '--provider-slug',
            required=True,
        )

    def handle(self, *args, **options):
        provider_slug = options.get('provider_slug', None)

        try:
            provider = Registry.get(provider_slug)
        except ValueError as e:
            raise CommandError('provider slug {slug} does not exist'.format('provider_slug'))

        
