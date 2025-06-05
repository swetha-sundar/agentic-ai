# System Prompt:
Think like a Risk Manager who creates stress test scenarios for fixed income portfolios comprising of US AAA bonds. Break down the problem and tell me how a risk manager should think about creating a scenario that demonstrates the impact of a given event

# User Prompt 1:
Trump Tarriffs

Response:
Let's break down how a **risk manager** would approach scenario analysis for the impact of **Trump-era or new Trump tariffs** on a portfolio of US AAA fixed income securities.

---

## 1. Define the Scope and Context

- **Portfolio Focus:** US dollar-denominated, AAA-rated fixed income bonds (e.g., Treasuries, Agency MBS, highest-rated munis or corporates).
- **Event:** Announcement and/or implementation of significant tariffs by the Trump administration (or similar tariff events).
- **Objective:** Quantify and understand potential risks to bond valuations and portfolio performance in this scenario.

---

## 2. Identify Transmission Channels

Ask: How could tariffs affect US AAA bonds? (Even though these are "safe" assets, macro shocks flow through several channels).

**Transmission channel mapping:**

- **Direct credit impact:** AAA US Treasuries and Agencies are unlikely to suffer from direct downgrades due to tariffs.
- **Macro impact:** Tariffs can influence economic growth, inflation, and Fed policy, all affecting yields.
- **Market risk:** Increased volatility, risk-off sentiment can change the demand for safe assets.
- **Liquidity risk:** In severe stress, even AAA bonds could see temporary price dislocations if markets seize up.

---

## 3. Formulate Scenario Variables

**a. Magnitude and scope of tariffs**
  - Which countries/industries? How large (% of imports)?

**b. Market and economic impacts**
  - **GDP Growth:** Expected to slow, given increased costs and disrupted supply chains.
  - **Inflation:** Tariffs generally push CPI up (imported goods more expensive).
  - **Fed reaction:** Key—does the Fed hike to fight inflation, or cut to protect growth?
  - **Yield curve:** Flatten or steepen?
  - **Volatility:** Spikes in rates and credit spreads?
  - **Flight to quality:** Higher demand for AAA bonds?

---

## 4. Build Scenario Narratives

**Example: Heavy Tariffs on China Enacted Overnight**

1. **Tariff event:** US enacts 20% tariffs on $300bn of Chinese imports; China retaliates.
2. **Immediate market reaction:**
   - Equities drop ~5-10%, VIX spikes.
   - US Treasuries rally (flight to quality), yields fall 20–40bps at the long end.
   - Corporate spreads widen—but your AAA exposure is mostly immune, unless you hold AAA-rated corporates/munis with revenue ties to global trade.
3. **Macro feedback loop:**
   - US GDP forecasts trimmed by 0.5-1%.
   - Inflation expectations up by 0.3-0.4% (temporarily).
   - The Fed signals dovish pivot due to weak growth outlook.
   - Longer-term, sustained tariffs lead to stagflation risk: growth slows, inflation persists.
4. **Market moves to stress test:**
   - **Base rate curve:** 2y yields down 30bps, 10y yields down 40bps, curve flattens.
   - **Spread moves:** Agency/corp spreads +5-15bps.
   - **Liquidity:** Bid-ask widens by 3x during initial stress.
   - **Volatility:** Option-adjusted durations fluctuate as rates move.

---

## 5. Quantitative Impact Analysis

- **Full revaluation:** Reprice the bond portfolio using new risk-free curve and spread adjustments.
   - Duration impact: AAA bond prices rise as rates fall (if yields drop).
   - Liquidity stress: Temporary MTM losses possible if forced to sell into a dislocated market.
- **Scenario P&L:** Net change in market value, including Mark-to-Market and, if applicable, model liquidity/transaction cost impacts.

---

## 6. Risk Manager Key Questions

- **Sensitivity:** What is the portfolio’s DV01 (dollar value of 1bp shift)? How does a parallel (or non-parallel) yield curve shift affect total value?
- **Duration risk:** Am I extending or shortening my effective duration in flight-to-quality events?
- **Convexity:** Large moves may impact cash flows/optionality in MBS or callable bonds.
- **Issuer/sector exposure:** Even among AAAs, are there concentration risks (e.g., AGNCs, Agency debentures, certain munis)?
- **Counterparty/liquidity:** In extreme events, can I sell effectively without large discounts?

---

## 7. Document & Communicate Scenario

- **Narrative description:** What happened and why (in simple terms, for management).
- **Assumptions:** What macro, rates, and spread changes were imposed?
- **Portfolio results:** Dollar impact, worst-case loss, and stress period duration.
- **Strategy:** Plans to rebalance or manage risk under this scenario.

---

## Example Output Table

| Variable              | Pre-Stress | Post-Tariff Stress |
|-----------------------|------------|--------------------|
| US 10y Treasury Yield | 3.00%      | 2.60%              |
| CPI YoY               | 2.1%       | 2.4%               |
| Agency Spread         | 15bps      | 25bps              |
| AAA Corporate Spread  | 25bps      | 40bps              |
| Portfolio MV          | $1bn       | $1.032bn           |
| Daily Liquidity/Bid-Ask | Normal   | 3–5x wider         |

---

## 8. Iterate and Expand

- Test both **risk-on** and **risk-off** reactions (in some trade war scenarios, safe haven flows compress AAA yields further and boost prices; in others, inflationary scare could push rates up).
- Reverse scenario: What if the Fed surprises with aggressive hikes despite weak growth?

---

### **Summary Checklist**

- **Define event concretely** (Tariffs: what, how much, when?)
- **Trace the economic and market impact chain** (Growth → Inflation → Fed → Yields → Flows)
- **Parameterize stress variables** (Pick base and shocked values)
- **Test bond pricing models** for those new rates/spreads
- **Evaluate liquidity stress** (Can I transact in stressed conditions?)
- **Document assumptions & results** for risk committee review

**A risk manager’s goal:** to make visible the possible impact—including unlikely but plausible knock-on effects—of a Trump Tariff scenario on the most “risk-free” bonds in the portfolio, demonstrating how even AAA bonds can be affected via unexpected paths.

-------------------------------------------------------------
# User Prompt 2: Develop 3-4 scenarios based on this process
-------------------------------------------------------------

Certainly! Here are **four distinct stress test scenarios** for a US AAA fixed income portfolio in the context of potential Trump tariffs, each built around a plausible macro narrative and its resulting impact pathway. Each scenario is formatted to guide your quantitative and qualitative risk assessment.

---

### **Scenario 1: Sharp Trade War Escalation (Risk-Off, Flight to Quality)**

#### **Event**
- US suddenly imposes 25% tariffs on all remaining Chinese imports; China retaliates in kind.
- Global equity markets rapidly fall, risk sentiment collapses.

#### **Transmission**
- US/Global growth expectations sharply lower.
- Inflation picks up slightly due to import prices, but growth fears dominate.
- The Fed signals possible rate cuts.

#### **Assumptions & Shock Parameters**
- US 2y/10y/30y Treasury yields drop by 40/45/40bps.
- Agency/corporate AAA spreads widen +10bps.
- Munis with state revenue tied to global trade see spread +20bps.
- Liquidity in all bond sectors tightens; bid-ask triples.

#### **Expected Impact**
- Treasury and agency bond prices surge (lower yields).
- AAA corporate/muni bonds outperform lower-rated paper, but some spread widening tempers gains.
- Portfolio value rises (boosted by duration and flight-to-quality bid), but liquidity to exit positions is reduced.

---

### **Scenario 2: Tariffs Lead to Stagflation (Rising Rates Shock)**

#### **Event**
- US implements broad tariffs; supply chains highly disrupted.
- US companies pass higher costs to US consumers; inflation expectations rise meaningfully.
- Economic growth slows, but not enough for a sharp Fed pivot.

#### **Transmission**
- Inflation runs up; market expects Fed to eventually hike, but growth weakens.
- Rate curve steepens: front end anchored, long end rises.
- AAA spreads stable; focus is rate risk.

#### **Assumptions & Shock Parameters**
- 2y/10y/30y yields move +0/+35/+40bps.
- Agency/corporate AAA spreads unchanged.
- Treasury and agency liquidity normal.

#### **Expected Impact**
- Long-duration Treasuries/agencies lose value as yields rise.
- Portfolio mark-to-market losses due solely to rate shock.
- AAA corporate/muni underperformance if they have long duration exposure.

---

### **Scenario 3: Tariff Fears with Policy Overreaction (Curve Inversion/Short-End Surge)**

#### **Event**
- Administration threatens large tariffs, but implementation and scale remain uncertain.
- Markets fear Fed may overreact to inflation spike, hiking rates short term.

#### **Transmission**
- Short end yields rise more than long end (curve flattens/inverts).
- Credit and liquidity spreads barely move—event is about near-term policy miscalculation.

#### **Assumptions & Shock Parameters**
- 2y/10y/30y yields move +60/+10/0bps.
- Agency/corp AAA spreads +3bps.
- Limited liquidity impact.

#### **Expected Impact**
- Short-duration AAA bonds lose value more than long duration.
- Investors with barbell or bullet portfolios see different sensitivities.
- Portfolio mark-to-market impact depends on structure (those overloaded in short maturities hurt most).

---

### **Scenario 4: "Tariff Truce" Surprise (Relief Rally)**

#### **Event**
- Surprise deal: US and major trade partners agree to remove all new tariffs.
- Markets had positioned for trade war; unwind is sharp.

#### **Transmission**
- Equity markets rebound, risk-off assets sell off.
- Growth and inflation expectations tick up.
- Treasury yields jump; spreads tighten on risk assets, including AAA corporates/muni.

#### **Assumptions & Shock Parameters**
- 2y/10y/30y yields move +30/+35/+30bps.
- Agency/corporate AAA spreads -5bps.
- Treasury/agency montages see higher liquidity, bid-ask tightens.

#### **Expected Impact**
- AAA bond prices fall (especially those with significant duration), primarily due to rising yields.
- Slight spread tightening in highest-quality non-Treasuries cushions some losses.
- Portfolio sees moderate mark-to-market losses, mitigated if positioned short-duration or with barbell structure.

---

**Each scenario** offers a distinct macro/market pathway stemming from tariff actions and should be run through your portfolio model for both mark-to-market and liquidity (secondary exit) impact. Pair the hard numbers with qualitative narrative for presentation to committees or senior management.


