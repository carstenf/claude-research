# Option Omega - Key Features Zusammenfassung

## Backtesting Capabilities

### Data Range
- **Historical Data:** 1/1/2013 - gestern
- **Update Frequency:** Täglich vor Market Open (meist 3 AM)
- **Ticker Support:** SPX, SPY, QQQ, und mehr
- **0DTE Support:** SPX/SPY mit Intraday Minute-by-Minute Simulation (IMSL)

### Strategy Setup

**Leg Configuration:**
- Custom multi-leg strategies
- Linked Legs für Spreads (z.B. 10-wide Put Spread)
- Strike Selection: Delta, Fixed, Percentage
- DTE: Exact oder Range

**Entry Conditions:**
- Time-based: Specific time oder Market Open/Close relative
- Frequency: Daily, Weekly (selected days), Monthly, Specific Dates
- Technical Indicators: SPX-based (using official CBOE data)
- Custom Signals Tester: CSV upload für eigene Entry/Exit Signals

**Exit Conditions:**
- Profit Target: Fixed $, % of Credit, Trailing
- Stop Loss: Fixed $, % of Credit, Trailing, IMSL (Intraday)
- Time-based: DTE, Specific Time
- GTC (Good Till Close)

### Advanced Features

**IMSL (Intraday Minute Stop Loss):**
- Nur für SPX/SPY 0DTE
- Nutzt High/Low jeder Minute
- NBBO only oder NBBO + Trades
- Precision Stop-Loss Testing

**The Punisher:**
- "Two Hits at PT": Profit Target nur wenn 2x erreicht
- "Cap Profits": Limitiere unrealistische Profits
- Slippage Control

**Position Sizing:**
- Starting Capital
- Allocation %
- Max Open Trades
- Fixed Contracts (override allocation)

**Custom Signals Tester:**
- CSV Upload für:
  - Entry Time Only
  - Entry + Exit Time
  - Entry + Strikes
  - Entry + Exit + Strikes (Full Custom)

### Results & Metrics

**Performance Metrics:**
- P/L (Total)
- CAGR (Compound Annual Growth Rate)
- Max Drawdown (EOD-based)
- Average per Trade
- Average Winner/Loser per Lot
- Max Winner/Loser
- Average Days in Trade
- Win Rate
- Net Liquidity

**Trade Log:**
- Opened On (Date, Time)
- Opening Price
- P/L per Trade
- Max Loss % (während Trade)
- Max Profit % (während Trade)
- Leg Details (Quantity, Date, Strike, Type)

**Export:**
- CSV Export für weitere Analyse
- Save/Share Backtests
- Tagging System für Organization

## Automation (Production Trading)

**Broker Support:**
- Tradier
- Schwab (ToS)
- tastytrade

**Features:**
- Cloud-based (kein Local PC nötig)
- Strategy from Backtester → Live
- Order Management (PT, SL, Trailing)
- 7-Day Reauthorization Required

## Wichtige Einschränkungen

1. **0DTE IMSL** nur für SPX/SPY
2. **Technical Indicators** nutzen CBOE:SPX (nicht SPY/ES)
3. **Different Days:** Freitag vs andere Tage separat testen (wegen 1DTE Behavior)
4. **Slippage:** Manuell einstellen für Realism
5. **Max Open Trades:** Limitiert parallel offene Positionen

## Best Practices (aus Doku)

1. **Separate Tests für Different Days** (Freitag vs andere)
2. **Use "The Punisher"** für realistische Results
3. **IMSL für 0DTE** wenn Intraday Stops kritisch
4. **Slippage einrechnen** (realistic fills)
5. **Allocation vernünftig** (nicht 100% bei hoher Win Rate → unrealistic scaling)

---

**Source:** docs.optionomega.com
**Relevanz:** Critical für Iron Condor 0DTE Backtesting
