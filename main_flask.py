from flask import Flask, request, jsonify, render_template, send_from_directory
import instaloader
import os
import glob

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'videos')

@app.route('/')
def index():
    return render_template('index.html')

class Downloader:
    def __init__(self, username=None, password=None):
        self.L = instaloader.Instaloader(download_pictures=True,
                                         download_videos=True,
                                         download_video_thumbnails=False,
                                         download_geotags=False,
                                         download_comments=False,
                                         save_metadata=False)
        if username and password:
            self.login(username, password)
    
    def login(self, username, password):
        self.L.login(username, password)
    
    def download_post(self, post_url):
        try:
            post = instaloader.Post.from_shortcode(self.L.context, post_url.split("/")[-2])
            self.L.download_post(post, target='videos')
            if post.typename == 'GraphImage':
                suffix = '.jpg'
            elif post.typename == 'GraphVideo':
                suffix = '.mp4'
            return 'videos/' + post.date.isoformat().replace('T', '_').replace(':', '-') + "_UTC" + suffix
        except instaloader.exceptions.InstaloaderException as e:
            return False
    
    def run(self, post_urls):
        urls = []
        for post_url in post_urls:
            result = self.download_post(post_url)
            if result:
                urls.append(result)
        for txt_file in glob.glob(".\\videos\\*.txt"):
            os.remove(txt_file)
        return urls

@app.route('/download', methods=['POST'])
def download():
    username = request.form.get('username')
    password = request.form.get('password')
    post_urls = request.form.get('post_urls').splitlines()
    downloader = Downloader(username, password)
    urls = downloader.run(post_urls)
    return urls

@app.route('/videos/<path:filename>')
def media(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )
