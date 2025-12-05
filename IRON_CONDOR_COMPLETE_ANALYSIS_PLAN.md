# Kompletter Iron Condor Analyse Plan
## OptionOmega + TradeBlocks Integration

**Version:** 2.0 (Finalisiert)  
**Datum:** 2025-12-05  
**Ziel:** 0DTE SPX Iron Condor Optimierung mit systematischer Regime-Analyse

---

## 📋 Executive Summary

### Analyse-Flow:
```
OptionOmega Backtests → Export CSV Logs → TradeBlocks/Python Analyse
    ↓
Parameter Grid Search (Entry Time, Delta, Width)
    ↓
Regime Correlation (VIX, Market Breadth, Weekday, Hour)
    ↓
Walk-Forward Validation (2024 Out-of-Sample)
    ↓
Final Recommendations mit klaren Entry/Exit Rules
```

### Werkzeuge:
1. **OptionOmega.com** - Backtesting Engine
2. **TradeBlocks.io** - Options Analytics (Python Library)
3. **Custom Python** - Regime Correlation Analysis

---

## 🎯 Ziel

**Finde die optimale 0DTE Iron Condor Konfiguration:**
- Beste Entry Time
- Optimale Delta & Wing Width
- Profit Target / Stop Loss Levels
- Market Regime Filter (VIX, Breadth)

**Success Criteria:**
- CAGR > 15%
- Win Rate > 65%
- Max Drawdown < 20%
- Sharpe Ratio > 1.5
- 2024 Validation positiv

---

## Phase 1: OptionOmega Baseline (Woche 1)

### 1.1 Initial Backtest Setup

**OptionOmega Configuration:**
```yaml
Symbol: SPX
Strategy: Iron Condor
DTE: 0 (0DTE)
Date Range: 2021-01-01 bis 2024-12-31

Position Structure:
  Short Put: 10 Delta
  Long Put: -30 points (linked to short)
  Short Call: 10 Delta
  Long Call: +30 points (linked to short)

Entry Rules:
  Frequency: Daily (Mon-Fri)
  Time: 1:00 PM EST
  Max Concurrent: 1 trade

Exit Rules:
  Profit Target: 50% of credit received
  Stop Loss: 100% of credit (IMSL per side)
  GTC: Yes (good-till-close)

Position Sizing:
  Capital: $50,000
  Contracts: 1 (fixed)
  
Advanced Settings:
  IMSL: Enabled (NBBO + Trades data)
  Punisher: "Two Hits at PT" + "Cap Profits"
  Slippage: $5 per leg
  Commissions: $1.50 per contract
```

**Export:** `baseline_full_2021_2024.csv`

### 1.2 Baseline Metrics zu Dokumentieren

```python
# Metrics aus OptionOmega Export:
{
  "total_trades": ...,
  "win_rate": ...,
  "cagr": ...,
  "max_drawdown": ...,
  "sharpe_ratio": ...,
  "avg_winner": ...,
  "avg_loser": ...,
  "avg_dte_at_entry": ...,
  "avg_credit_received": ...,
  "total_profit": ...
}
```

### 1.3 Friday vs Non-Friday Split

**Test A - Freitags Only:**
```yaml
Entry: Fridays only, 1:00 PM
Export: friday_only_2021_2024.csv
```

**Test B - Mo-Do Only:**
```yaml
Entry: Monday-Thursday, 1:00 PM
Export: weekday_only_2021_2024.csv
```

**Analyse:** Vergleich Win Rate, P&L, Max DD

---

## Phase 2: Parameter Grid Search (Woche 2-3)

### 2.1 Entry Time Optimization

**Variables:**
- Entry Times: 10:00, 11:00, 12:00, 13:00, 14:00, 15:00 EST
- Alle anderen Parameter: Baseline

**Tests:** 6 Backtests  
**Export:** `entry_time_{HH}00_2021_2024.csv`

**Python Analyse Script:**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load all entry time CSVs
results = {}
for hour in [10, 11, 12, 13, 14, 15]:
    df = pd.read_csv(f'entry_time_{hour}00_2021_2024.csv')
    results[hour] = {
        'cagr': ...,
        'win_rate': ...,
        'max_dd': ...,
        'avg_pl': df['pnl'].mean()
    }

# Plot comparison
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# ... visualization code
```

### 2.2 Delta & Wing Width Optimization

**Variables:**
- Short Deltas: 5, 7, 10, 12, 15
- Wing Widths: 20, 25, 30, 35, 40 points
- Entry Time: **Best from 2.1**

**Tests:** 5 × 5 = 25 Backtests  
**Export:** `delta_{D}_width_{W}_2021_2024.csv`

**Grid Search Matrix:**
```
       20pts  25pts  30pts  35pts  40pts
5Δ     [...]  [...]  [...]  [...]  [...]
7Δ     [...]  [...]  [...]  [...]  [...]
10Δ    [...]  [...]  [...]  [...]  [...]
12Δ    [...]  [...]  [...]  [...]  [...]
15Δ    [...]  [...]  [...]  [...]  [...]
```

### 2.3 Profit Target / Stop Loss Optimization

**Variables:**
- PT%: 40%, 50%, 60%, 75%
- SL%: 100%, 150%, 200% (of credit)
- Delta & Width: **Best from 2.2**

**Tests:** 4 × 3 = 12 Backtests  
**Export:** `pt_{PT}_sl_{SL}_2021_2024.csv`

---

## Phase 3: TradeBlocks Integration (Woche 4)

### 3.1 TradeBlocks Installation

```bash
# Install TradeBlocks
pip install tradeblocks --break-system-packages

# Or from GitHub
git clone https://github.com/kai-trading/tradeblocks.git
cd tradeblocks
pip install -e . --break-system-packages
```

### 3.2 CSV Import to TradeBlocks

**TradeBlocks kann:**
- CSV Logs importieren
- Trades visualisieren
- Correlations analysieren
- Greeks analysieren
- Regime-basierte Gruppierung

**Python Example:**
```python
import tradeblocks as tb

# Load OptionOmega CSV export
portfolio = tb.Portfolio.from_csv('baseline_full_2021_2024.csv')

# Analyze
print(portfolio.summary())
print(portfolio.metrics())

# Plot equity curve
portfolio.plot_equity_curve()

# Analyze by weekday
portfolio.group_by('weekday').plot_returns()
```

### 3.3 Advanced Analytics mit TradeBlocks

```python
# 1. Greeks Analysis
portfolio.analyze_greeks()

# 2. Regime Analysis
portfolio.add_market_data('VIX', '^VIX')
portfolio.correlate('pnl', 'VIX')

# 3. Time-of-Day Analysis
portfolio.group_by('entry_hour').summary()

# 4. Win/Loss Patterns
portfolio.analyze_patterns()
```

---

## Phase 4: Regime Correlation Analysis (Woche 4-5)

### 4.1 Data Sources

**Market Regime Indicators:**
1. **VIX** (Volatility)
   - Source: Yahoo Finance
   - Thresholds: <15, 15-20, 20-30, >30

2. **SPX Put/Call Ratio** (Sentiment)
   - Source: CBOE
   - File: `spy_put_call_ratio.csv`

3. **Market Breadth** ($ADD, $TICK)
   - Source: TradingView / IBKR
   - File: `nyse_breadth.csv`

4. **VIX Term Structure**
   - Source: CBOE
   - Calculation: VIX9D / VIX
   - Contango vs Backwardation

### 4.2 Custom Python Analysis

```python
import pandas as pd
import numpy as np

# Load OptionOmega results
trades = pd.read_csv('best_params_2021_2024.csv')

# Load regime data
vix = pd.read_csv('vix_daily_2021_2024.csv', index_col='date', parse_dates=True)
breadth = pd.read_csv('nyse_breadth_2021_2024.csv', index_col='date', parse_dates=True)

# Merge on entry date
trades['entry_date'] = pd.to_datetime(trades['entry_date'])
trades = trades.merge(vix[['close']], left_on='entry_date', right_index=True, how='left')
trades.rename(columns={'close': 'vix_at_entry'}, inplace=True)

# Regime Classification
trades['vix_regime'] = pd.cut(
    trades['vix_at_entry'], 
    bins=[0, 15, 20, 30, 100],
    labels=['Low', 'Medium', 'High', 'Extreme']
)

# Analyze P&L by Regime
regime_analysis = trades.groupby('vix_regime').agg({
    'pnl': ['mean', 'std', 'count'],
    'winner': 'mean'  # win rate
})

print(regime_analysis)

# Correlation Matrix
correlations = trades[['pnl', 'vix_at_entry', 'breadth', 'entry_hour']].corr()
print(correlations)
```

### 4.3 Regime Filter Rules

**Based on Analysis, define:**
```python
# Example Rules (to be derived from data):
ENTRY_RULES = {
    'vix_max': 25,  # Don't enter if VIX > 25
    'vix_min': 12,  # Don't enter if VIX < 12 (too quiet)
    'breadth_min': -500,  # Don't enter if $ADD < -500
    'term_structure': 'contango'  # Only enter if VIX in contango
}
```

---

## Phase 5: Walk-Forward Validation (Woche 5-6)

### 5.1 2024 Out-of-Sample Test

**Setup:**
```yaml
Training Period: 2021-2023 (determine best params)
Validation Period: 2024 (test robustness)
```

**Process:**
1. Find best params on 2021-2023
2. Apply exact same params to 2024
3. Compare performance

### 5.2 Degradation Analysis

```python
# Compare Training vs Validation
training_metrics = {
    'cagr': ...,
    'sharpe': ...,
    'max_dd': ...
}

validation_metrics = {
    'cagr': ...,
    'sharpe': ...,
    'max_dd': ...
}

degradation = {
    key: (validation_metrics[key] - training_metrics[key]) / training_metrics[key]
    for key in training_metrics
}

print(f"Performance Degradation: {degradation}")
# If degradation < 20%, params are robust
```

---

## Phase 6: Custom Signal Generation (Woche 6-7)

### 6.1 OptionOmega Custom Entry Logic

**Option 1: Manual Filter Pre-Trade**
```python
# Run this before each trading day
import yfinance as yf

vix = yf.Ticker("^VIX").history(period="1d")['Close'].iloc[-1]
if vix > 25:
    print("❌ VIX too high, skip today")
else:
    print("✅ Enter Iron Condor today")
```

**Option 2: Export → Filter → Re-backtest**
```python
# 1. Export full trade log from OO
# 2. Filter trades based on regime
trades = pd.read_csv('all_trades_2021_2024.csv')
trades_filtered = trades[
    (trades['vix_at_entry'] >= 12) & 
    (trades['vix_at_entry'] <= 25)
]

# 3. Recalculate metrics
filtered_cagr = calculate_cagr(trades_filtered)
filtered_sharpe = calculate_sharpe(trades_filtered)
```

---

## Phase 7: Final Recommendations (Woche 7)

### 7.1 Optimal Configuration (To Be Determined)

**Example Output (nach Analyse):**
```yaml
Best Iron Condor Configuration:
  Entry Time: 13:00 EST
  Short Delta: 10
  Wing Width: 30 points
  Profit Target: 50% of credit
  Stop Loss: 100% per side
  
Entry Filters:
  VIX: Between 12 and 25
  Day: Monday-Thursday (skip Friday)
  Market Breadth: $ADD > -500
  VIX Term Structure: Contango
  
Expected Performance (2021-2024):
  CAGR: 18.5%
  Sharpe: 1.82
  Max DD: 15.2%
  Win Rate: 68%
  
2024 Validation:
  CAGR: 16.1% (87% of training)
  Sharpe: 1.65
  Max DD: 18.3%
```

### 7.2 Implementation Guide

**Daily Workflow:**
```python
# automated_iron_condor.py
import yfinance as yf
from datetime import datetime

def check_entry_conditions():
    """Check if we should enter today"""
    
    # 1. Check weekday
    if datetime.now().weekday() == 4:  # Friday
        return False, "Skip Friday"
    
    # 2. Check VIX
    vix = yf.Ticker("^VIX").history(period="1d")['Close'].iloc[-1]
    if vix < 12 or vix > 25:
        return False, f"VIX {vix:.1f} out of range [12-25]"
    
    # 3. Check market breadth (would need IBKR API)
    # add_value = get_nyse_breadth()
    # if add_value < -500:
    #     return False, "Poor breadth"
    
    return True, "All conditions met"

# Run at 12:50 PM EST daily
can_enter, reason = check_entry_conditions()
print(f"Entry Decision: {can_enter} - {reason}")
```

---

## 📊 Deliverables

### Weekly Reports

**Week 1:** Baseline Metrics Document
**Week 2-3:** Parameter Optimization Results
**Week 4-5:** Regime Analysis Report
**Week 6:** Custom Signal Performance
**Week 7:** Walk-Forward Validation Report

### Final Deliverable

**Comprehensive Report:**
```
FINAL_IRON_CONDOR_ANALYSIS_REPORT.md

1. Executive Summary
   - Best Parameters
   - Optimal Regimes
   - Expected Performance

2. Methodology
   - Backtest Setup
   - Data Sources
   - Analysis Techniques

3. Results
   - Parameter Sensitivity Analysis
   - Regime Performance Breakdown
   - Walk-Forward Validation

4. Recommendations
   - Trading Rules
   - Entry Criteria
   - Risk Management
   - Position Sizing

5. Implementation Guide
   - Option Omega Setup (exact config)
   - Daily Regime Check Workflow
   - Trade Execution Checklist

6. Appendix
   - All CSV Exports
   - Python Analysis Code
   - Regime Data Sources
```

### Code Repository

**Structure:**
```
/home/carsten/research/iron_condor_analysis/
├── data/
│   ├── option_omega_exports/
│   │   ├── baseline_2021_2024.csv
│   │   ├── entry_time_*.csv
│   │   ├── delta_*_width_*.csv
│   │   └── ...
│   ├── regime_data/
│   │   ├── vix_2021_2024.csv
│   │   ├── market_breadth_2021_2024.csv
│   │   └── vix_term_structure_2021_2024.csv
│   └── custom_signals/
│       └── regime_filtered_entries.csv
├── analysis/
│   ├── analyze_oo_export.py
│   ├── regime_correlation.py
│   ├── parameter_optimization.py
│   └── generate_signals.py
├── notebooks/
│   ├── 01_baseline_analysis.ipynb
│   ├── 02_parameter_grid_search.ipynb
│   ├── 03_regime_analysis.ipynb
│   └── 04_ml_predictions.ipynb
├── reports/
│   ├── weekly_updates/
│   └── FINAL_REPORT.md
└── README.md
```

---

## 🚀 Getting Started

### 1. OptionOmega Access Setup
- [ ] Create/Login to OptionOmega.com account
- [ ] Verify SPX data access
- [ ] Test baseline backtest

### 2. TradeBlocks Installation
```bash
pip install tradeblocks --break-system-packages
# or
git clone https://github.com/kai-trading/tradeblocks.git
cd tradeblocks && pip install -e .
```

### 3. Data Collection Setup
```bash
# Create directory structure
mkdir -p /home/carsten/research/iron_condor_analysis/{data,analysis,reports}

# Setup regime data collection
python -m pip install yfinance pandas --break-system-packages
```

### 4. Run Baseline Test
1. Go to OptionOmega.com
2. Configure baseline (see Phase 1.1)
3. Run backtest
4. Export CSV → Save as `baseline_2021_2024.csv`

---

## 📝 Next Steps

**Immediate Actions:**
1. Verify OptionOmega access
2. Run baseline backtest (Phase 1.1)
3. Export CSV and verify data format
4. Install TradeBlocks
5. Begin entry time optimization (Phase 2.1)

**Questions to Answer:**
- OptionOmega subscription level? (need 0DTE data)
- Access to market breadth data? (IBKR, TradingView)
- Python environment ready on Hetzner?

---

## Success Metrics

**Criteria for "Success":**
1. **Identified Optimal Parameters:** Delta, Entry Time, PT/SL
2. **Regime Rules Defined:** Clear VIX/Breadth thresholds
3. **2024 Validation:** Strategy profitable in 2024 (difficult year)
4. **Practical Implementation:** Automatable via OO
5. **Risk-Adjusted Returns:** Sharpe > 1.5, Max DD < 20%

**Red Flags to Monitor:**
- Parameters too sensitive (slight change = big performance swing)
- Regime rules don't hold in 2024
- Walk-forward shows significant degradation
- Best params contradict research findings

---

**Version:** 2.0 Final  
**Status:** Ready to Execute  
**Estimated Timeline:** 7 Weeks  
**Tools:** OptionOmega + TradeBlocks + Custom Python  
**Location:** `/home/carsten/research/IRON_CONDOR_COMPLETE_ANALYSIS_PLAN.md`

---

**Next:** Start Phase 1.1 - Run Baseline Backtest in OptionOmega
