# ACER-CORE-Virtual-Hub-Simulation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.16547945-blue.svg)](https://doi.org/10.5281/zenodo.16547945)

This repository contains the complete code, data, and analysis accompanying the research paper:

**"Simulation of a virtual hub CORE and its impact on cross-border PPAs"**

*Authors:* Martin Tichý, Marek Miltner, Ondřej Štogl, Július Bemš  
*Institution:* Faculty of Electrical Engineering, CTU in Prague  
*Journal:* IEEE Access (to be published)

## 📋 Abstract

This article explores the potential of a Virtual Trading Hub (VTH) for the CORE region to reduce basis risk in cross-border Power Purchase Agreements (PPAs). A model PPA is developed between a Dutch wind energy producer and a Czech offtaker to simulate realistic contract conditions. The analysis compares three reference market scenarios: the producer's local market (Netherlands), the DE-LU bidding zone, and a simulated CORE VTH constructed as a volume-weighted average of spot prices across the region. The study introduces and quantifies "decoupling loss" as the key metric for measuring financial exposure due to market price divergence, both on observed historical data and on expanded stochastically simulated theoretical scenarios. Results show that the VTH scenario exhibits the strongest correlation with both counterparties' markets and significantly lower volatility in decoupling losses compared to the DE-LU reference, suggesting lower hedging costs and improved bankability.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- 8GB+ RAM (recommended for large simulations)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ACER-CORE-Virtual-Hub-Simulation.git
   cd ACER-CORE-Virtual-Hub-Simulation
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

1. **Data Processing:**
   ```bash
   python data/clean_data.ipynb
   ```

2. **AI-Powered Data Generation:**
   ```bash
   python ai-data-generation.ipynb
   ```

3. **Generate Paper Figures:**
   ```bash
   # Core region map
   python paper-figures/core-region-map.ipynb
   
   # Distribution analysis
   python paper-figures/distribution.ipynb
   
   # Reference market comparison
   python paper-figures/reference-market.ipynb
   ```

## 📁 Repository Structure

```
ACER-CORE-Virtual-Hub-Simulation/
├── data/                          # Data directory
│   ├── raw/                       # Raw data from ENTSO-E
│   │   ├── generation/            # Generation data by country
│   │   ├── load/                  # Load data by country
│   │   └── spot_prices/           # Spot price data by country
│   ├── processed/                 # Processed and cleaned data
│   │   ├── generation_aggregated/ # Aggregated generation data
│   │   ├── generation_combined/   # Combined generation data
│   │   ├── load_aggregated/       # Aggregated load data
│   │   ├── load_combined/         # Combined load data
│   │   ├── spot_prices_cleaned/   # Cleaned spot prices
│   │   └── spot_prices_quarter_hours/ # Quarter-hourly prices
│   └── clean_data.ipynb           # Data cleaning notebook
├── paper-figures/                 # Jupyter notebooks for paper figures
│   ├── core-region-map.ipynb      # CORE region visualization
│   ├── distribution.ipynb         # Distribution analysis
│   └── reference-market.ipynb     # Reference market comparison
├── ai-data-generation.ipynb       # AI-powered data generation
├── suppress_warnings.py           # Warning suppression utilities
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## 📊 Data Sources

The analysis uses publicly available data from the European Network of Transmission System Operators for Electricity (ENTSO-E):

- **Generation Data:** Actual generation per production type (2019-2022)
- **Load Data:** Total load day-ahead and actual values (2019-2022)
- **Spot Prices:** Day-ahead electricity prices (2019-2022)

**Countries included:** Austria (AT), Belgium (BE), Czech Republic (CZ), Germany-Luxembourg (DE-LU), France (FR), Croatia (HR), Hungary (HU), Netherlands (NL), Poland (PL), Romania (RO), Slovenia (SI), Slovakia (SK)

## 🔬 Methodology

### Virtual Trading Hub (VTH) Construction
The CORE VTH is constructed as a volume-weighted average of spot prices across the CORE region, providing a more representative reference price for cross-border PPAs.

### Risk Metrics
- **Decoupling Loss:** Primary metric measuring financial exposure due to market price divergence
- **Volatility:** Standard deviation of decoupling losses
- **Skewness:** Asymmetry of loss distribution
- **Kurtosis:** Tail heaviness of loss distribution

### Simulation Methods
1. **Historical Analysis:** Direct analysis of observed market data
2. **t-Copula Simulation:** Multivariate Student-t copula with EVT tail modeling
3. **VAE Simulation:** Variational Autoencoder with Student-t prior for synthetic data generation

## 📈 Key Findings

1. **Correlation Analysis:** The CORE VTH exhibits the strongest correlation with both counterparties' markets
2. **Risk Reduction:** Significantly lower volatility in decoupling losses compared to DE-LU reference
3. **Hedging Efficiency:** Lower hedging costs and improved bankability for cross-border PPAs
4. **Extreme Events:** Higher skewness and kurtosis indicate more frequent extreme outcomes in VTH scenario

## 🛠️ Dependencies

Core dependencies include:
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computations
- `scipy` - Statistical functions
- `scikit-learn` - Machine learning utilities
- `tensorflow` - Deep learning framework
- `matplotlib` & `seaborn` - Visualization
- `cartopy` - Geographic plotting

See `requirements.txt` for complete list with versions.

## 📝 Usage Examples

### Basic Data Analysis
```python
import pandas as pd
import numpy as np

# Load processed data
df = pd.read_csv('data/processed/spot_prices_combined.csv')

# Calculate decoupling losses
def calculate_decoupling_loss(ppa_strike, market_price, volume=1.0):
    return volume * (ppa_strike - market_price)

# Example calculation
ppa_strike = 50.0  # EUR/MWh
market_prices = df['vth_price'].values
losses = calculate_decoupling_loss(ppa_strike, market_prices)
```

### Running Simulations
```python
# Load the AI data generation notebook
# This will run the complete simulation pipeline including:
# - t-Copula simulation with EVT
# - VAE-based synthetic data generation
# - Risk metrics computation
```

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this code or data in your research, please cite our paper:

```bibtex
@article{tichy2024simulation,
  title={Simulation of a virtual hub CORE and its impact on cross-border PPAs},
  author={Tichý, Martin and Miltner, Marek and Štogl, Ondřej and Bemš, Július},
  journal={IEEE Access},
  year={2024},
  publisher={IEEE},
  doi={10.5281/zenodo.16547945}
}
```
```

## 👥 Authors

- **Martin Tichý** - Faculty of Electrical Engineering, CTU in Prague
- **Marek Miltner** - Faculty of Electrical Engineering, CTU in Prague & Civil and Environmental Engineering, Stanford University
- **Ondřej Štogl** - Faculty of Electrical Engineering, CTU in Prague & Institute of Sustainability in Civil Engineering, RWTH Aachen University
- **Július Bemš** - Faculty of Electrical Engineering, CTU in Prague

## 🙏 Acknowledgments

This research was supported by the Czech Technical University under grant No. SGS25/142/OHK5/3T/13.

## 📞 Contact

- **Corresponding Author:** Martin Tichý
- **Email:** tichyma8@fel.cvut.cz
- **Institution:** Faculty of Electrical Engineering, Czech Technical University in Prague

## 🔗 Related Links

- [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/)

---

**Note:** This repository is part of an open science initiative to promote transparency and reproducibility in energy market research. All data, code, and analysis methods are publicly available for verification and extension.
