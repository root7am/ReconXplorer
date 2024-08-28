from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_tiktok_user_info(username):
    """Fetch TikTok user information using Selenium."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service('C:/path/to/chromedriver.exe')  
    
    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = f"https://www.tiktok.com/@{username}"
        driver.get(url)
        time.sleep(5)  

        user_info = {
            "Username": username,
            "ID": None,
            "Followers": None,
            "Following": None,
            "Likes": None,
            "Videos": None,
            "Profile Picture URL": None
        }


        try:
            profile_picture = driver.find_element(By.CSS_SELECTOR, 'img[src*="profile_avatar"]')
            user_info["Profile Picture URL"] = profile_picture.get_attribute('src')
        except Exception as e:
            print(f"Error finding profile picture: {e}")

        try:
            stats = driver.find_elements(By.CSS_SELECTOR, 'strong')
            if len(stats) >= 3:
                user_info["Followers"] = stats[0].text
                user_info["Following"] = stats[1].text
                user_info["Likes"] = stats[2].text
        except Exception as e:
            print(f"Error finding stats: {e}")

        try:
            video_count = driver.find_element(By.CSS_SELECTOR, 'span[data-e2e="video-count"]')
            user_info["Videos"] = video_count.text
        except Exception as e:
            print(f"Error finding video count: {e}")

        return user_info
    except Exception as e:
        return {"Error": str(e)}
    finally:
        if driver:
            driver.quit()

def main():
    """Main function to handle user input and display TikTok user information."""
    username = input("Enter the TikTok username: ").strip()
    
    if not username:
        print("Username cannot be empty.")
        return
    
    user_data = get_tiktok_user_info(username)
    
    if "Error" in user_data:
        print(f"Error: {user_data['Error']}")
    else:
        print("TikTok User Information:")
        for key, value in user_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
