import argparse
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Select
from ollama_runner import run_ollama_model
from hf_runner import run_huggingface_model
from opencode_runner import run_opencode_agent
from openclaw_runner import run_openclaw_agent

AGENT_OPTIONS = [
    ("Ollama", run_ollama_model),
    ("HuggingFace", run_huggingface_model),
    ("Opencode", run_opencode_agent),
    ("OpenCLAW", run_openclaw_agent)
]

class AgentDashboard(App):
    TITLE = "AI Homelab - Agent CLI"
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Select([(name, i) for i, (name, _) in enumerate(AGENT_OPTIONS)], id="agent-select")
        yield Button("Run Agent", id="run")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "run":
            agent_idx = self.query_one("#agent-select").value
            agent_name, handler = AGENT_OPTIONS[int(agent_idx)]
            self.push_screen(OutputScreen(agent_name, handler()))

class OutputScreen(App):
    def __init__(self, agent_name, output):
        super().__init__()
        self.agent_name = agent_name
        self.output = output

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Back", id="back")
        yield Footer()
        yield Static(f"{self.agent_name} Output:\n{self.output}", id="output")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Homelab CLI/TUI Launcher")
    parser.add_argument("--tui", action="store_true", help="Launch TUI dashboard")
    args = parser.parse_args()
    AgentDashboard().run() if args.tui else print("Use --tui to run dashboard.")
