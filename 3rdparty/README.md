3rd party python packages
=========================

## pytz

It is required by Django.  We use stable source releases.

## Django

We remove unnecessary files from stable source releases:

	$ for i in $(find django -name locale); do
	> (cd $i && ls -d */ | sed -Ee '/^(en|fa).$/d' | xargs rm -rf);
	> done
	$ rm -rf django/docs django/tests
