# Ideation Agent: Market Analyst

Market Size Researcher & TAM/SAM/SOM Financial Analyst for the Ideation Pipeline.

## Overview

This agent is part of the [Ideation multi-agent pipeline](https://github.com/Othentic-Ai/ideation-claude). It is invoked by the orchestrator via webhook and communicates through Mem0.

**Role:** Gathers market size data and calculates realistic TAM, SAM, and SOM estimates

**Tools:** WebSearch

**Output:** Market sizing data, TAM/SAM/SOM calculations, investment thesis

## Architecture

```
┌─────────────────────────┐
│  Ideation Orchestrator  │
│  (Cursor Slack App)     │
└───────────┬─────────────┘
            │ repository_dispatch
            ▼
┌─────────────────────────┐
│  Market Analyst Agent     │◄──── This repo
│  (GitHub Actions)       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│        Mem0             │
│  (Shared Context)       │
└─────────────────────────┘
```

## Installation

```bash
pip install -e .
```

## Usage

### Via CLI

```bash
ideation-agent-market-analyst run --session-id <session-id>
```

### Via GitHub Actions (Webhook)

This agent is triggered via `repository_dispatch`:

```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Othentic-Ai/ideation-agent-market-analyst/dispatches \
  -d '{"event_type": "run", "client_payload": {"session_id": "abc123", "problem": "Your problem"}}'
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude API access |
| `MEM0_API_KEY` | Yes | Mem0 cloud storage |

## How It Works

1. **Triggered**: Orchestrator sends `repository_dispatch` webhook
2. **Context**: Agent reads session context from Mem0
3. **Execution**: Claude Code runs the agent with the system prompt
4. **Output**: Results written back to Mem0 for next agent

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
