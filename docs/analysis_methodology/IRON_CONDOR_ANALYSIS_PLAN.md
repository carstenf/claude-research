# Methodischer Analyseplan: 0DTE Iron Condor Optimierung

## 🎯 Ziel

Systematische Identifikation der optimalen 0DTE Iron Condor Parameter und Market Regime Bedingungen durch:
1. **Option Omega Backtesting** (Parameter Grid Search)
2. **Trade Log Export & Analyse** (Python/TradeBlocks)
3. **Regime Correlation Analysis** (VIX, Breadth, Time)

---

## Phase 1: Baseline Etablierung (Woche 1)

### 1.1 Single Baseline Backtest

**Ziel:** Referenz-Performance etablieren

**Option Omega Setup:**
```
Ticker: SPX
Strategy: Iron Condor
DTE: 0
Date Range: 2021-01-01 bis 2024-12-31

Legs:
- Sell Put: 10 Delta
- Buy Put: -30 points (linked)
- Sell Call: 10 Delta  
- Buy Call: +30 points (linked)

Entry:
- Frequency: Daily (Mon-Fri)
- Time: 1:00 PM EST
- Max Open Trades: 1

Exit:
- Profit Target: 50% of Credit
- Stop Loss: 100% of Credit (per side, IMSL)
- GTC: Yes

Position Sizing:
- Starting Capital: $50,000
- Fixed Contracts: 1
- Allocation: N/A (fixed)

Advanced:
- IMSL: Enabled (NBBO + Trades)
- Punisher: "Two Hits at PT" + "Cap Profits"
- Slippage: $5 per leg
```

**Expected Output:**
- Baseline CAGR
- Win Rate
- Max DD
- Average Winner/Loser
- Total Trades
- **Export CSV:** `baseline_2021_2024.csv`

### 1.2 Friday vs Non-Friday Split

**Rationale:** Freitag-Verhalten anders wegen Wochenend-Gamma

**Test 1:** Nur Freitag (gleiche Parameter)
- CSV Export: `friday_only_2021_2024.csv`

**Test 2:** Mo-Do (gleiche Parameter)
- CSV Export: `non_friday_2021_2024.csv`

**Vergleich:** Win Rate, CAGR, Max DD

---

## Phase 2: Parameter Grid Search (Woche 2-3)

### 2.1 Entry Time Optimization

**Variables:**
- Entry Time: 10:00, 11:00, 12:00, 13:00, 14:00, 15:00
- Alle anderen Parameter: Baseline

**Tests:** 6 Backtests
**CSV Export:** `entry_time_{time}_2021_2024.csv`

**Analyse:**
- Best CAGR by Entry Time
- Win Rate by Entry Time
- Correlation: Entry Time vs Avg P/L

### 2.2 Delta Optimization

**Variables:**
- Short Delta: 5, 7, 10, 12, 15
- Wing Width: 20, 25, 30, 35, 40 points
- Entry Time: Best aus 2.1

**Tests:** 5 (Delta) × 5 (Width) = 25 Backtests
**CSV Export:** `delta_{d}_width_{w}_2021_2024.csv`

**Analyse:**
- Heatmap: Delta vs Width (CAGR)
- Risk/Reward by Delta
- Double Stop-Loss Rate by Delta

### 2.3 Exit Optimization

**Variables:**
- Profit Target: 25%, 50%, 75%, 100% of Credit
- Stop Loss: 75%, 100%, 125%, 150% of Credit
- Best Delta/Width aus 2.2

**Tests:** 4 × 4 = 16 Backtests
**CSV Export:** `pt_{pt}_sl_{sl}_2021_2024.csv`

**Analyse:**
- Sharpe Ratio by PT/SL Combo
- Max DD by PT/SL Combo
- Trade Duration by PT/SL

---

## Phase 3: Market Regime Integration (Woche 4-5)

### 3.1 VIX Data Enrichment

**Source:** Download historical VIX from Yahoo Finance oder CBOE
**Timeframe:** 2021-2024, Daily

**Merge mit Trade Logs:**
```python
import pandas as pd

# Load trade log
trades = pd.read_csv('best_params_2021_2024.csv')
trades['entry_date'] = pd.to_datetime(trades['Opened On'].str.split(' ').str[0])

# Load VIX
vix = pd.read_csv('VIX_2021_2024.csv')
vix['Date'] = pd.to_datetime(vix['Date'])

# Merge
trades_with_vix = trades.merge(
    vix[['Date', 'Close']], 
    left_on='entry_date', 
    right_on='Date', 
    how='left'
)
trades_with_vix.rename(columns={'Close': 'VIX_Entry'}, inplace=True)
```

**Regime Classification:**
```python
def classify_vix_regime(vix):
    if vix < 15:
        return 'LOW'
    elif vix < 25:
        return 'MEDIUM'
    else:
        return 'HIGH'

trades_with_vix['VIX_Regime'] = trades_with_vix['VIX_Entry'].apply(classify_vix_regime)
```

### 3.2 Market Breadth Data

**Source:** 
- % SPX Stocks > 200 MA (FinViz historical oder manual tracking)
- Alternativ: SPY vs 200 MA als Proxy

**Add to Trades:**
```python
# Load breadth data
breadth = pd.read_csv('market_breadth_2021_2024.csv')

trades_with_regime = trades_with_vix.merge(
    breadth[['Date', 'Pct_Above_200MA']], 
    left_on='entry_date',
    right_on='Date',
    how='left'
)

# Classify
def classify_breadth(pct):
    if pct > 70:
        return 'STRONG'
    elif pct > 50:
        return 'NEUTRAL'
    else:
        return 'WEAK'

trades_with_regime['Breadth'] = trades_with_regime['Pct_Above_200MA'].apply(classify_breadth)
```

### 3.3 VIX Term Structure

**Source:** VX Futures Data (CBOE)
**Calculate:** VX1 vs VX2 (Contango/Backwardation)

```python
def classify_term_structure(vx1, vx2):
    ratio = vx2 / vx1
    if ratio > 1.05:
        return 'CONTANGO'
    elif ratio < 0.95:
        return 'BACKWARDATION'
    else:
        return 'FLAT'
```

### 3.4 Composite Regime Analysis

**Final DataFrame:**
```
| Entry Date | Entry Time | P/L | VIX | VIX_Regime | Breadth | Term_Structure | Winner |
|------------|------------|-----|-----|------------|---------|----------------|--------|
| 2021-01-04 | 13:00      | 150 | 18  | MEDIUM     | STRONG  | CONTANGO       | True   |
```

**Analyses:**

1. **Win Rate by Regime:**
```python
win_rate_by_regime = trades_with_regime.groupby('VIX_Regime')['Winner'].mean()
# Expected: LOW > MEDIUM > HIGH
```

2. **Average P/L by Regime:**
```python
avg_pl_by_regime = trades_with_regime.groupby('VIX_Regime')['P/L'].mean()
```

3. **Double Stop-Loss Rate:**
```python
# Identify double stop-losses (both legs hit)
# Logic: Loss > 150% of expected single-leg loss
dsl_rate_by_regime = ...
```

4. **Heatmap: VIX × Breadth**
```python
import seaborn as sns
pivot = trades_with_regime.pivot_table(
    values='P/L', 
    index='VIX_Regime', 
    columns='Breadth', 
    aggfunc='mean'
)
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='RdYlGn')
```

5. **Time-of-Day × VIX Interaction:**
```python
# Group by Entry Hour and VIX Regime
time_vix_perf = trades_with_regime.groupby(['Entry_Hour', 'VIX_Regime'])['P/L'].mean()
```

---

## Phase 4: Custom Signal Testing (Woche 6)

### 4.1 Regime-Filtered Entry Signals

**Goal:** Nur Trade bei optimalen Regimes

**CSV Generation:**
```python
# Filter: VIX < 20 & Breadth > 50%
optimal_days = regime_data[
    (regime_data['VIX'] < 20) & 
    (regime_data['Breadth_Pct'] > 50)
]['Date']

# Generate OO Custom Signals CSV
signals = pd.DataFrame({
    'entryDate': optimal_days,
    'entryTime': '13:00'  # Best time from Phase 2
})
signals.to_csv('regime_filtered_entries.csv', index=False)
```

**Option Omega:**
- Use "Custom Signals Tester"
- Upload `regime_filtered_entries.csv`
- Same Iron Condor params as best from Phase 2
- Compare vs Baseline (all days)

**Expected:** Higher Win Rate, Lower DD

### 4.2 Dynamic Parameter Switching

**Advanced:** Different params for different regimes

**Low VIX (< 15) CSV:**
```
entryDate,entryTime,shortCallStrike,longCallStrike,shortPutStrike,longPutStrike
2021-01-05,13:00,4200,4230,4000,3970
```
- Tighter Spreads (higher premium, higher risk)

**Medium VIX (15-25) CSV:**
- Standard Spreads

**Don't Trade High VIX (> 25)**

---

## Phase 5: Walk-Forward Analysis (Woche 7)

### 5.1 Rolling Window Backtest

**Rationale:** Avoid Look-Ahead Bias

**Method:**
1. Train: 2021-2022 → Optimize Parameters
2. Test: 2023 → Apply best params
3. Train: 2022-2023 → Re-optimize
4. Test: 2024 → Apply

**Implementation:**
- 4 separate OO Backtests
- Document parameter drift
- Check if "best params" stable over time

### 5.2 Out-of-Sample Validation

**2024 Only Test:**
- Use FINAL optimized params from Phase 2-4
- Test on 2024 data ONLY
- Compare vs 2024 research findings (10.5% Double SL rate)

**Critical Question:**
"Hätte diese Strategie 2024 funktioniert?"

---

## Phase 6: Python Analysis Pipeline (Ongoing)

### 6.1 Automated Trade Log Processing

**Script:** `analyze_oo_export.py`

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class IronCondorAnalyzer:
    def __init__(self, csv_path, vix_path=None, breadth_path=None):
        self.trades = pd.read_csv(csv_path)
        self.vix = pd.read_csv(vix_path) if vix_path else None
        self.breadth = pd.read_csv(breadth_path) if breadth_path else None
        self._preprocess()
    
    def _preprocess(self):
        # Parse dates/times
        # Merge regime data
        # Calculate metrics
        pass
    
    def performance_summary(self):
        return {
            'total_trades': len(self.trades),
            'win_rate': self.trades['Winner'].mean(),
            'avg_win': self.trades[self.trades['Winner']]['P/L'].mean(),
            'avg_loss': self.trades[~self.trades['Winner']]['P/L'].mean(),
            'sharpe': ...,
            'max_dd': ...,
        }
    
    def regime_analysis(self):
        # Group by VIX/Breadth regimes
        # Return performance by regime
        pass
    
    def plot_equity_curve(self):
        # Cumulative P/L over time
        pass
    
    def plot_regime_heatmap(self):
        # VIX × Breadth performance heatmap
        pass
    
    def identify_best_conditions(self, metric='sharpe'):
        # Return optimal entry conditions
        pass
    
    def generate_entry_signals_csv(self, criteria):
        # Output CSV for OO Custom Signals
        pass
```

### 6.2 Correlation Analysis

**Metrics:**
- Spearman Correlation: VIX vs P/L
- Pearson Correlation: Entry Time vs P/L
- Chi-Square: Day of Week vs Winner

### 6.3 Machine Learning (Optional - Advanced)

**Goal:** Predict Trade Outcome

**Features:**
- VIX (current, 5-day MA, 20-day MA)
- VIX Term Structure (VX1/VX2 ratio)
- Breadth (%, change)
- SPX vs 200 MA (distance %)
- Day of Week
- Entry Time
- Recent Volatility (ATR)

**Target:** Binary (Win/Loss) oder Regression (P/L)

**Model:** Random Forest, XGBoost, or Logistic Regression

**Validation:** Walk-forward (2021-2022 train → 2023 test)

---

## Phase 7: TradeBlocks Integration (Falls verfügbar)

**Pending:** TradeBlocks GitHub Code Review

**Anticipated Features:**
- Portfolio Simulation
- Greeks Tracking over Trade Life
- Risk Analytics
- Regime-specific Performance Dashboards

**Action:** Once TradeBlocks docs found, integrate pipeline

---

## Deliverables

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

**Next Step:** 
1. Establish OptionOmega Access
2. Run Baseline Backtest (Phase 1.1)
3. Export CSV
4. Setup Python Environment
5. Begin Analysis

