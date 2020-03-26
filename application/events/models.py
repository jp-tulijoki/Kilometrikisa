from application import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    
    date = db.Column(db.String(144), nullable=False)
    sport = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, date, sport, distance, description):
        self.date = date
        self.sport = sport
        self.distance = distance
        self.description = description
