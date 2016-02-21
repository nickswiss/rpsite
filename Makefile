
install:
	pip install -r $(CURDIR)/requirements.txt

run:
	$(CURDIR)/rpsite/manage.py runserver

migrations:

