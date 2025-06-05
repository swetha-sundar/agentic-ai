# This script generates a UML diagram for the stress testing workflow using Graphviz.
import graphviz

# Define the UML diagram using Graphviz's DOT language
uml = graphviz.Digraph('StressTestWorkflow', format='png')
uml.attr(rankdir='LR', size='8,5')

# Agents
agents = {
    "Event Signal Agent": "Detects geopolitical/macro events from news & alerts",
    "Scenario Builder Agent": "Builds structured macro scenarios from events",
    "Market Data Fetch Agent": "Fetches market data like yield curves, spreads",
    "Risk Factor Shock Generator Agent": "Applies stress shocks to market data",
    "Portfolio Valuation Agent": "Revalues portfolio under stressed market conditions",
    "Liquidity & Spread Stress Agent": "Models bid-ask widening and liquidity stress",
    "Report Generator Agent": "Generates reports and dashboards",
    "Dashboard Agent": "Presents interactive visualization to human users"
}

# Add agents as nodes
for agent, desc in agents.items():
    uml.node(agent, f"<<b>{agent}</b>>\n{desc}", shape='component')

# Define edges (workflow sequence)
edges = [
    ("Event Signal Agent", "Scenario Builder Agent"),
    ("Scenario Builder Agent", "Market Data Fetch Agent"),
    ("Market Data Fetch Agent", "Risk Factor Shock Generator Agent"),
    ("Risk Factor Shock Generator Agent", "Portfolio Valuation Agent"),
    ("Portfolio Valuation Agent", "Liquidity & Spread Stress Agent"),
    ("Liquidity & Spread Stress Agent", "Report Generator Agent"),
    ("Report Generator Agent", "Dashboard Agent")
]

# Add edges to diagram
for src, dst in edges:
    uml.edge(src, dst)

# Render the diagram
uml.render(directory="./stress-testing/", cleanup=False)
