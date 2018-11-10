Library Management System
=========================

This is going to be a Library Management System (under development).
There is a plan for these functionalities:

  * Add/Edit/Remove Book/Author/Publisher,

  * User Registeration by admin,

  * Users can request to borrowing a book or extending borrowing,

  * Admin can approve or reject any request,

  * ...

How to run
==========

At first create a virtual environment and then activate it.

In UNIX-like systems:

	$ /path/to/python -m venv venv
	$ . venv/bin/activate

In Microsoft Windows:

	$ C:\path\to\python.exe -m venv venv
	$ venv\Scripts\activate

Then install requirements:

	$ pip install -r requirements.txt

Finally run:

	$ libraryman migrate
	$ libraryman createsuperuser
	$ libraryman runserver
