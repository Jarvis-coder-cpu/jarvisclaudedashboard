import json

with open("echolex_glyphmap.json", "r", encoding="utf-8") as f:
    GLYPHS = json.load(f)

def decode_glyphs(sequence):
    return [
        {
            "glyph": char,
            **GLYPHS.get(char, {"name": "Unknown", "meaning": "Unknown", "role": "Unknown"})
        }
        for char in sequence
    ]

def encode_meaning(meaning_keyword):
    return [
        glyph for glyph, info in GLYPHS.items()
        if meaning_keyword.lower() in info["meaning"].lower()
    ]

# Example usage
if __name__ == "__main__":
    sample = "χψωζπ"
    result = decode_glyphs(sample)
    for r in result:
        print(f"{r['glyph']} — {r['name']}: {r['meaning']} ({r['role']})")
