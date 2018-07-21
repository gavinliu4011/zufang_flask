from zufang_flask.models import HouseItem

__author__ = 'GavinLiu'
__date__ = '2018/7/21 13:05'

from flask import Blueprint, jsonify, render_template

house = Blueprint('house', __name__)


@house.route('/index.html')
def index():
    return render_template('index.html')


@house.route('/get_houselist', methods=['GET'])
def get_houselist():
    house_list = [house_info.to_dict() for house_info in HouseItem.query.all()]
    return jsonify(data=house_list)
