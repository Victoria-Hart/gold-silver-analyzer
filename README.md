# Gold & Silver Analyzer
A Python-based analysis tool that retrieves price data for gold and silver via an API, analyzes trends over time, and presents the results via CLI and visualizations.

## Projektbeskrivning

Detta projekt är en Python-applikation för att analysera priser på ädelmetaller (guld och silver). Projektet är uppbyggt med tydlig struktur, datamodeller, validering, tester och automatiserad CI.

---

## Installation och körning

### Virtuell miljö (venv)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### Installera beroenden

```bash
pip install -r requirements.txt
```

### Hur projektet körs

Projektet är modulärt uppbyggt och flera delar kan köras eller testas var för sig.

Exempel:

- Tester kan köras med:
  ```bash
  pytest
  ```
- Enskilda moduler (t.ex. analys eller CLI) kan köras direkt under utveckling:
  ```bash
  python src/analysis/price_analyzer.py
  ```
Projektet saknar i nuläget en gemensam startpunkt (main.py) för att köra hela applikationen, vilket är planerat som ett nästa steg.

---

## Projektstruktur
```text
gold-silver-analyzer/
├── src/
│   ├── models/
│   ├── api/
│   ├── cli/
│   └── analysis/
├── tests/
├── .github/workflows/
├── requirements.txt
└── README.md
```
- **Python-moduler** (9+): cache_manager.py, metals_client.py, price_analyzer.py, portfolio_calculator.py, commands.py, output_formatter.py, ...
- **Klasser** (3+): Metal (models/metal.py), Price (models/price.py), Transaction (models/transaction.py), ...
- **Datavalidering**: Sker i datamodellerna i `models/` (price.py, metal.py, transaction.py) och verifieras genom enhetstester i `tests/` ...
- **Standardbibliotek** (5+): datetime (models/price.py), argparse (cli/commands.py), pathlib, json (api/cache_manager.py), typing (api/metals_client.py), ...
- **Externa bibliotek** (2+): pytest (tests/test_metal.py), requests (api/metals_client.py), ...
- **Enhetstester** (3+): i `tests/` (test_metal.py, test_price.py, test_transaction.py), ...
---

## Testinstruktioner
Tester körs med pytest.
```bash
pytest
```
Testerna validerar bland annat:
- korrekt datavalidering
- felhantering
- grundläggande funktionalitet i datamodellerna

---

## CI/CD-beskrivning
Projektet använder GitHub Actions för Continuous Integration (CI).

Vid varje push eller pull request:
- installeras beroenden
- alla tester körs automatiskt
CI används för att säkerställa kodkvalitet, medan eventuell CD (t.ex. deployment) ligger utanför projektets scope.

---

## Vem som gjort vad
- **Ali**: API (src/api/)
- **Victoria**: Models + CI (src/models/, tests/)
- **Albin**: Analysis (src/analysis/)
- **Anas**: Visualization (src/visualization/)
- **Allan**: CLI (src/cli/)
