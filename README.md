# 📈 Binance Futures Trading Bot (Testnet)

## 🧠 Overview
This project is a CLI-based Python trading bot that interacts with the **Binance Futures Testnet (USDT-M)** to place MARKET and LIMIT orders.

The application is designed with a clean modular architecture, proper logging, and robust error handling, as required in the assignment.

---

## ⚙️ Features

- ✅ Place **MARKET** and **LIMIT** orders  
- ✅ Supports both **BUY** and **SELL**  
- ✅ Command-line interface using `argparse`  
- ✅ Input validation (order type, price, etc.)  
- ✅ Structured code (client layer + CLI layer)  
- ✅ Logging of:
  - API requests
  - API responses
  - Errors  
- ✅ Exception handling (invalid input, API errors, network issues)

---

## 🏗️ Project Structure


trading-bot/



├── client/

│ ├── init.py

│ └── binance_client.py # Binance API wrapper



├── cli/

│ ├── init.py

│ └── main.py # CLI entry point



├── logs/

│ └── bot.log # Execution logs



├── screenshots/ 



├── requirements.txt

└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/palash-sadhwani/trading-bot.git

cd trading-bot


---

### 2️⃣ Install Dependencies

pip install -r requirements.txt


---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:


API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key


> ⚠️ Note: This project uses **Binance Futures Testnet** (`testnet=True`), so no real funds are involved.

---

## ▶️ Usage

### 🔹 MARKET Order

python -m cli.main --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01


---

### 🔹 LIMIT Order

python -m cli.main --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000


---

## 📊 Sample Output


Order Request:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01, 'price': None}

Order Success:
Order ID: 12878510173
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00


---

## 📝 Logging

All API interactions and errors are logged in:


logs/bot.log


Includes:
- Order parameters
- API responses
- Error messages

---

## ⚠️ Assumptions & Notes

- Binance Futures **Testnet** is used for safe testing.
- MARKET orders may show status as `NEW` due to **simulated liquidity** in testnet.
- LIMIT orders must follow market rules:
  - SELL price ≥ market price
  - BUY price ≤ market price

---

## 🚧 Error Handling

The application handles:
- Invalid CLI inputs
- Missing price for LIMIT orders
- Binance API errors (e.g., invalid price)
- Network/API failures

---

## 🎯 Evaluation Criteria Coverage

| Requirement | Status |
|------------|--------|
| MARKET orders | ✅ |
| LIMIT orders | ✅ |
| BUY/SELL support | ✅ |
| CLI input | ✅ |
| Logging | ✅ |
| Error handling | ✅ |
| Clean structure | ✅ |

---

## 📌 Future Improvements

- Add Stop-Limit / OCO order support  
- Enhanced CLI (interactive prompts)  
- Real-time price fetching before order validation  
- Web UI dashboard  

---

## 👨‍💻 Author

**Palash Sadhwani**  
