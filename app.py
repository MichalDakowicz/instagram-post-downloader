from flask import Flask, request, jsonify, render_template, send_from_directory
import instaloader
import os
import glob
import zipfile
import time

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
        post = instaloader.Post.from_shortcode(self.L.context, post_url.split("/")[-2])
        self.L.download_post(post, target='videos')
    
    def run(self, post_urls):
        urls = []
        for post_url in post_urls:
            result = self.download_post(post_url)
            if result:
                urls.append(result)
        return urls

@app.route('/download', methods=['POST'])
def download():
    username = request.form.get('username')
    password = request.form.get('password')
    post_urls = request.form.get('post_urls').splitlines()
    downloader = Downloader(username, password)
    downloader.run(post_urls)
    
    for url in glob.glob('./videos/*.txt'):
        os.remove(url)

    with zipfile.ZipFile('zip/downloads.zip', 'w') as zipf:
        for url in glob.glob('./videos/*'):
            zipf.write(url, arcname=os.path.basename(url))
            
    return send_from_directory('zip', 'downloads.zip', as_attachment=True)

@app.route('/clear', methods=['POST'])
def clear():
    for url in glob.glob('./videos/*'):
        os.remove(url)
    for url in glob.glob('zip/*'):
        os.remove(url)
        
    return "Cleared"

if __name__ == "__main__":
    app.run(debug=True)
