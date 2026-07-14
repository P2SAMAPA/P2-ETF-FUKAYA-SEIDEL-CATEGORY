import os

HF_TOKEN = os.environ.get("HF_TOKEN", "")
DATA_REPO = "P2SAMAPA/fi-etf-macro-signal-master-data"
OUTPUT_REPO = "P2SAMAPA/p2-etf-fukaya-seidel-category-results"

WINDOWS = [63, 252, 504, 1008, 2016, 4032, 4536]

UNIVERSES = {
    "FI_COMMODITIES": ["TLT", "VCIT", "LQD", "HYG", "VNQ", "GLD", "SLV"],
    "EQUITY_SECTORS": [
        "SPY", "QQQ", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "SMH", "SOXX", "XLB",
        "XLP", "XLU", "GDX", "XME", "IWF", "XSD", "XBI", "IWM", "IWD", "IWO"
    ],
    "COMBINED": [
        "TLT", "VCIT", "LQD", "HYG", "VNQ", "GLD", "SLV",
        "SPY", "QQQ", "XLK", "XLF", "XLE", "XLV", "XLI", "XLY", "SMH", "SOXX", "XLB",
        "XLP", "XLU", "GDX", "XME", "IWF", "XSD", "XBI", "IWM", "IWD", "IWO"
    ]
}

# All available macro variables
MACRO_VARS = [
    "VIX", "DXY", "T10Y2Y", "TBILL_3M",
    "DGS1MO", "DGS3MO", "DGS6MO", "DGS1", "DGS2", "DGS5", "DGS7",
    "DGS10", "DGS20", "DGS30"
]

# Fukaya-Seidel parameters
FLOER_THRESHOLD = 0.3        # threshold for Floer homology detection
A_INFITY_ORDER = 3           # order of A∞ operations
TOP_N = 3
