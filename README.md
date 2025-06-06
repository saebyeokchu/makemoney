# 💸 MakeMoney

**MakeMoney** is an automated economic signal collector and ETF decision assistant.  
It surfs various financial and economic websites, analyzes daily macroeconomic indicators, and generates plain-text summaries that can be used to support ETF investment decisions.

---

## 🧠 Project Goals

- 📊 **Collect daily economic data** from multiple sources
- 🤖 **Analyze** indicators like inflation, interest rates, commodity prices, etc.
- 📁 **Generate readable reports** to help decide whether to invest in specific ETFs
- 🧱 Designed as a modular foundation for a future AI-based investment assistant

---

## 🔧 Features

- 🌐 Web crawling with Python (e.g., `urllib`, `requests`, `BeautifulSoup`)
- 📈 Rule-based signal interpretation (e.g., if CPI rises → negative for bonds)
- 🧾 Outputs a simple `.txt` report with summarized insights
- 📦 Clean modular structure for extension (e.g., AI/ML models later)

---

## 📁 Project Structure

```bash
makemoney/
├── analyze.py         # Main script for scraping and analyzing economic data
├── toTextFile.py      # Converts analysis results into a plain .txt report
├── output/
│   └── result.txt     # Final summary file generated by toTextFile.py
├── utils/             # (Optional) Helper functions for scraping, formatting, etc.
├── README.md
```

---

## 🚀 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/saebyeokchu/makemoney.git
cd makemoney
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, the key libraries used may include:  
> `beautifulsoup4`, `requests`, `pandas`, `lxml`, etc.

### 3. Run Data Collection and Analysis

```bash
python analyze.py
```

- This script collects up-to-date economic signals and applies simple decision logic.

### 4. Generate Report

```bash
python toTextFile.py
```

- The output report (e.g., `output/result.txt`) will summarize the day's signals and suggest whether certain ETFs are favorable.

---

## 📈 Example Use Case

**Scenario**:  
- Inflation data rises  
- Bond yields spike  
- USD strengthens

**Result**:
```txt
[오늘의 경제 요약]
- 물가 지표 상승 → 채권에 부정적
- 금리 인상 가능성 존재
- ETF 'TIP'(물가연동채권)은 주의 필요

[추천]
- 오늘은 주식형 ETF보다 단기채권 또는 현금 비중 확대가 유리
```

---

## 🧩 Next Steps

- [ ] Add support for more economic sources (e.g., Fed, KDI, Bloomberg)
- [ ] Incorporate AI/ML for pattern recognition and backtesting
- [ ] Add portfolio simulation module

---

## 🙌 Contribution

If you have ideas on how to improve signal interpretation, or want to integrate this with a frontend/notification system, feel free to fork and PR!

---

## 📄 License

MIT License

---

Developed by [@saebyeokchu](https://github.com/saebyeokchu) 🌅  
Focused on building accessible, explainable financial tools.
```
