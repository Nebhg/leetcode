"""
MILLENNIUM MANAGEMENT — Data Operations Analyst
Mock Technical Challenge: Market Data Feed Validation

You've just been handed a raw market data feed that's been ingested from a vendor
into the systematic trading team's infrastructure. Before this data can be used by
any trading strategy, it needs to pass a quality check.

Your job is to write the validation layer.

Time: 45 minutes
Language: Python (no pandas — use plain Python)

---

The data below is a feed of minute-bar OHLCV (Open, High, Low, Close, Volume)
records for a set of equities. Each record represents one minute of trading.

Fields:
  - ticker:     instrument identifier
  - timestamp:  UTC datetime string, format 'YYYY-MM-DD HH:MM'
  - open:       opening price
  - high:       highest price in the bar
  - low:        lowest price in the bar
  - close:      closing price
  - volume:     shares traded

The feed has several real-world data quality problems baked in.
Your job is to find them.

---

TASKS (complete in order — don't jump ahead)

1. Write a function `find_duplicates(feed)` that returns all records where
   (ticker, timestamp) is duplicated. Return a list of (ticker, timestamp) tuples.

2. Write a function `find_stale_prices(feed, threshold=3)` that returns all tickers
   where the close price is identical for `threshold` or more consecutive bars.
   Stale price = the feed stopped updating but kept sending the last known value.
   Return a dict: {ticker: [(start_timestamp, end_timestamp, price), ...]}

3. Write a function `find_ohlc_violations(feed)` that returns all records where
   the OHLCV data is internally inconsistent. Violations:
   - high < low
   - open not between low and high (inclusive)
   - close not between low and high (inclusive)
   - volume < 0
   Return a list of dicts with 'ticker', 'timestamp', and 'reason'.

4. Write a function `find_gaps(feed, expected_interval_minutes=1)` that returns
   all tickers where there is a gap in the time series larger than expected.
   Return a dict: {ticker: [(gap_start, gap_end, gap_minutes), ...]}

5. Write a function `run_quality_report(feed)` that calls all four functions above
   and prints a clean summary report. Format it like you'd hand it to a quant
   researcher who needs to decide whether to use this data.

---

STRETCH (if you finish early)

6. Write a function `find_price_outliers(feed, z_threshold=3.0)` that flags bars
   where the close price is more than `z_threshold` standard deviations from the
   mean close price for that ticker. No external libraries — compute mean and std
   from scratch.

---
"""

# ============================================================
# MOCK DATA — do not modify
# ============================================================

FEED = [
    # --- AAPL bars (clean data to start) ---
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:30", "open": 185.20, "high": 185.75, "low": 184.90, "close": 185.50, "volume": 120000},
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:31", "open": 185.50, "high": 186.10, "low": 185.30, "close": 185.90, "volume": 98000},
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:32", "open": 185.90, "high": 186.20, "low": 185.60, "close": 186.00, "volume": 87000},
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:33", "open": 186.00, "high": 186.50, "low": 185.80, "close": 186.30, "volume": 102000},
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:34", "open": 186.30, "high": 186.80, "low": 186.10, "close": 186.70, "volume": 95000},

    # --- AAPL duplicate record (same ticker + timestamp, different close) ---
    {"ticker": "AAPL", "timestamp": "2024-01-15 09:33", "open": 186.00, "high": 186.50, "low": 185.80, "close": 186.35, "volume": 103000},

    # --- MSFT bars with a gap (09:32 is missing) ---
    {"ticker": "MSFT", "timestamp": "2024-01-15 09:30", "open": 374.10, "high": 374.80, "low": 373.90, "close": 374.50, "volume": 85000},
    {"ticker": "MSFT", "timestamp": "2024-01-15 09:31", "open": 374.50, "high": 375.20, "low": 374.30, "close": 375.00, "volume": 79000},
    # 09:32 missing — gap
    {"ticker": "MSFT", "timestamp": "2024-01-15 09:33", "open": 375.10, "high": 375.60, "low": 374.80, "close": 375.40, "volume": 91000},
    {"ticker": "MSFT", "timestamp": "2024-01-15 09:34", "open": 375.40, "high": 375.90, "low": 375.20, "close": 375.70, "volume": 88000},

    # --- TSLA bars with stale prices (close stuck at 245.30 for 4 bars) ---
    {"ticker": "TSLA", "timestamp": "2024-01-15 09:30", "open": 245.00, "high": 245.80, "low": 244.70, "close": 245.30, "volume": 210000},
    {"ticker": "TSLA", "timestamp": "2024-01-15 09:31", "open": 245.30, "high": 245.60, "low": 245.10, "close": 245.30, "volume": 198000},  # stale
    {"ticker": "TSLA", "timestamp": "2024-01-15 09:32", "open": 245.30, "high": 245.50, "low": 245.10, "close": 245.30, "volume": 175000},  # stale
    {"ticker": "TSLA", "timestamp": "2024-01-15 09:33", "open": 245.30, "high": 245.40, "low": 245.10, "close": 245.30, "volume": 162000},  # stale
    {"ticker": "TSLA", "timestamp": "2024-01-15 09:34", "open": 245.30, "high": 246.10, "low": 245.20, "close": 245.90, "volume": 220000},  # price moves again

    # --- NVDA bars with an OHLC violation ---
    {"ticker": "NVDA", "timestamp": "2024-01-15 09:30", "open": 612.00, "high": 613.50, "low": 611.50, "close": 612.80, "volume": 305000},
    {"ticker": "NVDA", "timestamp": "2024-01-15 09:31", "open": 612.80, "high": 610.00, "low": 613.50, "close": 611.00, "volume": 290000},  # high < low — violation
    {"ticker": "NVDA", "timestamp": "2024-01-15 09:32", "open": 612.00, "high": 614.00, "low": 611.00, "close": 615.50, "volume": 278000},  # close > high — violation
    {"ticker": "NVDA", "timestamp": "2024-01-15 09:33", "open": 613.00, "high": 614.50, "low": 611.80, "close": 613.90, "volume": 265000},
    {"ticker": "NVDA", "timestamp": "2024-01-15 09:34", "open": 613.90, "high": 614.80, "low": 613.50, "close": 614.20, "volume": 258000},

    # --- GOOGL bars with a price outlier and a volume violation ---
    {"ticker": "GOOGL", "timestamp": "2024-01-15 09:30", "open": 141.20, "high": 141.80, "low": 140.90, "close": 141.50, "volume": 62000},
    {"ticker": "GOOGL", "timestamp": "2024-01-15 09:31", "open": 141.50, "high": 142.10, "low": 141.30, "close": 141.90, "volume": 58000},
    {"ticker": "GOOGL", "timestamp": "2024-01-15 09:32", "open": 141.90, "high": 142.30, "low": 141.70, "close": 198.40, "volume": 71000},  # close is an outlier
    {"ticker": "GOOGL", "timestamp": "2024-01-15 09:33", "open": 142.00, "high": 142.50, "low": 141.80, "close": 142.20, "volume": -500},   # negative volume — violation
    {"ticker": "GOOGL", "timestamp": "2024-01-15 09:34", "open": 142.20, "high": 142.70, "low": 142.00, "close": 142.50, "volume": 67000},
]


# ============================================================
# YOUR CODE BELOW
# ============================================================

def find_duplicates(feed):
    """
    Return a list of (ticker, timestamp) tuples that appear more than once.
    """
    pass


def find_stale_prices(feed, threshold=3):
    """
    Return a dict of tickers where close price is identical for `threshold`
    or more consecutive bars.
    Format: {ticker: [(start_timestamp, end_timestamp, price), ...]}
    """
    pass


def find_ohlc_violations(feed):
    """
    Return a list of dicts for records with internal OHLCV inconsistencies.
    Each dict: {'ticker': ..., 'timestamp': ..., 'reason': ...}
    """
    pass


def find_gaps(feed, expected_interval_minutes=1):
    """
    Return a dict of tickers where time series has a gap larger than expected.
    Format: {ticker: [(gap_start, gap_end, gap_minutes), ...]}
    Hint: you'll need to parse timestamps and compute differences.
    """
    pass


def run_quality_report(feed):
    """
    Run all checks and print a clean summary.
    """
    pass


# ============================================================
# STRETCH
# ============================================================

def find_price_outliers(feed, z_threshold=3.0):
    """
    Flag bars where close is more than z_threshold standard deviations
    from the mean close for that ticker. No pandas or scipy.
    """
    pass


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    run_quality_report(FEED)
