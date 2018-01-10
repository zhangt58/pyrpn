.PHONY: test

test:
	PYTHONPATH=../:$(PYTHONPATH) \
	nosetests --with-coverage --cover-package=pyrpn \
		--with-id -v --logging-level=INFO \
		--exclude-dir-file="skiptests"

