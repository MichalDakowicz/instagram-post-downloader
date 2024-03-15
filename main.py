import instaloader
import os
import glob

if not os.path.exists("videos"):
    os.makedirs("videos")

if not os.path.exists("links.txt"):
    with open("links.txt", "w") as f:
        f.write("")

class Downloader:
    def __init__(self):
        self.L = instaloader.Instaloader(download_pictures=True,
                                         download_videos=True,
                                         download_video_thumbnails=False,
                                         download_geotags=False,
                                         download_comments=False,
                                         save_metadata=False)
        login = input("Do you want to login? (sometimes doesn't work without logging in) (yes/no): ")
        if login.lower() == "yes":
            self.login(input("Username: "), input("Password: "))
        else:
            print("Skipping login")
        self.run()
    
    def download_post(self, post_url):
        try:
            post = instaloader.Post.from_shortcode(self.L.context, post_url.split("/")[-2])
            self.L.download_post(post, target='videos')
            print("Post downloaded successfully!")
        except instaloader.exceptions.InstaloaderException as e:
            print(f"Error: {e}")
    
    def run(self):
        print("Starting the download process...")
        with open("links.txt", "r") as f:
            post_urls = f.read().splitlines()
        for i, post_url in enumerate(post_urls):
            print(f"Downloading post {i+1}/{len(post_urls)}")
            self.download_post(post_url)
        for txt_file in glob.glob(".\\videos\\*.txt"):
            os.remove(txt_file)

download = Downloader()

for txt_file in glob.glob(".\\videos\\*.txt"):
    os.remove(txt_file)