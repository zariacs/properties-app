# Properties Web App

Deploying properties web app. Using Render to host frontend (JavaScript), backend (Flask), and database (PostgreSQL). This app creates new properties through an intake form (Flask-WTForms), connects to a database (Flask-SQLAlchemy, PostgreSQL) and adds the property to that database, displays all properties, and displays individual properties.

-- App was developed locally successfully.
-- Have deployed the database and connected to it from the local app. Currently working on deploying the rest of the frontend and backend.
-- After that, I'll integrate storage for property images using a DropBox or Google Drive API. This is to replace the previous method of storing uploaded image files in a local uploads directory, which is no longer an option due to there being no permanent storage for the file directory once deployed. This storage integration is intended to remedy this for the new deployment environment.
-- Lastly, I will include user authentication for this particular app, to further improve security by restricting file uploads to registered users.
