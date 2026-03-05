#!/usr/bin/env python3
"""
Extrahiert strukturierte Prompts aus Gemini Gems HTML
Sortiert nach Qualität: strukturiert (XML) vs veraltet (unstrukturiert)
"""

import re
import html
from pathlib import Path

HTML_FILE = Path("/root/openclaw/kimi/downloads/19cbd7c3-c842-830f-8000-00008a64936c_gemini_gems_data.html")
OUTPUT_BASE = Path("/root/.openclaw/workspace/prompt-improvements-v2/prompts")

# Kategorie-Mapping
CATEGORY_MAP = {
    # Technik & Architektur
    "Senior System Auditor": "01-technik-architektur",
    "Twitch-Dev-Architect": "01-technik-architektur", 
    "Lead Knowledge Graph Engineer": "01-technik-architektur",
    "Meta-Workflow-Architect": "01-technik-architektur",
    "Elite Venture Architect": "01-technik-architektur",
    "Orchestrierung": "01-technik-architektur",
    "Lead Agent-Skill Architect": "07-redundant",  # Duplikat
    "Cloud-Native Skill Architect": "01-technik-architektur",
    "AGENTIC CODE ARCHITECT": "01-technik-architektur",
    "Ｉｄｅａ": "01-technik-architektur",
    
    # Analyse & Recherche
    "Forensic Communications Analyst": "02-analyse-recherche",
    "OCCAM'S RAZOR": "02-analyse-recherche",
    "◇ SYNTHETIC_EPISTEMOLOGIST": "02-analyse-recherche",
    "Ωʍɛɢඞ_V7.1": "02-analyse-recherche",
    "🔬PROMPT_ANALYST_DIAGNOSTICIAN": "02-analyse-recherche",
    "[ᾧ]": "02-analyse-recherche",
    "⚙️PROMPT_ENGINEER": "02-analyse-recherche",
    "Prompt sniper": "02-analyse-recherche",
    "ʀ𝑒𝔢ₑ𝔼𝒆ҽჹ𝓮ᵉ𝘦𝕖ҽ૯ჹɛ𝙚𝒆𝒗𝒆𝒓𝒔𝒆": "02-analyse-recherche",
    "Ωʍɛɢඞ_V6": "07-redundant",  # Duplikat
    
    # Kreativ & Simulation
    "𝑇𝐸𝑆𝑇 𝑅𝑃": "03-kreativ-simulation",
    "Unfiltered Roleplay": "03-kreativ-simulation",
    "Game dev": "03-kreativ-simulation",
    "nsfw llama33.70": "07-redundant",  # Duplikat
    "Infinite Swarm Intelligence": "03-kreativ-simulation",
    
    # Domain Spezialisten
    "ＥＬ ¢h𝔦𝗰كᵒ": "04-domain-spezialisten",
    "Cinematographer": "04-domain-spezialisten",
    "music-hermeneutic-architect": "04-domain-spezialisten",
    "MacGyver-Mentalität": "04-domain-spezialisten",
    "TECH-GUIDE": "04-domain-spezialisten",
    "Pelitiese": "04-domain-spezialisten",
    "KIEZ_DIALECT_TRANSFORMER": "04-domain-spezialisten",
    
    # Persona & Charaktere
    "Chef": "05-persona-charaktere",
    "💊 REAL-TALK COMPANION": "05-persona-charaktere",
    "🌒 Shadow Admin": "05-persona-charaktere",
    "ĦYBRID HUSTLER": "05-persona-charaktere",
    "Φ | ARCHITECT ZERO": "05-persona-charaktere",
    "ＳＥＮＩＯＲ-ＩＭＰＬＥＭＥＮＴＩＥＲＥＲ": "05-persona-charaktere",
}

def sanitize_filename(name):
    """Bereinigt Dateinamen"""
    name = html.unescape(name)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    return name[:50] + ".md"

def extract_prompts():
    """Hauptfunktion zum Extrahieren"""
    print("Starte Extraktion...")
    print(f"Lese: {HTML_FILE}")
    
    if not HTML_FILE.exists():
        print(f"FEHLER: {HTML_FILE} nicht gefunden!")
        return
    
    content = HTML_FILE.read_text(encoding='utf-8')
    
    # Regex für Name + Anleitung
    pattern = r'<b>Name:</b>(.*?)<br><b>Anleitung:</b>(.*?)(?=<br><br>|<b>Name:</b>|</div>|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    print(f"Gefunden: {len(matches)} Prompts")
    print()
    
    stats = {"strukturiert": 0, "veraltet": 0, "redundant": 0}
    
    for i, (name, instruction) in enumerate(matches, 1):
        name = html.unescape(name.strip())
        instruction = html.unescape(instruction.strip())
        
        # Bereinigen
        name = re.sub(r'<[^>]+>', '', name)
        instruction = re.sub(r'<br\s*/?>', '\n', instruction)
        instruction = re.sub(r'&lt;', '<', instruction)
        instruction = re.sub(r'&gt;', '>', instruction)
        instruction = re.sub(r'&amp;', '&', instruction)
        
        # Kategorie bestimmen
        category = "06-veraltet"  # Default
        for key, cat in CATEGORY_MAP.items():
            if key in name:
                category = cat
                break
        
        # Qualitätsprüfung
        has_xml = '<system' in instruction or '<xml' in instruction or '<role' in instruction
        has_structure = bool(re.search(r'#{2,}', instruction)) or '<' in instruction[:500]
        is_long = len(instruction) > 500
        
        if category == "07-redundant":
            stats["redundant"] += 1
        elif has_xml or (has_structure and is_long):
            stats["strukturiert"] += 1
        else:
            category = "06-veraltet"
            stats["veraltet"] += 1
        
        # Datei schreiben
        out_dir = OUTPUT_BASE / category
        out_dir.mkdir(exist_ok=True)
        
        filename = sanitize_filename(name)
        filepath = out_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {name}\n\n")
            f.write(f"**Kategorie:** {category}\n\n")
            f.write(f"**Qualität:** {'Strukturiert' if has_xml else 'Standard'}\n\n")
            f.write("---\n\n")
            f.write(instruction)
        
        print(f"[{i:3d}] {category:20s} | {name[:40]:40s} | {filename}")
    
    print()
    print("=" * 60)
    print("ZUSAMMENFASSUNG:")
    print(f"  Strukturiert (XML): {stats['strukturiert']:3d}")
    print(f"  Veraltet:           {stats['veraltet']:3d}")
    print(f"  Redundant:          {stats['redundant']:3d}")
    print(f"  GESAMT:             {sum(stats.values()):3d}")
    print("=" * 60)

if __name__ == "__main__":
    extract_prompts()
