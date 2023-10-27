from bs4 import BeautifulSoup
import requests
import instaloader
import time

L = instaloader.Instaloader()
L.load_session_from_file('frankie____d')

def get_bio(username):
    # Replace 'username' with the Instagram username you want to scrape
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.biography
    # Download the profile's data
    #L.download_profile(profile, profile_pic=True)

with open("/Users/frankie/Documents/random/trinity.txt") as f:
    usernames = str(f.readlines()) # individual words

usernames = usernames.split("href=")
usernames = [x.split(' role=')[0] for x in usernames]

usernames = [i.split('"')[1] for i in usernames[1:]]
usernames = usernames[1:]
usernames = [i.split('/')[1] for i in usernames]
usernames = list(set(usernames))

count = 0
user_list = []
failed = []
for username in usernames:
    try:
        bio = str(get_bio(username))
        print(bio)
        if '24' in bio or 'snap' in bio or 'sc' in bio or 'Sc' in bio:
            user_list.append(f"{username}: {bio}")
            with open("/Users/frankie/Documents/random/trinity2.txt", "w") as o:
                o.write(str(user_list))
    except Exception:
        print(username)
        failed.append(username)
    time.sleep(2)


print(failed)