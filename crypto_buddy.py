import requests
import json
import time
from typing import Dict, Any, Optional

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.api_base = "https://api.coingecko.com/api/v3"
        self.cache = {}
        self.cache_duration = 300  # 5 minutes
        
        # Predefined sustainability scores (manual research)
        self.sustainability_db = {
            "bitcoin": {"score": 3, "reason": "High energy PoW", "emoji": "🔥"},
            "ethereum": {"score": 7, "reason": "PoS upgrade", "emoji": "⚡"},
            "cardano": {"score": 9, "reason": "Efficient PoS", "emoji": "🌱"},
            "solana": {"score": 6, "reason": "Fast PoS", "emoji": "⚡"},
            "polygon": {"score": 8, "reason": "Layer 2 solution", "emoji": "🌱"},
            "avalanche": {"score": 7, "reason": "Eco-friendly consensus", "emoji": "⚡"},
            "algorand": {"score": 9, "reason": "Carbon negative", "emoji": "🌱"},
            "tezos": {"score": 8, "reason": "Low energy PoS", "emoji": "🌱"},
            "chainlink": {"score": 5, "reason": "Runs on Ethereum", "emoji": "⚡"},
            "polkadot": {"score": 7, "reason": "Efficient PoS", "emoji": "⚡"},
            "litecoin": {"score": 4, "reason": "PoW with lower energy", "emoji": "🔥"},
            "dogecoin": {"score": 2, "reason": "High energy PoW", "emoji": "🔥"},
        }
        
        self.top_cryptos = list(self.sustainability_db.keys())

    def get_crypto_data(self, crypto_id: str) -> Optional[Dict[str, Any]]:
        """Fetch real-time crypto data with caching"""
        cache_key = f"{crypto_id}_{int(time.time() // self.cache_duration)}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            url = f"{self.api_base}/simple/price"
            params = {
                'ids': crypto_id,
                'vs_currencies': 'usd',
                'include_24hr_change': 'true',
                'include_market_cap': 'true',
                'include_24hr_vol': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if crypto_id in data:
                self.cache[cache_key] = data[crypto_id]
                return data[crypto_id]
            return None
            
        except Exception as e:
            print(f"⚠️ API Error: {e}")
            return self.get_fallback_data(crypto_id)

    def get_fallback_data(self, crypto_id: str) -> Dict[str, Any]:
        """Fallback data when API fails"""
        fallback_prices = {
            "bitcoin": {"usd": 43500, "usd_24h_change": 2.1},
            "ethereum": {"usd": 2650, "usd_24h_change": 1.8},
            "cardano": {"usd": 0.48, "usd_24h_change": 3.2},
            "solana": {"usd": 98, "usd_24h_change": -1.5}
        }
        return fallback_prices.get(crypto_id, {"usd": 0, "usd_24h_change": 0})

    def analyze_profitability(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Simple profitability analysis"""
        change_24h = data.get('usd_24h_change', 0)
        price = data.get('usd', 0)
        
        if change_24h > 5:
            trend = "🚀 Strong Bull"
            profit_score = 9
        elif change_24h > 2:
            trend = "📈 Rising"
            profit_score = 7
        elif change_24h > -2:
            trend = "➡️ Stable"
            profit_score = 5
        elif change_24h > -5:
            trend = "📉 Declining"
            profit_score = 3
        else:
            trend = "💀 Bearish"
            profit_score = 1
            
        return {
            "trend": trend,
            "score": profit_score,
            "change": change_24h,
            "price": price
        }

    def get_investment_advice(self, crypto_id: str) -> str:
        """Generate investment advice based on rules"""
        data = self.get_crypto_data(crypto_id)
        if not data:
            return f"❌ Sorry, I couldn't find data for {crypto_id}"
        
        profit_analysis = self.analyze_profitability(data)
        sustainability = self.sustainability_db.get(crypto_id, {"score": 5, "reason": "Unknown", "emoji": "❓"})
        
        # Combined scoring logic
        combined_score = (profit_analysis["score"] * 0.6) + (sustainability["score"] * 0.4)
        
        price = profit_analysis["price"]
        change = profit_analysis["change"]
        
        advice = f"📊 **{crypto_id.upper()} Analysis**\n"
        advice += f"💰 Price: ${price:,.2f} ({change:+.1f}% 24h)\n"
        advice += f"📈 Trend: {profit_analysis['trend']}\n"
        advice += f"{sustainability['emoji']} Sustainability: {sustainability['score']}/10 - {sustainability['reason']}\n"
        
        # Investment recommendation logic
        if combined_score >= 8:
            advice += f"✅ **STRONG BUY** - Great combo of growth + sustainability!"
        elif combined_score >= 6:
            advice += f"👍 **CONSIDER** - Decent opportunity with balanced metrics"
        elif combined_score >= 4:
            advice += f"⚠️ **CAUTION** - Mixed signals, high risk"
        else:
            advice += f"❌ **AVOID** - Poor metrics, consider alternatives"
            
        advice += f"\n🎯 Overall Score: {combined_score:.1f}/10"
        return advice

    def handle_query(self, query: str) -> str:
        """Main query processing with if-else logic"""
        query = query.lower().strip()
        
        # Greeting responses
        if any(word in query for word in ['hi', 'hello', 'hey']):
            return "👋 Hey there! I'm CryptoBuddy! Ask me about crypto investments! Try 'help' for suggestions."
        
        # Help responses
        if 'help' in query:
            return """🤖 **CryptoBuddy Help Menu**
• Ask about specific cryptos: 'How's Bitcoin?' or 'Tell me about Ethereum'
• Find sustainable options: 'What's the greenest crypto?'
• Get trending coins: 'What's rising today?'
• Compare options: 'Bitcoin vs Ethereum'
• Type 'list' to see cryptos I know about
• Type 'exit' to quit"""

        # List available cryptos
        if 'list' in query:
            crypto_list = ', '.join([crypto.title() for crypto in self.top_cryptos])
            return f"🪙 **I can analyze these cryptos:**\n{crypto_list}"
        
        # Sustainability queries
        if any(word in query for word in ['green', 'sustainable', 'eco', 'environment']):
            best_sustainable = max(self.sustainability_db.items(), key=lambda x: x[1]['score'])
            crypto_name, data = best_sustainable
            return f"{data['emoji']} **Most Sustainable: {crypto_name.upper()}**\nScore: {data['score']}/10 - {data['reason']}\n\n{self.get_investment_advice(crypto_name)}"
        
        # Trending/rising queries
        if any(word in query for word in ['trending', 'rising', 'hot', 'bull']):
            trending_cryptos = []
            for crypto in self.top_cryptos[:5]:  # Check top 5
                data = self.get_crypto_data(crypto)
                if data and data.get('usd_24h_change', 0) > 2:
                    trending_cryptos.append((crypto, data.get('usd_24h_change', 0)))
            
            if trending_cryptos:
                trending_cryptos.sort(key=lambda x: x[1], reverse=True)
                result = "🚀 **Trending Up Today:**\n"
                for crypto, change in trending_cryptos[:3]:
                    result += f"• {crypto.upper()}: +{change:.1f}%\n"
                return result
            else:
                return "😐 No major gainers today. Market seems quiet!"
        
        # Specific crypto queries
        for crypto in self.top_cryptos:
            if crypto in query or crypto.replace('-', '') in query:
                return self.get_investment_advice(crypto)
        
        # Comparison queries (simple)
        if 'vs' in query or 'compare' in query:
            words = query.split()
            found_cryptos = [word for word in words if word in self.top_cryptos]
            if len(found_cryptos) >= 2:
                crypto1, crypto2 = found_cryptos[0], found_cryptos[1]
                return f"**{crypto1.upper()} vs {crypto2.upper()}:**\n\n{self.get_investment_advice(crypto1)}\n\n---\n\n{self.get_investment_advice(crypto2)}"
        
        # Default response
        return "🤔 I didn't understand that. Try asking about Bitcoin, Ethereum, or type 'help' for suggestions!"

    def run(self):
        """Main chat loop"""
        print("🤖 CryptoBuddy starting up...")
        print("🔗 Connecting to crypto data...")
        print("✅ Ready to help with crypto investment advice!")
        print("⚠️ **DISCLAIMER: This is educational only. Crypto is risky - always DYOR!**\n")
        
        while True:
            try:
                user_input = input("💬 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("👋 Thanks for using CryptoBuddy! Happy investing & remember to DYOR! 🚀")
                    break
                
                if not user_input:
                    continue
                    
                response = self.handle_query(user_input)
                print(f"\n🤖 CryptoBuddy: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 CryptoBuddy shutting down. Stay safe out there! 🚀")
                break
            except Exception as e:
                print(f"😅 Oops! Something went wrong: {e}")

# Run the bot
if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.run()