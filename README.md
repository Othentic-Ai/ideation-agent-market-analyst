# Ideation Agent: Market Analyst

Market Size Researcher & TAM/SAM/SOM Financial Analyst for the Ideation Pipeline.

## Overview

This agent is part of the [Ideation multi-agent pipeline](https://github.com/Othentic-Ai/ideation-claude). It runs on [claude.ai/code](https://claude.ai/code) invoked by the Orchestrator via Slack hooks.

**Role:** Gathers market size data and calculates realistic TAM, SAM, and SOM estimates

**Output:** Market sizing data, TAM/SAM/SOM calculations, investment thesis

## Architecture

```
┌─────────────────────────────┐
│    Ideation Orchestrator    │
│  (manages flow via Slack)   │
└──────────────┬──────────────┘
               │ Slack hook
               ▼
┌────────────────────────┐
│  Market Analyst Agent  │  ◄── This repo
│     (Claude Code)      │
└──────────┬─────────────┘
           │ read/write
           ▼
┌─────────────────────────────┐
│            Mem0             │
│      (Shared Context)       │
└─────────────────────────────┘
```

## Repository Structure

```
ideation-agent-market-analyst/
├── CLAUDE.md        # Agent instructions (Claude Code reads this)
└── README.md        # This file
```

## How It Works

1. **Triggered**: Orchestrator invokes this agent via Slack hook
2. **Context**: Agent reads session context from Mem0
3. **Execution**: claude.ai/code reads `CLAUDE.md` and performs analysis
4. **Output**: Results written to Mem0 for the Orchestrator and next agent

## Part of Ideation Pipeline

This agent is one of 9 specialized agents:

| Phase | Agent | Repository |
|-------|-------|------------|
| 1 | Researcher | [ideation-agent-researcher](https://github.com/Othentic-Ai/ideation-agent-researcher) |
| 2 | Market Analyst | [ideation-agent-market-analyst](https://github.com/Othentic-Ai/ideation-agent-market-analyst) |
| 3 | Customer Discovery | [ideation-agent-customer-discovery](https://github.com/Othentic-Ai/ideation-agent-customer-discovery) |
| 4 | Scoring Evaluator | [ideation-agent-scoring-evaluator](https://github.com/Othentic-Ai/ideation-agent-scoring-evaluator) |
| 5 | Competitor Analyst | [ideation-agent-competitor-analyst](https://github.com/Othentic-Ai/ideation-agent-competitor-analyst) |
| 6 | Resource Scout | [ideation-agent-resource-scout](https://github.com/Othentic-Ai/ideation-agent-resource-scout) |
| 7 | Hypothesis Architect | [ideation-agent-hypothesis-architect](https://github.com/Othentic-Ai/ideation-agent-hypothesis-architect) |
| 8 | Pivot Advisor | [ideation-agent-pivot-advisor](https://github.com/Othentic-Ai/ideation-agent-pivot-advisor) |
| 9 | Report Generator | [ideation-agent-report-generator](https://github.com/Othentic-Ai/ideation-agent-report-generator) |

Orchestrated by: [ideation-claude](https://github.com/Othentic-Ai/ideation-claude)

## License

MIT
