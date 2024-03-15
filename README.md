# Instagram Video Downloader with Instaloader

## Description:

This simple Python script leverages the Instaloader library to download videos from Instagram posts. It provides the flexibility to login for potentially better download success and automatically cleans up unnecessary text files.

## Features:

-   Downloads Instagram videos based on post URLs provided in a "links.txt" file.
    Offers optional login for improved download reliability (sometimes required by Instagram).
-   Automatically removes extraneous text files from the download directory.

## Requirements

-   Instaloader library: Install using pip install instaloader

## Instructions

-   Place each Instagram post URL you want to download on a separate line within this file.
-   Run the script:

```bash
python3 main.py
```

-   (Optional) Provide login credentials:
    If you choose to login, the script will prompt you for your username and password.

## How it Works

### Initialization:

The Instaloader instance is created with configurations to download videos, but exclude unnecessary metadata.
Asks the user if they want to log in.

### Downloading Posts:

Reads post URLs from "links.txt".
Iterates through each URL, attempting to download the video using Instaloader.
Provides progress updates.

### Cleanup:

Deletes any leftover text files within the download directory.

## Notes:

Instagram may occasionally change its structure, requiring updates to the Instaloader library or this script.

Logging in sometimes helps if you encounter issues downloading from private accounts.
