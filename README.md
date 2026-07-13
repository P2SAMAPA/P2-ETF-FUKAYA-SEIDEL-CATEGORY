# Fukaya-Seidel Category for ETFs

Represents assets as Lagrangians in a symplectic manifold. Intersection Floer homology detects stable pairings between assets. An A∞ category encodes higher-order associative relationships, with mutations corresponding to portfolio rebalancing. The per‑ETF score is the Floer homology rank.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- Lagrangian embedding in phase space (return, momentum)
- Floer homology for stable pairings
- A∞ operations for higher-order relationships
- Score = Floer homology rank (stable intersections)
- Two‑tab Streamlit dashboard (auto best, manual)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-fukaya-seidel-category-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python train.py` (fast)
4. Launch dashboard: `streamlit run streamlit_app.py`

## Interpretation

- High Floer rank → more stable market structure → potential alpha.
- Low Floer rank → fragmented structure.

## Requirements

See `requirements.txt`.
