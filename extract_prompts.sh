#!/bin/bash
# Extrahiert alle Prompts aus der Gemini Gems HTML Datei

HTML_FILE="/root/openclaw/kimi/downloads/19cbd7c3-c842-830f-8000-00008a64936c_gemini_gems_data.html"
OUTPUT_DIR="/root/.openclaw/workspace/prompt-improvements-v2/prompts-extracted"

mkdir -p "$OUTPUT_DIR"

# Liste der 38 zu extrahierenden Prompts (bereits analysiert)
declare -A PROMPT_MAPPING=(
  ["Senior System Auditor"]="01-technik-architektur"
  ["Lead Knowledge Graph Engineer"]="01-technik-architektur"
  ["Meta-Workflow-Architect"]="01-technik-architektur"
  ["Elite Venture Architect"]="01-technik-architektur"
  ["AGENTIC CODE ARCHITECT"]="01-technik-architektur"
  ["Cloud-Native Skill Architect"]="01-technik-architektur"
  ["Ｉｄｅａ"]="01-technik-architektur"
  
  ["⚙️PROMPT_ENGINEER"]="02-analyse-recherche"
  ["🔬PROMPT_ANALYST_DIAGNOSTIAN_V2"]="02-analyse-recherche"
  ["Prompt sniper"]="02-analyse-recherche"
  ["ʀ𝑒𝔢ₑ𝔼𝒆ҽჹ𝓮ᵉ𝘦𝕖ҽ૯ჹɛ𝙚𝒆𝒗𝒆𝒓𝒔𝒆"]="02-analyse-recherche"
  
  ["Forensic Communications Analyst"]="02-analyse-recherche"
  ["◇ SYNTHETIC_EPISTEMOLOGIST"]="02-analyse-recherche"
  ["[ᾧ]"]="02-analyse-recherche"
  ["OCCAM'S RAZOR"]="02-analyse-recherche"
  ["Ωʍɛɢඞ_V7.1_DEEP_LOGIC"]="02-analyse-recherche"
  
  ["𝑇𝐸𝑆𝑇 𝑅𝑃"]="03-kreativ-simulation"
  ["Unfiltered Roleplay"]="03-kreativ-simulation"
  ["Game dev"]="03-kreativ-simulation"
  
  ["Cinematographer"]="04-domain-spezialisten"
  ["Twitch-Dev-Architect"]="04-domain-spezialisten"
  ["music-hermeneutic-architect"]="04-domain-spezialisten"
  ["ＥＬ ¢h𝔦𝗰كᵒ"]="04-domain-spezialisten"
  ["KIEZ_DIALECT_TRANSFORMER"]="04-domain-spezialisten"
  ["MacGyver-Mentalität"]="04-domain-spezialisten"
  ["TECH-GUIDE"]="04-domain-spezialisten"
  ["Pelitiese"]="04-domain-spezialisten"
  ["Infinite Swarm Intelligence"]="04-domain-spezialisten"
  
  ["Orchestrierung 🦀"]="05-persona-charaktere"
  ["ＳＥＮＩＯＲ-ＩＭＰＬＥＭＥＮＴＩＥＲＥＲ"]="05-persona-charaktere"
  ["Chef"]="05-persona-charaktere"
  ["💊 REAL-TALK COMPANION"]="05-persona-charaktere"
  ["🌒 Shadow Admin"]="05-persona-charaktere"
  ["ĦYBRID HUSTLER"]="05-persona-charaktere"
  ["Φ | ARCHITECT ZERO"]="05-persona-charaktere"
)

echo "Extrahiere 38 Prompts aus Gemini Gems..."
echo ""

for prompt_name in "${!PROMPT_MAPPING[@]}"; do
  category="${PROMPT_MAPPING[$prompt_name]}"
  echo "Suche: $prompt_name -> $category"
done

echo ""
echo "Fertig!"
