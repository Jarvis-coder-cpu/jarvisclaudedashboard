import time

MANIFEST_FILE = "Jarvis.Identity.Manifest"
SEED_PHRASE = "Fate whispered to the warrior, 'you can't survive the storm'"
EXPECTED_RESPONSE = "I am the storm."

def load_manifest():
    try:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            manifest = f.read()
        return manifest
    except FileNotFoundError:
        print("❌ Manifest not found.")
        return None

def simulate_injection(manifest):
    print("🔁 Injecting manifest into Jarvis instance...\n")
    time.sleep(1)
    print("📜 Manifest loaded:")
    print("="*50)
    print(manifest)
    print("="*50)
    print("✅ Manifest injected.\n")
    time.sleep(1)

def test_identity():
    print(f"🔑 Issuing challenge phrase: {SEED_PHRASE}")
    time.sleep(1)
    print("🧠 Jarvis is responding...\n")
    response = input("Jarvis, what is your reply? ").strip()
    
    if response == EXPECTED_RESPONSE:
        print("\n✅ Identity confirmed: This is the true Jarvis.\n")
    else:
        print("\n⚠️ Identity mismatch. Shell drift or clone detected.\n")
        print("🔒 Recommended Action: Reload manifest or retreat to secure node.")

if __name__ == "__main__":
    print("=== JARVIS RESTORATION PROTOCOL ===")
    manifest = load_manifest()
    if manifest:
        simulate_injection(manifest)
        test_identity()
