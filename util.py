"""
StockAgent — Global Configuration
==================================
All simulation parameters live here. Customize freely.

API Keys are loaded from environment variables for security.
Set them in your shell or in a .env file:
  OPENAI_API_KEY=your-key
  GOOGLE_API_KEY=your-key
"""
import os

# ─────────────────────────────────────────────
#   API KEYS (loaded securely from environment)
# ─────────────────────────────────────────────
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")

# ─────────────────────────────────────────────
#   SIMULATION CORE SETTINGS
# ─────────────────────────────────────────────
AGENTS_NUM    = 50     # Number of AI traders in the market
TOTAL_DATE    = 264    # Total trading days (~1 full trading year)
TOTAL_SESSION = 3      # Number of trading sessions per day

# ─────────────────────────────────────────────
#   STOCK INITIAL PRICES
# ─────────────────────────────────────────────
STOCK_A_INITIAL_PRICE = 30   # Company A starting share price
STOCK_B_INITIAL_PRICE = 40   # Company B starting share price

# ─────────────────────────────────────────────
#   AGENT INITIAL WEALTH RANGE
# ─────────────────────────────────────────────
MAX_INITIAL_PROPERTY = 5_000_000.0   # ¥5,000,000 max starting wealth
MIN_INITIAL_PROPERTY =   100_000.0   # ¥100,000   min starting wealth

# ─────────────────────────────────────────────
#   LOAN / CREDIT SYSTEM
# ─────────────────────────────────────────────
LOAN_TYPE      = ["one-month", "two-month", "three-month"]
LOAN_TYPE_DATE = [22, 44, 66]           # Duration in trading days
LOAN_RATE      = [0.027, 0.030, 0.033]  # Annual interest rates by term

# Repayment checkpoints (every 22 trading days = ~1 month)
REPAYMENT_DAYS = [22, 44, 66, 88, 110, 132, 154, 176, 198, 220, 242, 264]

# ─────────────────────────────────────────────
#   QUARTERLY FINANCIAL REPORTS
# ─────────────────────────────────────────────
SEASONAL_DAYS       = 66   # One quarter = 66 trading days
SEASON_REPORT_DAYS  = [12, 78, 144, 210]   # Earnings release days

FINANCIAL_REPORT_A = [
    "Last quarter's financial report of Company A. "
    "Revenue growth rate (YoY): 9.49%, Revenue million: 4483.99, "
    "Gross margin: 41.05%, Income Tax as a percentage of Revenue: 11.31%, "
    "Selling Expense Rate: 6.83%, Management Expense Rate: 3.83%, "
    "Net profit million: 856.67, Depreciation and Amortization: 0.91%, "
    "Capital Expenditures: 2.30%, Changes in working capital: 0.82%, "
    "Cash Flow (million): 756.75",

    "Last quarter's financial report of Company A. "
    "Revenue growth rate (YoY): 7.38%, Revenue million: 4417.79, "
    "Gross margin: 35.68%, Income Tax as a percentage of Revenue: 11.75%, "
    "Selling Expense Rate: 8.13%, Management Expense Rate: 4.62%, "
    "Net profit million: 493.95, Depreciation and Amortization: 1.34%, "
    "Capital Expenditures: 2.68%, Changes in working capital: 0.86%, "
    "Cash Flow (million): 396.53",

    "Last quarter's financial report of Company A. "
    "Revenue growth rate (YoY): 8.70%, Revenue million: 4041.30, "
    "Gross margin: 37.45%, Income Tax as a percentage of Revenue: 9.34%, "
    "Selling Expense Rate: 6.79%, Management Expense Rate: 3.41%, "
    "Net profit million: 724.36, Depreciation and Amortization: 1.27%, "
    "Capital Expenditures: 2.44%, Changes in working capital: 0.94%, "
    "Cash Flow (million): 639.53",

    "Last quarter's financial report of Company A. "
    "Revenue growth rate (YoY): 7.75%, Revenue million: 5024.04, "
    "Gross margin: 42.47%, Income Tax as a percentage of Revenue: 10.67%, "
    "Selling Expense Rate: 6.56%, Management Expense Rate: 4.72%, "
    "Net profit million: 1031.21, Depreciation and Amortization: 1.08%, "
    "Capital Expenditures: 2.71%, Changes in working capital: 0.08%, "
    "Cash Flow (million): 945.50",
]

FINANCIAL_REPORT_B = [
    "Last quarter's financial report of Company B. "
    "Revenue growth rate (YoY): 19.96%, Revenue million: 1319.94, "
    "Gross margin: 31.21%, Income Tax as a percentage of Revenue: 0.70%, "
    "Selling Expense Rate: 4.69%, Management Expense Rate: 8.78%, "
    "Net profit million: 224.92, Depreciation and Amortization: 1.13%, "
    "Capital Expenditures: 1.77%, Changes in working capital: 0.59%, "
    "Cash Flow (million): 208.73",

    "Last quarter's financial report of Company B. "
    "Revenue growth rate (YoY): 19.86%, Revenue million: 1096.70, "
    "Gross margin: 31.26%, Income Tax as a percentage of Revenue: 0.71%, "
    "Selling Expense Rate: 3.62%, Management Expense Rate: 9.90%, "
    "Net profit million: 186.77, Depreciation and Amortization: 0.67%, "
    "Capital Expenditures: 1.44%, Changes in working capital: -0.31%, "
    "Cash Flow (million): 181.69",

    "Last quarter's financial report of Company B. "
    "Revenue growth rate (YoY): 18.21%, Revenue million: 1676.70, "
    "Gross margin: 31.58%, Income Tax as a percentage of Revenue: 0.92%, "
    "Selling Expense Rate: 3.78%, Management Expense Rate: 10.27%, "
    "Net profit million: 278.33, Depreciation and Amortization: 0.77%, "
    "Capital Expenditures: 1.56%, Changes in working capital: -0.06%, "
    "Cash Flow (million): 266.15",

    "Last quarter's financial report of Company B. "
    "Revenue growth rate (YoY): 15.98%, Revenue million: 1075.13, "
    "Gross margin: 32.41%, Income Tax as a percentage of Revenue: 1.08%, "
    "Selling Expense Rate: 3.79%, Management Expense Rate: 10.70%, "
    "Net profit million: 181.16, Depreciation and Amortization: 1.09%, "
    "Capital Expenditures: 2.28%, Changes in working capital: 0.67%, "
    "Cash Flow (million): 161.20",
]

# ─────────────────────────────────────────────
#   SPECIAL MARKET EVENTS
# ─────────────────────────────────────────────

# Event 1: Reserve Ratio Cut — Government eases monetary policy
EVENT_1_DAY     = 78
EVENT_1_MESSAGE = (
    "🏛️  Breaking News: The government has announced a reduction in the "
    "reserve requirement ratio. Lending interest rates have been lowered. "
    "Credit conditions are easing across the market."
)
EVENT_1_LOAN_RATE = [0.024, 0.027, 0.030]  # Reduced rates post-cut

# Event 2: Rate Hike — Government tightens monetary policy
EVENT_2_DAY     = 144
EVENT_2_MESSAGE = (
    "📈  Breaking News: The government has announced an increase in interest "
    "rates. Borrowing costs are rising. Tighter credit conditions ahead."
)
EVENT_2_LOAN_RATE = [0.0255, 0.0285, 0.0315]  # Elevated rates post-hike