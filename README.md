<div align="center">

# RTA Command Center


<!-- badges:start -->

![licence](https://img.shields.io/badge/licence-MIT-blue)
[![last commit](https://img.shields.io/github/last-commit/HatemIsmailShalaby1979/RTA_command_center)](https://github.com/HatemIsmailShalaby1979/RTA_command_center/commits/main)
![status](https://img.shields.io/badge/ci-no CI-lightgrey?label=no CI%20(2026-10-02))

*Measured 2026-10-06 — head `15f7742` (2026-10-02); Python.*

<!-- No static test or coverage count is shown here: a frozen
     number decays silently. Run the suite for a current figure;
     the CI badge above is the live status. -->
<!-- badges:end -->

**A precursor to Helix Prime — real-time adherence monitoring, later absorbed into its RTA engine.**

![Status](https://img.shields.io/badge/status-learning--exercise-yellow)
![Type](https://img.shields.io/badge/type-precursor-blue)
![Licence](https://img.shields.io/badge/licence-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12-3776ab)

</div>

## One-line identity

A May–June 2026 learning exercise: a real-time adherence monitor for contact-centre floors. Its adherence engine is the substantive part, and the problem it targets — the lag between a breach and the corrective action — later became Helix Prime's RTA engine.

> [!NOTE]
> **Operating principle.** The adherence engine is the real deliverable. `src/calculations.py` takes a schedule/adherence CSV and returns per-agent adherence percentages, summary metrics, and threshold alerts; it imports cleanly and exposes `RTACalculations`. The app's second import depends on launch directory, and `requirements.txt` is incomplete — both are fixable packaging gaps, not engine defects.

One of four small tools built during the May–June 2026 period, before Helix Prime existed. The problem it targets — real-time adherence monitoring, and the lag between a breach and the corrective action — was later absorbed into Helix Prime's RTA engine. This repository is the sketch, not the system.

## What is in the repository

Four substantial pieces, all written and readable:

| File | Lines | What it is |
|---|---:|---|
| `src/app.py` | 299 | Streamlit UI: configuration, CSV upload, alert thresholds, filters, key metrics, active alerts, per-agent detail, Excel export |
| `src/calculations.py` | 361 | **The real adherence engine.** `RTACalculations` with `time_to_minutes`, `calculate_adherence`, `calculate_summary_metrics`, `generate_alerts`, and `calculate_daily_trend`. Restored from the mis-uploaded `rta-command-centersrccalculations.py.txt` via `git mv` (see "How to make it run again"). |
| `visualizations.py` | 291 | Plotly charts — `RTAVisualizations` builds the adherence and trend panels. Sits at the repository root. |
| `_archive/calculations_root_stub.py` | 26 | **A stub, not the engine.** Its body is `# ... (keep your existing adherence math logic exactly as it is) ...` and it returns an undefined `df_result`. |

The engine is the substantive part: it takes a schedule/adherence CSV and returns per-agent adherence percentages, summary metrics, and threshold alerts. It imports cleanly and exposes `RTACalculations`.

## What does not work

- **A second import still depends on launch directory.** `src/app.py` line 13 is `from visualizations import RTAVisualizations`, but `visualizations.py` sits at the repository root while `app.py` is in `src/`. The import resolves only when the app is launched with the repository root on `sys.path` (for example `python -m streamlit run src/app.py` from the repository root, or with `PYTHONPATH=.`). Moving `visualizations.py` into `src/` removes the dependency; that was left as a separate decision.
- **`requirements.txt` is two lines** — a comment and `streamlit==1.35.0`. The code also imports `pandas`, `numpy`, `plotly`, and `openpyxl`. A reader who follows the documented install gets an `ImportError` until those are added.
- **No test suite is collected.** `test_calculations()` is a print-and-assert function living inside the engine module, so no runner picks it up.
- **Five mis-upload `.txt` artefacts are still tracked**, alongside the files they duplicate: `rta-command-centerREADME.md.txt`, `rta-command-centerrequirements.txt.txt`, `rta-command-centersrcapp.py.txt`, `rta-command-centersrcvisualizations.py.txt`, `rta-command-center.gitignore.txt`, plus `rta-command-centerexamplessample_data.csv.xlsx` (an xlsx mis-named `.txt`). The engine's `.txt` copy was consumed by the `git mv` above; these five remain and should be removed from tracking.

## How to make it run again

The engine restore is already done in this repository. To run the app:

```bash
git clone https://github.com/HatemIsmailShalaby1979/RTA_command_center.git
cd RTA_command_center
# engine already restored: rta-command-centersrccalculations.py.txt -> src/calculations.py
pip install streamlit pandas numpy plotly openpyxl
python -m streamlit run src/app.py   # launched from repo root so 'visualizations' resolves
```

If you prefer the app to launch from any directory, move `visualizations.py` into `src/`:

```bash
git mv visualizations.py src/visualizations.py
```

> [!WARNING]
> **What this repository is not.** Not a deployed service, and not a production deployment. It does not integrate with a live workforce-management or telephony system; the CRM layer is simulated. No authentication, no role separation, no tenant isolation. The adherence data is sample data. No external audit, no certified data isolation, no signed security review, no revenue.
>
> **Claims removed from earlier revisions of this file.** An earlier version presented the following as measured business impact. No baseline, sample, or method was recorded for any of them, so they are not repeated as results:
>
> | Claim | Figure |
> |---|---|
> | Team daily throughput | 14 tasks → 40 tasks (↑ 186%) |
> | Quality score | 100% maintained |
> | DSAT incidents | 0 |
> | Manual reporting time | ~8 hrs/week → 0 |
>
> A "Production-ready" label also appeared in an earlier revision. It was not supported — no production gates are recorded for this repository — and it is gone.

## Related work

- [Helix Prime](https://github.com/HatemIsmailShalaby1979/Helix-Prime) — the operations core; its RTA engine is where this thinking ended up
- [Helix Education](https://github.com/HatemIsmailShalaby1979/Helix-Education) — event-sourced learning engine
- [Study Studio](https://github.com/HatemIsmailShalaby1979/Study-Studio) — local-first AI tutor
- [L&D Command Center](https://github.com/HatemIsmailShalaby1979/L-D-Command-Center) — desktop learning and career workstation
- [Blue Waves](https://github.com/HatemIsmailShalaby1979/Blue-Waves-) — content studio
- [Full portfolio](https://github.com/HatemIsmailShalaby1979) — how this fits the wider work

### The other 2026 building attempts

- [WFM Forecasting Calculator](https://github.com/HatemIsmailShalaby1979/wfm-forecasting-calculator)
- [CX Sentiment Sentinel](https://github.com/HatemIsmailShalaby1979/cx-sentiment-sentinel) — the repository name overpromises; the code is a KPI-decay risk scorer
- [Dynamic Ops Automation Engine](https://github.com/HatemIsmailShalaby1979/Dynamic-Ops-Automation-Engine)

## Author

Built by Hatem Ismail Shalaby, Contact Centre Operations & AI Implementation Lead | WFM & CX Transformation. Background: https://github.com/HatemIsmailShalaby1979

## Licence

MIT
