from . import db

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    location = db.Column(db.String(80))
    price = db.Column(db.String(40))
    type = db.Column(db.String(30)) # House or Apartment
    description = db.Column(db.String(260))
    photo = db.Column(db.String(260)) # File path for property photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    
    