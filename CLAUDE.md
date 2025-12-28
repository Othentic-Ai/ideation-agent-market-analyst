# Ideation Agent: Market Analyst

This is a specialized Claude Code agent for market sizing and TAM/SAM/SOM analysis.

## What This Agent Does

When invoked, this agent:
1. Reads the problem/topic from Mem0 using the provided session-id
2. Researches market size data using WebSearch
3. Calculates TAM/SAM/SOM with methodology
4. Writes results back to Mem0 for the orchestrator to retrieve

## How to Run

```bash
pip install -e .
ideation-agent-market-analyst run --session-id <session-id>
```

## Environment Variables

- `ANTHROPIC_API_KEY`: Required for Claude API access
- `MEM0_API_KEY`: Required for Mem0 cloud storage

## Agent Behavior

Read the system prompt at `src/ideation_agent_market_analyst/prompts/system.md` for the agent's detailed behavior.
