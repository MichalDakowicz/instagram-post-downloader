import instaloader
import os
import glob

def download_post(L, post_url):
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])
        L.download_post(post, target='videos')
        print("Post downloaded successfully!")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

L = instaloader.Instaloader(download_pictures=True,
                            download_videos=True,
                            download_video_thumbnails=False,
                            download_geotags=False,
                            download_comments=False,
                            save_metadata=False)

login = input("Do you want to login? (sometimes doesn't work without logging in) (yes/no): ")
if login.lower() == "yes":
    L.login(input("Username: "), input("Password: "))
else:
    print("Skipping login")

print("Starting the download process...")
with open("links.txt", "r") as f:
    post_urls = f.read().splitlines()
for i, post_url in enumerate(post_urls):
    print(f"Downloading post {i+1}/{len(post_urls)}")
    download_post(L, post_url)

for txt_file in glob.glob(".\\videos\\*.txt"):
    os.remove(txt_file)