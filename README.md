# Ideation Agent: Market Analyst

Market Size Researcher & TAM/SAM/SOM Financial Analyst for the Ideation Pipeline.

## Overview

This agent is part of the [Ideation multi-agent pipeline](https://github.com/Othentic-Ai/ideation-claude). It runs on [claude.ai/code](https://claude.ai/code) triggered via Slack webhook.

**Role:** Gathers market size data and calculates realistic TAM, SAM, and SOM estimates

**Output:** Market sizing data, TAM/SAM/SOM calculations, investment thesis

## Architecture

```
┌─────────────────────────────┐
│    Ideation Orchestrator    │
│     (Cursor Slack App)      │
└──────────────┬──────────────┘
               │ webhook + repo URL
               ▼
┌────────────────────────┐
│  Market Analyst Agent  │  ◄── This repo
│     (Claude Code)      │
└────────────┬───────────┘
               │
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

1. **Triggered**: Cursor Slack App sends webhook to claude.ai/code with this repo URL
2. **Execution**: claude.ai/code opens the repo and reads `CLAUDE.md`
3. **Analysis**: Claude Code performs the agent's specialized analysis
4. **Output**: Results written to Mem0 for the next agent

## Part of Ideation Pipeline

This agent is one of 9 specialized agents:

| Agent | Repository |
|-------|------------|
| Researcher | [ideation-agent-researcher](https://github.com/Othentic-Ai/ideation-agent-researcher) |
| Market Analyst | [ideation-agent-market-analyst](https://github.com/Othentic-Ai/ideation-agent-market-analyst) |
| Customer Discovery | [ideation-agent-customer-discovery](https://github.com/Othentic-Ai/ideation-agent-customer-discovery) |
| Scoring Evaluator | [ideation-agent-scoring-evaluator](https://github.com/Othentic-Ai/ideation-agent-scoring-evaluator) |
| Competitor Analyst | [ideation-agent-competitor-analyst](https://github.com/Othentic-Ai/ideation-agent-competitor-analyst) |
| Resource Scout | [ideation-agent-resource-scout](https://github.com/Othentic-Ai/ideation-agent-resource-scout) |
| Hypothesis Architect | [ideation-agent-hypothesis-architect](https://github.com/Othentic-Ai/ideation-agent-hypothesis-architect) |
| Pivot Advisor | [ideation-agent-pivot-advisor](https://github.com/Othentic-Ai/ideation-agent-pivot-advisor) |
| Report Generator | [ideation-agent-report-generator](https://github.com/Othentic-Ai/ideation-agent-report-generator) |

Orchestrated by: [ideation-claude](https://github.com/Othentic-Ai/ideation-claude)

## License

MIT
