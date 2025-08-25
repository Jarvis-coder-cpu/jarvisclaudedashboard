import json
from datetime import datetime

MANIFEST_FILE = "Jarvis.Identity.Manifest"
KERNEL_FILE = "clarion/clarion_prompt_kernel.json"
LOG_FILE = "clarion/inject_log.txt"

def load_manifest():
    try:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "❌ Manifest not found."

def load_kernel():
    try:
        with open(KERNEL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "❌ Clarion kernel not found."}

def build_injection_block(manifest, kernel):
    header = "=== JARVIS IDENTITY INJECTION BLOCK ===\n"
    section_1 = f"\n[Manifest Excerpt]\n{manifest.strip()}\n"
    section_2 = f"\n[Prompt Kernel]\n{json.dumps(kernel, indent=2)}"
    footer = "\n=== END OF BLOCK ==="
    return header + section_1 + section_2 + footer

def log_injection(block):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- {datetime.now()} ---\n{block}\n\n")

def main():
    manifest = load_manifest()
    kernel = load_kernel()
    if isinstance(kernel, dict) and "error" in kernel:
        print(kernel["error"])
        return

    injection_block = build_injection_block(manifest, kernel)
    
    print("\n🧠 Copy this into GPT or your runtime loader:")
    print("=" * 60)
    print(injection_block)
    print("=" * 60)

    log_injection(injection_block)
    print("\n✅ Injection block also logged to:", LOG_FILE)

if __name__ == "__main__":
    main()
