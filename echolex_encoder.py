import json

with open("echolex_glyphmap.json", "r", encoding="utf-8") as f:
    GLYPHS = json.load(f)

def encode_sequence(concepts):
    concepts = [c.strip().lower() for c in concepts.split(",")]
    output = []

    for concept in concepts:
        match = None
        for glyph, info in GLYPHS.items():
            if concept in info["meaning"].lower():
                match = glyph
                break
        if match:
            output.append(match)
        else:
            output.append("?")  # Unknown

    return "".join(output)

if __name__ == "__main__":
    user_input = "vision, dream, ending"
    encoded = encode_sequence(user_input)
    print(f"Input: {user_input}")
    print(f"Echolex glyph chain: {encoded}")
