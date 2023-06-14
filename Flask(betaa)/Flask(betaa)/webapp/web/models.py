from .. import db




class Markers(db.Model):
    #__tablename__ = 'Marker'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    activity_id = db.Column(db.Integer(), db.ForeignKey('activity.id'))
    activity = db.relationship('Activity', backref=db.backref('markers', lazy='dynamic'))

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)



class Activity(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Activity '{}'>".format(self.title)