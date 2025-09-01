import time
import schedule
from instagrapi import Client
import os

# ====== CONFIGURATION ======
USERNAME = os.getenv("IG_USERNAME") or "relax_mind___"
PASSWORD = os.getenv("IG_PASSWORD") or "Prashant@8668"
VIDEO_PATH = "D:\\reels\\bottle close.mp4"  # Path to your reel file

# Funny + Satisfying captions with hashtags
CAPTIONS = [
    "POV: when you finally win an argument with the bottle cap 😂 #satisfying #funnyreels #viralreels #asmr #fyp #instareels",
    "Me closing tabs on my brain like this 🧠✨ #relatable #dailyvibes #viral #funny #satisfyingreels",
    "Somebody give me a medal 🥇 for this talent #viralreels #comedyreels #satisfyingvideo #fyp #instareels",
    "Not me, just a professional bottle closer 💪🤣 #funnyreels #satisfying #viralvideo #trendingreels #reelitfeelit",
    "When life gives you bottles, close them like a boss 😎 #instareels #funny #fypシ #satisfyingcontent #viral",
    "Tell me this isn’t the most satisfying thing you’ve seen today 👀 #asmr #reelsinstagram #satisfying #viralreels #instafunny",
    "Rewatching this 10 times because… why not 😍 #dailyvibes #funnyreels #asmrcommunity #trendingreels #instareels",
    "Therapist: ‘relax.’ Me: closes bottle like this 🧘 #satisfyingvideo #relatable #viral #funny #instaviral",
    "Lowkey better than ASMR 🔥 #satisfying #asmr #viralreels #funnyreels #instatrending",
    "The bottle: finally feels loved ❤😂 #funnyvideo #reelitfeelit #viralcontent #instareels #comedyreels"
]

# Times to post (24-hour format)
SCHEDULE_TIMES = ["08:00", "13:00", "18:00", "21:00"]  # 8 AM, 1 PM, 6 PM, 9 PM
# ===========================

cl = Client()
cl.login(USERNAME, PASSWORD)

caption_index = 0  # track which caption to use

def post_reel():
    global caption_index
    caption = CAPTIONS[caption_index % len(CAPTIONS)]  # rotate captions
    cl.clip_upload(VIDEO_PATH, caption=caption)
    print(f"✅ Reel posted with caption: {caption}")
    caption_index += 1

# Schedule posts
for post_time in SCHEDULE_TIMES:
    schedule.every().day.at(post_time).do(post_reel)
    print(f"📅 Scheduled reel at {post_time}")

# Keep script running
while True:
    schedule.run_pending()
    time.sleep(30)