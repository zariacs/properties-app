# Properties PostgreSQL/Flask/Boostrap

Used Flask with Bootstrap to make a web application that accepts and displays information on properties available for rent/sale. It stores the property information in a PostgreSQL database.

This app creates new properties through an intake form (Flask-WTForms), connects to a database (PostgreSQL, Flask-SQLAlchemy) and adds the property to that database, displays all properties, and displays individual properties.

Made use of routes, migrations, models, templates, etc.

```bash
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt
$ flask --app app --debug run
```
