from setuptools import setup, find_packages

setup(
	name = 'libraryman',
	version = '0.1',
	author = 'Ali Farzanrad',
	author_email = 'ali_farzanrad@riseup.net',
	description = 'Library Management System',
	license = 'ISC',
	keywords = 'django library management',

	packages = find_packages(),
	include_package_data = True,
	install_requires = ['Django>=2.1,<2.2'],
	entry_points = {
		'console_scripts': [
			'libraryman = conf.scripts:main'
		]
	},
	classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: No Input/Output (Daemon)',
		'Environment :: Web Environment',
		'Framework :: Django :: 2.1',
		'Intended Audience :: Education',
		'License :: OSI Approved :: ISC License (ISCL)',
		'Natural Language :: English',
		'Natural Language :: Persian',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.8',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Internet :: WWW/HTTP :: WSGI',
	])
