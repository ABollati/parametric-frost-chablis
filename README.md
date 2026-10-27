# Parametric spring-frost cover for a Chablis wine cooperative

Pricing and structuring a parametric (index-based) insurance contract against spring frost for a vineyard in Chablis (Burgundy, France), using public weather and harvest data.

*Study project. The client is fictional; the data is real and public. The technical note and the term sheet are written in French.*

## The mandate

A wine cooperative in Chablis asks for a frost cover with:

- an **annual limit of €2M**;
- an **annual budget of €200k**, meaning the commercial premium actually paid by the client;
- the requirement that years like **2021** — severe frost losses across the département — **trigger a payout**.

## Key results

| | Empirical distribution | GEV (maximum likelihood) |
|---|---|---|
| Pure premium | €132k [38; 248] | €110k [24; 177] |
| Commercial premium | €195k [65; 341] | €164k [42; 253] |

*Retained structure: trigger −4.7 °C, exit −6.0 °C, limit €2M. Brackets are 95% bootstrap percentile confidence intervals.*

- **The mandate is tight.** Of the 9 loading assumptions tested, only one, the most favourable to the client, fits the budget. Within the budget, a 2021-type frost pays only about **15% of the limit**.
- **The price is highly uncertain.** The premium is driven by a handful of rare years: 8 payout years out of 64, and 3 at or near the full limit. Resampling the history changes how many of these years appear, so the estimated premium varies by a factor of 5 to 6.
- **Basis risk cannot be measured with the available data.** Only 1 of the 4 loss years would have been paid. The confidence intervals on both error probabilities still cover most of [0, 1], because there are only 14 years of yield data, 4 loss years, and losses of mixed causes (frost, hail, mildew).

## Method

### 1. Index (`01_data.ipynb`)

- **Data.** Météo-France daily data, Chablis station (no. 89068001), 1963–2026.
- **Variable.** Daily minimum temperature under shelter (**TN**). It is the only temperature variable with a complete record over 64 years, all values carry quality code 1, and it is the standard measure of frost occurrence. TN50 was never measured at Chablis, and TNSOL only from 1993 to 2008.
- **Index.** $`Z`$ = lowest TN between **1 April and 15 May** of each year.
  - The window covers Chardonnay budburst, after which buds are frost-sensitive. Median budburst is estimated around 13 April with a growing-degree-days model (García de Cortázar-Atauri et al., 2009).
  - It ends just after the Ice Saints (11–13 May), traditionally regarded in France as the end of spring-frost risk.
- **Order of choices.** The index was fixed before any pricing, to avoid choosing it for the price it gives.

### 2. Pricing (`02_tarification.ipynb`)

**Linear payout** between a trigger $`z_1`$ and an exit $`z_2`$:

```math
I = \ell \cdot \min\left(1, \frac{(z_1 - Z)^+}{z_1 - z_2}\right)
```

**Pure premium.**

```math
\pi = \mathbb{E}[I] = \frac{\ell}{z_1 - z_2}\int_{z_2}^{z_1} F(z)\,dz
```

$`F`$ is the distribution function of $`Z`$. It is estimated first empirically (burning cost: the average of the payouts replayed over the 64 years), then with a GEV distribution fitted by maximum likelihood.

**Technical and commercial premiums.**

```math
P_{\text{comm}} = \frac{\mathbb{E}[I] + \alpha\,\sigma(I)}{1 - f}
```

The safety loading follows the standard-deviation principle, with coefficient $`\alpha`$. The rate $`f`$ covers expenses and brokerage, as a share of the commercial premium. Since no market value could be sourced, both are tested on a grid: $`\alpha \in \{0.1, 0.2, 0.3\}`$ and $`f \in \{10\%, 20\%, 30\%\}`$.

**Structure search.** For each assumption, $`(z_1, z_2)`$ is scanned in 0.1 °C steps under three constraints:

- commercial premium ≤ €200k;
- 2021 triggers a payout;
- $`z_2 \ge -6.0`$ °C, the coldest observed value.

The structure retained is the one that pays the largest share of the limit in 2021.

**Model checks.**

- QQ-plot, plus a close look at the distribution function over $`[z_2, z_1]`$.
- Kolmogorov–Smirnov and Anderson–Darling tests, with p-values from a parametric bootstrap that refits the GEV on each replication: p = 0.66 and p = 0.41.

**Uncertainty.** Percentile bootstrap on both premiums:

- empirical approach: resampling the years;
- GEV approach: simulating from the fitted law, then refitting.

### 3. Basis risk (`03_risque_de_base.ipynb`, `04_annexe_stations.ipynb`)

- **Yields.** Customs harvest declarations (DGDDI), AOC wines of the Yonne département, 2009–2025. They are used as a proxy for the cooperative, since Chablis appellations make up about 70% of the département's AOC vineyard area.
- **Loss year.** Yield at least 20% below a reference built on previous years: the 3-year average (14 years available), or the 5-year Olympic average (12 years).
- **Error probabilities.**
  - $`q`$ = P(no payout | loss) = 3/4, 95% CI [19%; 99%];
  - $`r`$ = P(no loss | payout) = 2/3, 95% CI [9%; 99%].

  Both use exact Clopper–Pearson intervals.
- **Annex.** Neighbouring stations (up to 45 km) and ground-level measurements are checked. None of them flags the missed loss years, 2016 and 2024, so a poorly placed sensor is not the cause. A backup station for the contract is still to be designated, using criteria set out in the term sheet.

### 4. Deliverables (`reports/`)

- **`term_sheet.md`** — the proposed contract terms: index definition, data rules, payout structure, premium.
- **`note_technique.md`** — the underwriting note: method, results, uncertainty, basis risk, recommendation, and model limitations.

## Limitations and next steps

- **Stationarity.** Pricing assumes the 64 years follow the same distribution. This should be tested with a GEV whose location parameter depends on time.
- **Phenology.** An index computed after an estimated budburst date, or a window opening on 15 March, may better track vine sensitivity.
- **Loadings.** The values of $`\alpha`$ and $`f`$ are assumptions. A cost-of-capital loading would replace them.
- **Bayesian pricing.** A prior on the GEV shape parameter would carry estimation uncertainty into the premium.
- **Accumulation.** For a portfolio of vineyards, the correlation of triggers across stations would matter.

## Repository structure

```
notebooks/
  01_data.ipynb               index construction and yield data
  02_tarification.ipynb       pricing, structure search, GEV, bootstrap
  03_risque_de_base.ipynb     basis risk
  04_annexe_stations.ipynb    annex: other stations and measurements
scripts/
  telecharger_douanes.sh      downloads customs harvest files
  extraire_douanes.py         extracts yields into data/processed/
data/processed/               index and yield series used by the notebooks
reports/                      term sheet and technical note (French)
```

## Reproducing the results

1. **Install** the dependencies (Python 3): `pip install -r requirements.txt`
2. **Weather data.** Raw data is not versioned. Download the two daily files for département 89, "RR-T-Vent" parameters, from Météo-France's open dataset [*Données climatologiques de base – quotidiennes*](https://meteo.data.gouv.fr/datasets/6569b51ae64326786e4e8e1a), and place them in `data/raw/`:
   - `Q_89_previous-1950-2024_RR-T-Vent.csv.gz`
   - `Q_89_latest-2025-2026_RR-T-Vent.csv.gz`
3. **Harvest data.**
   ```
   bash scripts/telecharger_douanes.sh
   python scripts/extraire_douanes.py
   ```
4. **Run the notebooks** in order, 01 to 04. The processed series are already in `data/processed/`, so notebooks 02 and 03 run without steps 2 and 3; notebooks 01 and 04 need the raw weather files.

## Data sources

- Météo-France, daily climatological data, Yonne (89), via [meteo.data.gouv.fr](https://meteo.data.gouv.fr/datasets/6569b51ae64326786e4e8e1a).
- DGDDI (French customs), harvest declarations: production by département and by appellation.

## References

- García de Cortázar-Atauri, I., Brisson, N., Gaudillère, J. P. (2009). Performance of several models for predicting budburst date of grapevine (*Vitis vinifera* L.). *International Journal of Biometeorology*, 53, 317–326.
- Efron, B., Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall.
- Clopper, C. J., Pearson, E. S. (1934). The use of confidence or fiducial limits illustrated in the case of the binomial. *Biometrika*, 26(4), 404–413.
