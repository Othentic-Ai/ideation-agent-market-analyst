"""Core agent execution logic for the Market Analyst agent."""

from pathlib import Path

def get_system_prompt() -> str:
    """Load the system prompt from the prompts directory."""
    prompt_path = Path(__file__).parent / "prompts" / "system.md"
    return prompt_path.read_text()

def run_agent(session_id: str, problem: str) -> dict:
    """Run the market analyst agent."""
    system_prompt = get_system_prompt()
    return {
        "phase": "market_analyst",
        "session_id": session_id,
        "problem": problem,
        "status": "pending_claude_execution",
        "system_prompt_loaded": bool(system_prompt),
        "instructions": "This agent should be run via Claude Code CLI"
    }
