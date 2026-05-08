# 🤖 Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## 📁 Project Structure

```
trading_bot/
  bot/
    __init__.py         # Package marker
    client.py           # Binance API client (signs & sends requests)
    orders.py           # Order building, sending & display logic
    validators.py       # Input validation
    logging_config.py   # Logging setup (file + console)
  cli.py                # CLI entry point (you run this!)
  .env                  # Your API keys (you create this!)
  README.md
  requirements.txt
```

---

## ⚙️ Setup Steps

### 1. Clone or download the project
```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Binance Futures Testnet API Keys
1. Go to: https://testnet.binancefuture.com
2. Log in / Register
3. Go to **API Management**
4. Generate your API Key and Secret

### 5. Create a `.env` file in the project root
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

---

## 🚀 How to Run

### ✅ Place a MARKET BUY order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### ✅ Place a MARKET SELL order
```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

### ✅ Place a LIMIT BUY order
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

### ✅ Place a LIMIT SELL order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

### ❓ See help
```bash
python cli.py --help
```

---

## 📤 Example Output

```
🤖 Binance Futures Testnet Trading Bot Starting...

==================================================
         📦 ORDER REQUEST SUMMARY
==================================================
  Symbol     : BTCUSDT
  Side       : BUY
  Order Type : MARKET
  Quantity   : 0.01
==================================================

==================================================
         ✅ ORDER RESPONSE
==================================================
  Order ID     : 123456789
  Symbol       : BTCUSDT
  Status       : FILLED
  Side         : BUY
  Type         : MARKET
  Quantity     : 0.01
  Executed Qty : 0.01
  Avg Price    : 65000.50
==================================================
  🎉 Order placed successfully!
==================================================
```

---

## 📒 Log File

All activity is saved to `trading_bot.log` in the project root.

Example log entries:
```
2024-01-15 10:30:45 | INFO | validators | ✅ Inputs validated — BUY MARKET | BTCUSDT | Qty: 0.01
2024-01-15 10:30:45 | INFO | orders | 📋 Order Request → BUY MARKET | Symbol: BTCUSDT | Qty: 0.01
2024-01-15 10:30:46 | INFO | orders | 📥 Order Response → OrderID: 123456789 | Status: FILLED | ExecutedQty: 0.01 | AvgPrice: 65000.50
```

---

## 🛡️ Error Handling

| Scenario | What happens |
|---|---|
| Missing API keys | Bot exits with clear message |
| Invalid side/type | Validation error shown |
| Missing price for LIMIT | Validation error shown |
| Binance API error | Error details shown + logged |
| Network failure | Clear network error message |

---

## 📝 Assumptions

- Uses Binance Futures **Testnet** only (fake money, safe to test)
- Testnet base URL: `https://testnet.binancefuture.com`
- LIMIT orders use `timeInForce=GTC` (Good Till Cancelled) by default
- Minimum quantity and price precision depends on the symbol's exchange info
- API keys are stored in a `.env` file (never hardcoded)

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `requests` | HTTP calls to Binance API |
| `python-dotenv` | Load API keys from `.env` file |
| `argparse` | Parse CLI arguments |
