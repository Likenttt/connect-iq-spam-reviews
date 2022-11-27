import redis
import os
import io
from dotenv import load_dotenv
from flask import Flask, Response
import qrcode
from flask import request
import json
from flask import send_file


app = Flask(__name__)


@app.route('/')
@app.route('/<path:path>')
def home(path):
    # b4337e65-9333-49e4-9e7b-27e4f68922a1 in https://apps.garmin.cn/zh-CN/apps/b4337e65-9333-49e4-9e7b-27e4f68922a1
    id = request.args.get('appid')
    identifier = request.args.get('domain')  # all(default)/cn/com
    ecLevel = request.args.get('mode')  # downloads(default)/reviews/ratings
    height = request.args.get('h')

    if record:
        entry = json.loads(record)
        text = entry['text']
        if entry['identifier'] == "NA":
            newEntry = {
                'id': 'qr_pair:'+id,
                'text': text,
                'identifier': identifier
            }
            r.set('qr_pair:'+id, json.dumps(newEntry))
            entry['identifier'] = identifier
        if entry['identifier'] == identifier:
            error_correction_level = get_error_correction_level(ecLevel)
            qr = qrcode.QRCode(
                version=None,
                box_size=7 if height is None else height,
                error_correction=error_correction_level,
                border=1)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            tmp_file_dir = '/tmp/'+id+'.jpeg'
            img.save(tmp_file_dir, format='jpeg')
            return send_file(tmp_file_dir, mimetype='image/jpeg', download_name='qrcode.jpeg'), 200
    return 'N', 200
