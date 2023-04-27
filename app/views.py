"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for the application.
"""

from app import app, db
from flask import render_template, request, redirect, send_from_directory, url_for, flash
from app.forms import NewPropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
import os

###
# Routing for the application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Zaria Chen Shui")


@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    """Render the website's form to add a new property."""
    form = NewPropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        # Intake of form data
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        
        type = form.type.data
        description = form.description.data
        photo = form.photo.data
        
        photo_filename = secure_filename(photo.filename)
        photo_filepath = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
        photo.save(photo_filepath)
        
        # Save property info to database
        property = Property(title=title, bedrooms=bedrooms, bathrooms=bathrooms, location=location, price=price, type=type, description=description, photo=photo_filename)
        db.session.add(property)
        db.session.commit()  
       
        # Redirect user
        flash('Property posted successfully.', 'success')
        return redirect(url_for('home'))
        
    return render_template('new_property.html', form=form)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/properties')
def all_properties():
    print('All properties')
    properties = Property.query.all()
    return render_template('all_properties.html', properties=properties)


@app.route('/properties/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/properties/<int:property_id>')
def individual_property(property_id):
    property = Property.query.filter_by(id = str(property_id)).first()
    return render_template('individual_property.html', property=property)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
