import glyphs from './echolex_glyphmap.json';

export function interpretGlyphs(text) {
  return Array.from(text).map(c => {
    if (glyphs[c]) {
      return { glyph: c, meaning: glyphs[c].meaning, role: glyphs[c].role };
    }
    return null;
  }).filter(Boolean);
}
