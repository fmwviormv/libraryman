import os

def manage():
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
	from django.core.management import execute_from_command_line
	if os.name == 'nt' and not os.sys.argv[0].endswith('.py'):
		os.sys.argv[0] += '-script.py'
	execute_from_command_line(os.sys.argv)
