"""Mem0 integration for session-based context sharing across agents."""

import json
import os
from datetime import datetime
from typing import Optional

from mem0 import MemoryClient


class SessionMemory:
    """Memory service for session-based context sharing.

    Each session represents a single evaluation run, with all agents
    reading from and writing to the same session context.
    """

    def __init__(self, session_id: str):
        """Initialize session memory.

        Args:
            session_id: Unique identifier for this evaluation session
        """
        self.session_id = session_id
        self.user_id = f"ideation_session_{session_id}"
        self._client = None

    @property
    def client(self) -> MemoryClient:
        """Lazy initialization of Mem0 client."""
        if self._client is None:
            api_key = os.getenv("MEM0_API_KEY")
            if not api_key:
                raise ValueError("MEM0_API_KEY environment variable is required")
            self._client = MemoryClient(api_key=api_key)
        return self._client

    def get_session(self) -> Optional[dict]:
        """Get the current session context.

        Returns:
            Session data dict or None if not found
        """
        try:
            results = self.client.search(
                f"session {self.session_id}",
                user_id=self.user_id,
                limit=1,
                filters={"metadata": {"type": "session"}}
            )
            if results.get("results"):
                memory = results["results"][0].get("memory", "")
                try:
                    return json.loads(memory)
                except json.JSONDecodeError:
                    return {"raw": memory}
            return None
        except Exception as e:
            print(f"[mem0] Warning: Failed to get session: {e}")
            return None

    def create_session(self, problem: str, threshold: float = 7.0) -> str:
        """Create a new session.

        Args:
            problem: The problem statement to evaluate
            threshold: Elimination threshold

        Returns:
            Session ID
        """
        session_data = {
            "session_id": self.session_id,
            "problem": problem,
            "threshold": threshold,
            "created_at": datetime.now().isoformat(),
            "phases": {
                "researcher": {"status": "pending"},
                "market_analyst": {"status": "pending"},
                "customer_discovery": {"status": "pending"},
                "scoring_evaluator_problem": {"status": "pending"},
                "competitor_analyst": {"status": "pending"},
                "resource_scout": {"status": "pending"},
                "hypothesis_architect": {"status": "pending"},
                "scoring_evaluator_solution": {"status": "pending"},
                "pivot_advisor": {"status": "pending"},
                "report_generator": {"status": "pending"},
            },
            "scores": {
                "problem": None,
                "solution": None,
                "combined": None
            },
            "decision": None
        }

        memory_text = json.dumps(session_data, indent=2)

        try:
            result = self.client.add(
                memory_text,
                user_id=self.user_id,
                metadata={
                    "type": "session",
                    "session_id": self.session_id,
                    "timestamp": datetime.now().isoformat()
                }
            )
            return self.session_id
        except Exception as e:
            print(f"[mem0] Warning: Failed to create session: {e}")
            return self.session_id

    def update_phase(self, phase: str, status: str, output: dict) -> bool:
        """Update a phase's status and output.

        Args:
            phase: Phase name (e.g., "researcher")
            status: New status (e.g., "complete", "failed")
            output: Phase output data

        Returns:
            True if successful
        """
        phase_data = {
            "session_id": self.session_id,
            "phase": phase,
            "status": status,
            "output": output,
            "updated_at": datetime.now().isoformat()
        }

        memory_text = f"""
Phase Update: {phase}
Session: {self.session_id}
Status: {status}
Updated: {datetime.now().isoformat()}

Output:
{json.dumps(output, indent=2)[:3000]}
"""

        try:
            self.client.add(
                memory_text,
                user_id=self.user_id,
                metadata={
                    "type": "phase_output",
                    "session_id": self.session_id,
                    "phase": phase,
                    "status": status,
                    "timestamp": datetime.now().isoformat()
                }
            )
            return True
        except Exception as e:
            print(f"[mem0] Warning: Failed to update phase: {e}")
            return False

    def get_phase_output(self, phase: str) -> Optional[dict]:
        """Get a specific phase's output.

        Args:
            phase: Phase name

        Returns:
            Phase output dict or None
        """
        try:
            results = self.client.search(
                f"phase {phase} session {self.session_id}",
                user_id=self.user_id,
                limit=1,
                filters={
                    "metadata": {
                        "type": "phase_output",
                        "session_id": self.session_id,
                        "phase": phase
                    }
                }
            )
            if results.get("results"):
                return results["results"][0]
            return None
        except Exception as e:
            print(f"[mem0] Warning: Failed to get phase output: {e}")
            return None

    def get_previous_phases(self) -> dict:
        """Get all completed phase outputs for context.

        Returns:
            Dict of phase name -> output
        """
        try:
            results = self.client.search(
                f"session {self.session_id}",
                user_id=self.user_id,
                limit=20,
                filters={
                    "metadata": {
                        "type": "phase_output",
                        "session_id": self.session_id,
                        "status": "complete"
                    }
                }
            )

            phases = {}
            for result in results.get("results", []):
                meta = result.get("metadata", {})
                phase = meta.get("phase")
                if phase:
                    phases[phase] = result
            return phases
        except Exception as e:
            print(f"[mem0] Warning: Failed to get previous phases: {e}")
            return {}
