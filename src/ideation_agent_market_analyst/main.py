"""CLI entry point for the Market Analyst agent."""

import json
import click
from rich.console import Console
from .agent import run_agent
from .memory import SessionMemory

console = Console()

@click.group()
def cli():
    """Ideation Agent: Market Analyst - TAM/SAM/SOM Analysis."""
    pass

@cli.command()
@click.option("--session-id", required=True, help="Session ID for Mem0 context")
@click.option("--problem", default=None, help="Problem statement (optional)")
@click.option("--output-json", is_flag=True, help="Output results as JSON")
def run(session_id: str, problem: str | None, output_json: bool):
    """Run the market analyst agent for a given session."""
    memory = SessionMemory(session_id)

    if not problem:
        session = memory.get_session()
        if not session:
            console.print(f"[red]Error: No session found for {session_id}[/red]")
            raise SystemExit(1)
        problem = session.get("problem")

    console.print(f"[blue]Running market analyst agent for session: {session_id}[/blue]")
    result = run_agent(session_id, problem)
    memory.update_phase("market_analyst", "complete", result)

    if output_json:
        print(json.dumps(result, indent=2))
    else:
        console.print("[green]Market analyst agent completed successfully[/green]")

if __name__ == "__main__":
    cli()
