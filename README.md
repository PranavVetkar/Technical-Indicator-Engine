# 📊 Technical Indicator Engine (Crypto)

A Python-based technical analysis engine that fetches historical cryptocurrency market data from **Binance** using **CCXT**, computes popular technical indicators, and generates simple **BUY / SELL / HOLD** trading signals.

This project is designed for **learning, experimentation, and rapid prototyping** of rule-based trading logic.

---

## 🚀 Features

- 📈 Fetches **historical OHLCV candle data** from Binance
- 📊 Computes key technical indicators:
  - Simple Moving Averages (SMA – Fast & Slow)
  - Relative Strength Index (RSI)
- 🧠 Generates **basic trading signals** based on trend & momentum
- 🧩 Modular and easy-to-extend architecture
- ⚡ Lightweight and beginner-friendly

---

## 🏦 Exchange Used

- **Binance** (via CCXT)

> Can be extended to any CCXT-supported exchange.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT** – Exchange API abstraction
- **Pandas** – Data processing & indicator computation

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Technical-Indicator-Engine.git
cd Technical-Indicator-Engine
