# SA Grid Resilience & Health Monitor

**Data Engineer Portfolio Project**  
Monitors South African electricity grid health, resilience indicators and weather conditions using public data.

---

## Project Highlights

- Live weather data for 4 major South African cities (Open-Meteo)
- Grid status integration (EskomSePush)
- Transparent Grid Stress / Resilience Score
- Interactive Streamlit dashboard with charts and tables
- Clean project structure and documented data sources

---

## Data Sources

| Source        | Purpose              | Notes                          |
|---------------|----------------------|--------------------------------|
| Open-Meteo    | Weather data         | Free, no API key needed        |
| EskomSePush   | Grid status          | Free API token required        |

---

## How to Run

```bash
git clone https://github.com/katlegomodiba45/sa-grid-health-monitor.git
cd sa-grid-health-monitor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/dashboard/app.py