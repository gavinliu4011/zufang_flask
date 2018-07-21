from zufang_flask import db

__author__ = 'GavinLiu'
__date__ = '2018/7/21 13:05'


class HouseItem(db.Model):
    """房屋信息"""
    __tablename__ = 'house_info'
    house_url = db.Column(db.String(512), primary_key=True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255))
    source = db.Column(db.String(255))

    def to_dict(self):
        return {
            'house_url': self.house_url,
            'title': self.title,
            'location': self.location,
            'source': self.source,
        }
