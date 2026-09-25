# RTA Command Center

> **Status: building attempt.** The adherence-variance engine and threshold logic
> run against the sample data included in the repository. The business-impact
> figures in this file have no recorded method, baseline, or sample, so they are
> presented below as historical project context, not as measured results. Snapshot
> 2026-06-02.

A precursor to Helix Prime, from the May–June 2026 build period. The thinking
here was later absorbed into Helix Prime.

## What it does

Real-time adherence monitoring for contact-centre and BPO operations. It tracks
adherence variance per agent and per queue, applies configurable alert thresholds,
and exports compliance and adherence reports. The problem it targets is the lag
between an adherence breach and the corrective action.

- Adherence variance tracking per agent and queue
- Configurable alert thresholds per SLA tier
- Anomaly-detection layer for compounding escalations
- CRM data simulation for demo and staging
- Exportable compliance and adherence reports

## What is verified, and what is not

| Item | Status |
|---|---|
| Adherence variance and threshold logic | Runs locally against the sample data. |
| CRM data simulation | Runs for demo and staging use. |
| Report export | Runs locally. |
| Throughput, QA, DSAT, and reporting-time figures | Historical project context. No method, baseline, or sample is recorded. Not verifiable. |
| External audit | None. |

### Historical project context (unverified)

An earlier version of this file presented the figures below as measured business
impact. No baseline, sample, or method was ever recorded for any of them, so they
are reproduced here as the project's own historical claims and marked unverified.
They should not be read as results.

| Claim | Figure | Status |
|---|---|---|
| Team daily throughput | 14 tasks → 40 tasks (↑ 186%) | Unverified historical claim |
| Quality score | 100% maintained | Unverified historical claim |
| DSAT incidents | 0 | Unverified historical claim |
| Manual reporting time | ~8 hrs/week → 0 | Unverified historical claim |

The "Production-ready" label that previously appeared in this file has been
removed. It was not supported: no production gates are recorded for this
repository.

## Quick start

    git clone https://github.com/HatemIsmailShalaby1979/RTA_command_center.git
    cd RTA_command_center
    pip install -r requirements.txt
    streamlit run srcapp.py

## Architecture

- `srcapp.py`: Streamlit UI layer and session state management
- `calculations.py`: adherence variance engine and threshold logic
- `visualizations.py`: chart rendering and alert display
- `.devcontainer/`: containerised development environment

## Stack

Python · Streamlit · Pandas · SQL · Docker

## Honest boundary

It is a single application, not a deployed service. It does not integrate with a
live workforce-management or telephony system; the CRM layer is simulated. It has
no authentication, no role separation, and no tenant isolation. The adherence data
is sample data, not production data.

This is not a production deployment claim. There is no external audit, no
certified data isolation, and no signed security review. No revenue has been
realised.

## Related work

- [Helix Prime](https://github.com/HatemIsmailShalaby1979/Helix-Prime) — the operations core
- [Helix Education](https://github.com/HatemIsmailShalaby1979/Helix-Education) — event-sourced learning engine
- [Study Studio](https://github.com/HatemIsmailShalaby1979/Study-Studio) — local-first AI tutor
- [L&D Command Center](https://github.com/HatemIsmailShalaby1979/L-D-Command-Center) — desktop learning and career workstation
- [Blue Waves](https://github.com/HatemIsmailShalaby1979/Blue-Waves-) — content studio
- [LIVE Support Assistant](https://github.com/HatemIsmailShalaby1979/LIVE-Support-Assistant) — explainable support prototype
- [Full portfolio](https://github.com/HatemIsmailShalaby1979) — how this project fits the wider work

### The 2026 building attempts

- [WFM Forecasting Calculator](https://github.com/HatemIsmailShalaby1979/wfm-forecasting-calculator)
- [CX Sentiment Sentinel](https://github.com/HatemIsmailShalaby1979/cx-sentiment-sentinel)
- [Dynamic Ops Automation Engine](https://github.com/HatemIsmailShalaby1979/Dynamic-Ops-Automation-Engine)

## Author

**Hatem Ismail Shalaby** — Operations Architect · AI Systems Engineer · Founder

- GitHub: [HatemIsmailShalaby1979](https://github.com/HatemIsmailShalaby1979)
- LinkedIn: [hatem-shalaby-202902127](https://www.linkedin.com/in/hatem-shalaby-202902127/)
- Email: hatemshalaby2025@gmail.com
- Education: BSc Managerial Sciences (Computer Section), Sadat Academy for Management Sciences; Business Analytics Nanodegree, Udacity

Based in Al Obour City, Al-Qalyubia Governorate, Egypt.

## Licence

MIT
