import json
import argparse

# Load glyph map
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

def encode_sequence(concepts):
    concepts = [c.strip().lower() for c in concepts.split(",")]
    output = []

    for concept in concepts:
        match = None
        for glyph, info in GLYPHS.items():
            if concept in info["meaning"].lower():
                match = glyph
                break
        output.append(match or "?")
    return "".join(output)

def poetic_interpretation(decoded):
    parts = []
    for item in decoded:
        m = item["meaning"]
        r = item["role"]
        if m == "Unknown":
            parts.append(f"[{item['glyph']}]")
        else:
            parts.append(f"{m.lower()} ({r.lower()})")
    return " → ".join(parts).capitalize() + "."

def main():
    parser = argparse.ArgumentParser(description="Echolex CLI – Symbolic Glyph Encoder/Decoder")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--decode", help="Input glyph chain to decode (e.g., 'χψω')")
    group.add_argument("--encode", help="Input concept list (comma-separated) to encode (e.g., 'breath, dream')")
    parser.add_argument("--poetic", action="store_true", help="Return poetic interpretation (decode only)")

    args = parser.parse_args()

    if args.decode:
        result = decode_glyphs(args.decode)
        if args.poetic:
            print("Poetic Interpretation:")
            print(poetic_interpretation(result))
        else:
            print("Decoded Glyphs:")
            for r in result:
                print(f"{r['glyph']} — {r['name']}: {r['meaning']} ({r['role']})")

    elif args.encode:
        result = encode_sequence(args.encode)
        print(f"Echolex Glyph Chain: {result}")

if __name__ == "__main__":
    main()
