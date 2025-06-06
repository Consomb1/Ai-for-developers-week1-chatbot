# protrader.py

print("👋 Welcome to ProTrader - your smart crypto companion!")
print("Ask me anything about trending, sustainable, or profitable cryptocurrencies!")
print("Type 'exit' to leave anytime.\n")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "volatile",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Solana": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7.5/10
    },
    "Polkadot": {
        "price_trend": "rising",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 9/10
    }
}

while True:
    user_query = input("You: ").lower()

    if user_query == "exit":
        print("ProTrader: 🚪 Logging out. Stay sharp, trader!")
        break

    elif "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[recommend]["sustainability_score"] * 10
        print(f"ProTrader: 🌱 Go green with {recommend}! It scores {score:.1f}/10 in sustainability!")

    elif "trending" in user_query or "rising" in user_query:
        rising = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"ProTrader: 🚀 These are trending up: {', '.join(rising)}.")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"ProTrader: 🏆 For long-term growth, go for {coin} — it's rising and backed by strong market cap!")
                break

    elif "recommend" in user_query or "should i buy" in user_query:
        picks = [coin for coin, data in crypto_db.items()
                 if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7]
        print(f"ProTrader: 🤖 Based on trends + eco scores, try: {', '.join(picks)}.")

    elif "wreck" in user_query or "luna" in user_query:
        print("ProTrader: 😬 Oof! No Luna-landings here. Try Cardano or Polkadot—they’re stable, rising, and not headed to the moon… then crashing 🌕")

    elif "market cap" in user_query:
        high_cap = [coin for coin, data in crypto_db.items() if data["market_cap"] == "high"]
        print(f"ProTrader: 💰 These are top market cap coins: {', '.join(high_cap)}.")

    elif "low energy" in user_query or "energy efficient" in user_query:
        low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"ProTrader: 🔋 These coins use low energy: {', '.join(low_energy)}.")

    elif "risk" in user_query or "safe" in user_query:
        print("ProTrader: 🛡️ Solana has a stable trend, low energy use, and decent sustainability—great for cautious investors.")

    elif "innovative" in user_query or "future" in user_query:
        print("ProTrader: 🧠 Polkadot is your bet! Built for Web3, eco-smart, and still climbing the charts 🚀")

    elif "new" in user_query or "beginner" in user_query:
        print("ProTrader: 🐣 Welcome, rookie investor! Start with Cardano — beginner-friendly, eco-focused, and showing solid growth 📈")

    elif "stable" in user_query:
        print("ProTrader: ⚖️ Solana's holding its ground well—less rollercoaster, more cruise mode 🛳️")

    elif "best" in user_query and "overall" in user_query:
        print("ProTrader: 🏅 Cardano wins for balance: good trend, low energy use, and strong sustainability! It’s the all-star 🌟")

    elif "avoid" in user_query or "high energy" in user_query:
        print("ProTrader: ⚠️ Avoid Bitcoin if you're energy-conscious—it’s the gas guzzler of the bunch ⛽🔥")

    elif "green portfolio" in user_query or "build portfolio" in user_query:
        print("ProTrader: 💚 Build your eco-portfolio with Cardano, Solana, and Polkadot. Smart + sustainable = winning combo 🌍")

    elif "eat less" in user_query or "grow more" in user_query:
        print("ProTrader: Haha love the analogy! 🐛➡️🦋 Try Polkadot — small energy appetite, big market dreams!")

    else:
        print("ProTrader: 🤔 Hmm... Try asking about 'sustainable', 'trending', 'safe', or 'recommend'. I'm here for smart crypto advice!")

