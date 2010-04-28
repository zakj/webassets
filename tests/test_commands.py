from django.core.management import call_command


def test_rebuild():
    call_command('assets', 'rebuild')