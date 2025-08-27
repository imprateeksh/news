import feedparser
from datetime import datetime

# Define feeds
feeds = {
    "AI": "https://news.google.com/rss/search?q=artificial+intelligence&hl=en-IN&gl=IN&ceid=IN:en",
    "Cloud": "https://news.google.com/rss/search?q=cloud+computing&hl=en-IN&gl=IN&ceid=IN:en"
}

def fetch_news(feed_url, limit=5):
    news_items = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:limit]:
        news_items.append(f"- [{entry.title}]({entry.link})")
    return "\n".join(news_items)

# Current date + day
now = datetime.utcnow()
date_str = now.strftime("%Y-%m-%d")
day_str = now.strftime("%A")  # Monday, Tuesday, etc.
time_str = now.strftime("%H:%M UTC")

# Generate README content
readme_content = f"""# 🌍 Daily Trends  

📅 **Date:** {date_str} ({day_str})  
🕒 **Last Updated:** {time_str}  

---

## 🧠 AI
{fetch_news(feeds["AI"])}

## ☁️ Cloud
{fetch_news(feeds["Cloud"])}
"""

# Write to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated")
