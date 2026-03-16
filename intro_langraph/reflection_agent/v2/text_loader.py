from pathlib import Path

PROMPTS_DIR = Path(__file__).parent / "prompts"

def load_prompt(node_name: str, prompt_type: str):
    prompt_file_name = f'{PROMPTS_DIR}/{node_name}_{prompt_type}.md'
    return Path(prompt_file_name).read_text(encoding="utf-8")