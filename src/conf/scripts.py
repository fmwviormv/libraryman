import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

def main(argv = None):
	from django.core.management import execute_from_command_line
	execute_from_command_line(argv)
