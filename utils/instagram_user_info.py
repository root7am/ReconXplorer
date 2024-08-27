import instaloader
import os
from pystyle import Colors

loader = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(message):
    print(f"Error: {message}")

def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"Username: {profile.username}")
        print(f"Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Profile Picture URL: {profile.profile_pic_url}")

        for post in profile.get_posts():
            print(f"Post URL: {post.url}")
            print(f"Caption: {post.caption[:100]}")  
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}")
            print()

    except instaloader.exceptions.InstaloaderException as e:
        handle_error(str(e))

def main():
    clear()
    username = input(f"Enter Instagram username: ")
    get_profile_info(username)

if __name__ == "__main__":
    main()