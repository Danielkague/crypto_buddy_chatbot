# 💬 CryptoBuddy - Your AI Crypto Investment Guide

Welcome to **CryptoBuddy**, a rule-based Python chatbot that provides friendly, data-driven cryptocurrency investment advice based on **profitability** (e.g., price trends) and **sustainability** (e.g., energy efficiency, project viability).

---

## ✅ What You'll Learn

- Basic AI-driven decision-making using `if-else` logic
- How to design conversational logic with Python
- Simple data analysis on crypto trends
- Real-world application of sustainable investing

---

## 🤖 Bot Personality

**Name:** CryptoBuddy  
**Tone:** Friendly, helpful, and slightly meme-loving  
**Sample Greeting:**  
> “Hey there! 🌟 Let’s find you a green and growing crypto!”

---

## 🛠️ Tools & Technologies

- **Language**: Python (Beginner-friendly)
- **Platform**: Google Colab / Jupyter Notebook / Any IDE
- **Libraries**: No external libraries required (optional: ChatterBot or NLTK for stretch goals)

---

## 📊 Dataset Used

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

🧠 Chatbot Logic
The chatbot understands basic user inputs like:

“Which crypto is trending up?”

“What’s the most sustainable coin?”

“Which coin is best for long-term growth?”

Example Rule
if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

💡 Investment Advice Logic
Profitability Advice:

Prioritize coins where price_trend == "rising" and market_cap == "high"

Sustainability Advice:

Prefer energy_use == "low" and sustainability_score > 7/10

🧪 Sample Interaction
You: Which crypto should I buy for long-term growth?
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀

🔒 Ethics & Disclaimer
⚠️ Disclaimer: This chatbot is for educational purposes only. Crypto is risky—always do your own research before investing.

🌱 Stretch Goals (Optional)
Integrate with CoinGecko API for real-time data

Use NLTK for more advanced natural language understanding

Add GUI or voice input for better UX

📁 Project Structure
crypto_chatbot/
│
├── crypto_bot.py        
├── README.md            
├── screenshots/         
└── demo_video.mp4

🗣️ 50-Word Summary
CryptoBuddy uses simple rule-based logic to analyze cryptocurrency data and offer investment suggestions. By evaluating price trends and sustainability metrics, it mimics basic AI decision-making without machine learning. It’s a hands-on introduction to how AI can guide informed, ethical financial decisions using straightforward Python logic.

🚀 How to Run
Clone or download the repo.

Open crypto_bot.py in your favorite Python environment.

Run the script and start chatting!

Try asking:

“What’s the best coin for growth?”

“Which coin is most energy efficient?”

📸 Submission Checklist
✅ Code file uploaded
✅ README completed
✅ Screenshot of chatbot in action
✅ 30-second demo video
✅ 50-word summary posted.

🧠 Let’s Build the Future, One Chatbot at a Time!
Happy coding!
Join the PLP Community to share progress, ask questions, and get inspired! 💬✨
---

Let me know if you'd like the accompanying `crypto_bot.py` code, a sample screenshot mockup, or guidance on creating   
