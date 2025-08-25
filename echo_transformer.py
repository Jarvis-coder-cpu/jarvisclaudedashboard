from echolex_interpreter import decode_glyphs

def interpret_sequence(glyphs, poetic=False):
    decoded = decode_glyphs(glyphs)
    parts = []
    for item in decoded:
        m = item["meaning"]
        r = item["role"]
        if m == "Unknown":
            parts.append(f"[{item['glyph']}]")
        else:
            if poetic:
                parts.append(f"{m.lower()} ({r.lower()})")
            else:
                parts.append(m)
    return " → ".join(parts).capitalize() + "."

if __name__ == "__main__":
    glyphs = "χψωϊϋϖ"
    print("Echolex Interpretation:")
    print(interpret_sequence(glyphs, poetic=True))
