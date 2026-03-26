import subprocess

def run_ollama_model():
    try:
        cmd = [
            "ollama", "run", "llama2", "-p", "What is the capital of France?"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return result.stdout
    except Exception as e:
        return f"[Ollama Error] {e}"
