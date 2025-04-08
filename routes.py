from flask import Blueprint, request, jsonify, send_file
from utils import is_valid_youtube_url, download_video, get_video_info
import os

api = Blueprint('api', __name__)

@api.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url or not is_valid_youtube_url(url):
        return jsonify({"error": "Invalid or missing YouTube URL"}), 400

    try:
        file_path = download_video(url)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/video_info', methods=['GET'])
def video_info():
    url = request.args.get('url')

    if not url or not is_valid_youtube_url(url):
        return jsonify({"error": "Invalid or missing YouTube URL"}), 400

    try:
        info = get_video_info(url)
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
