import os
import requests
import shutil


def download_file(url: str, directory: str):
    dl_filename = os.path.basename(url)
    new_dl_path = os.path.join(directory, dl_filename)

    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(new_dl_path, 'wb') as file_obj:
            shutil.copyfileobj(req.raw, file_obj)
        print("Downloaded and Saved")


if __name__=='__main__':

    # Directory to save downloaded files, you can change directory to save file
    download_directory = os.path.join(os.path.expanduser('~'), 'downloads')

    url = input('https://img.freepik.com/free-photo/ai-human-technology-background_1409-5588.jpg \nEnter Url To Download: ')

    download_file(url, download_directory)

    



