#!/usr/bin/env python3
"""Generate comprehensive universal knowledge base waveform symbols."""

import json
from typing import List
from waveform_static_db import WaveformSymbol, create_waveform_symbol


def generate_biology() -> List[WaveformSymbol]:
    """Generate biology and life science symbols."""
    concepts = [
        ("CELL", "Cell unit"),
        ("NUCLEUS", "Cell nucleus"),
        ("MITOCHONDRIA", "Mitochondria organelle"),
        ("CHLOROPLAST", "Chloroplast organelle"),
        ("RIBOSOME", "Ribosome"),
        ("ENDOPLASMIC_RETICULUM", "Endoplasmic reticulum"),
        ("GOLGI_APPARATUS", "Golgi apparatus"),
        ("LYSOSOME", "Lysosome"),
        ("MEMBRANE", "Cell membrane"),
        ("DNA", "Deoxyribonucleic acid"),
        ("RNA", "Ribonucleic acid"),
        ("PROTEIN", "Protein molecule"),
        ("ENZYME", "Enzyme catalyst"),
        ("METABOLISM", "Metabolic processes"),
        ("PHOTOSYNTHESIS", "Photosynthesis process"),
        ("RESPIRATION", "Cellular respiration"),
        ("MITOSIS", "Mitosis process"),
        ("MEIOSIS", "Meiosis process"),
        ("GENE", "Genetic unit"),
        ("CHROMOSOME", "Chromosome structure"),
        ("EVOLUTION", "Evolutionary process"),
        ("NATURAL_SELECTION", "Natural selection"),
        ("MUTATION", "Genetic mutation"),
        ("ADAPTATION", "Adaptation process"),
        ("ECOSYSTEM", "Ecosystem concept"),
        ("BIOME", "Biome classification"),
        ("ORGANISM", "Living organism"),
        ("SPECIES", "Species classification"),
        ("GENUS", "Genus classification"),
        ("TAXONOMY", "Taxonomic classification"),
    ]
    return [create_waveform_symbol(name, "biology", description=desc) for name, desc in concepts]


def generate_medicine() -> List[WaveformSymbol]:
    """Generate medical and anatomy symbols."""
    concepts = [
        ("ANATOMY", "Anatomical study"),
        ("PHYSIOLOGY", "Physiological study"),
        ("PATHOLOGY", "Disease study"),
        ("NEUROLOGY", "Nervous system study"),
        ("CARDIOLOGY", "Heart study"),
        ("PULMONOLOGY", "Lung study"),
        ("GASTROENTEROLOGY", "Digestive system study"),
        ("NEPHROLOGY", "Kidney study"),
        ("ENDOCRINOLOGY", "Hormone study"),
        ("IMMUNOLOGY", "Immune system study"),
        ("HEMATOLOGY", "Blood study"),
        ("ONCOLOGY", "Cancer study"),
        ("DERMATOLOGY", "Skin study"),
        ("ORTHOPEDICS", "Bone study"),
        ("PSYCHIATRY", "Mental health study"),
        ("SURGERY", "Surgical procedure"),
        ("DIAGNOSIS", "Disease diagnosis"),
        ("PROGNOSIS", "Disease prediction"),
        ("THERAPY", "Treatment method"),
        ("PHARMACOLOGY", "Drug study"),
        ("VACCINATION", "Vaccine administration"),
        ("ANTIBIOTICS", "Antibiotic drugs"),
        ("VIRUS", "Viral pathogen"),
        ("BACTERIA", "Bacterial pathogen"),
        ("IMMUNE_SYSTEM", "Immune response system"),
        ("INFLAMMATION", "Inflammatory response"),
        ("HORMONE", "Hormonal molecule"),
        ("NEUROTRANSMITTER", "Neurotransmitter molecule"),
        ("SYNAPSE", "Neural synapse"),
        ("NEURAL_PATHWAY", "Neural pathway"),
    ]
    return [create_waveform_symbol(name, "medicine", description=desc) for name, desc in concepts]


def generate_psychology() -> List[WaveformSymbol]:
    """Generate psychology and behavior symbols."""
    concepts = [
        ("COGNITION", "Cognitive process"),
        ("PERCEPTION", "Perception process"),
        ("ATTENTION", "Attention mechanism"),
        ("MEMORY", "Memory process"),
        ("LEARNING", "Learning process"),
        ("CONDITIONING", "Behavioral conditioning"),
        ("EMOTION", "Emotional response"),
        ("MOTIVATION", "Motivational drive"),
        ("PERSONALITY", "Personality traits"),
        ("BEHAVIOR", "Behavioral pattern"),
        ("PSYCHOLOGY", "Psychology study"),
        ("PSYCHOTHERAPY", "Therapeutic treatment"),
        ("NEUROSCIENCE", "Brain and nervous system"),
        ("CONSCIOUSNESS", "Conscious awareness"),
        ("UNCONSCIOUS", "Unconscious mind"),
        ("DREAM", "Dream state"),
        ("SLEEP", "Sleep state"),
        ("STRESS", "Stress response"),
        ("ANXIETY", "Anxiety disorder"),
        ("DEPRESSION", "Depressive state"),
        ("PHOBIA", "Phobic response"),
        ("ADDICTION", "Addictive behavior"),
        ("TRAUMA", "Traumatic experience"),
        ("DEVELOPMENT", "Developmental psychology"),
        ("COGNITION_BIAS", "Cognitive bias"),
        ("REINFORCEMENT", "Behavioral reinforcement"),
        ("PUNISHMENT", "Behavioral punishment"),
        ("REWARD", "Reward mechanism"),
        ("HABIT", "Habitual behavior"),
        ("INSTINCT", "Instinctual behavior"),
    ]
    return [create_waveform_symbol(name, "psychology", description=desc) for name, desc in concepts]


def generate_sociology() -> List[WaveformSymbol]:
    """Generate sociology and social science symbols."""
    concepts = [
        ("SOCIETY", "Social organization"),
        ("CULTURE", "Cultural system"),
        ("COMMUNITY", "Community group"),
        ("GROUP", "Social group"),
        ("INSTITUTION", "Social institution"),
        ("FAMILY", "Family unit"),
        ("ROLE", "Social role"),
        ("STATUS", "Social status"),
        ("NORM", "Social norm"),
        ("VALUE", "Social value"),
        ("CLASS", "Social class"),
        ("STRATIFICATION", "Social stratification"),
        ("MOBILITY", "Social mobility"),
        ("EQUALITY", "Social equality"),
        ("INEQUALITY", "Social inequality"),
        ("CONFLICT", "Social conflict"),
        ("COOPERATION", "Social cooperation"),
        ("TRADITION", "Traditional practice"),
        ("CHANGE", "Social change"),
        ("DEVIANCE", "Deviant behavior"),
        ("CONFORMITY", "Conformist behavior"),
        ("SOCIALIZATION", "Social learning"),
        ("ORGANIZATION", "Organizational structure"),
        ("GOVERNANCE", "Governance system"),
        ("POWER", "Power dynamics"),
        ("AUTHORITY", "Authority structure"),
        ("LEGITIMACY", "Legitimacy concept"),
        ("REVOLUTION", "Revolutionary change"),
        ("REFORM", "Social reform"),
        ("JUSTICE", "Social justice"),
    ]
    return [create_waveform_symbol(name, "sociology", description=desc) for name, desc in concepts]


def generate_economics() -> List[WaveformSymbol]:
    """Generate economics and business symbols."""
    concepts = [
        ("ECONOMICS", "Economic study"),
        ("SUPPLY", "Supply concept"),
        ("DEMAND", "Demand concept"),
        ("MARKET", "Market mechanism"),
        ("PRICE", "Price mechanism"),
        ("COST", "Cost analysis"),
        ("PROFIT", "Profit concept"),
        ("REVENUE", "Revenue concept"),
        ("INVESTMENT", "Investment decision"),
        ("CAPITAL", "Capital resource"),
        ("LABOR", "Labor resource"),
        ("PRODUCTION", "Production process"),
        ("CONSUMPTION", "Consumption behavior"),
        ("TRADE", "Trade activity"),
        ("CURRENCY", "Currency exchange"),
        ("INFLATION", "Inflation concept"),
        ("DEFLATION", "Deflation concept"),
        ("RECESSION", "Economic recession"),
        ("GROWTH", "Economic growth"),
        ("GDP", "Gross domestic product"),
        ("UNEMPLOYMENT", "Unemployment rate"),
        ("WAGE", "Wage payment"),
        ("TARIFF", "Trade tariff"),
        ("SUBSIDY", "Subsidy program"),
        ("LOAN", "Loan concept"),
        ("INTEREST", "Interest rate"),
        ("DEBT", "Debt obligation"),
        ("CREDIT", "Credit system"),
        ("BANK", "Banking institution"),
        ("STOCK_MARKET", "Stock market"),
    ]
    return [create_waveform_symbol(name, "economics", description=desc) for name, desc in concepts]


def generate_history() -> List[WaveformSymbol]:
    """Generate history and civilization symbols."""
    concepts = [
        ("ANCIENT_HISTORY", "Ancient era"),
        ("MEDIEVAL_HISTORY", "Medieval era"),
        ("RENAISSANCE", "Renaissance period"),
        ("ENLIGHTENMENT", "Enlightenment period"),
        ("INDUSTRIAL_REVOLUTION", "Industrial revolution"),
        ("MODERN_ERA", "Modern era"),
        ("CIVILIZATION", "Civilization concept"),
        ("EMPIRE", "Empire concept"),
        ("KINGDOM", "Kingdom concept"),
        ("REPUBLIC", "Republic form"),
        ("MONARCHY", "Monarchy system"),
        ("DEMOCRACY", "Democratic system"),
        ("TYRANNY", "Tyrannical system"),
        ("WAR", "Warfare concept"),
        ("PEACE", "Peace concept"),
        ("CONQUEST", "Territorial conquest"),
        ("COLONIZATION", "Colonial expansion"),
        ("EXPLORATION", "Exploratory voyage"),
        ("DISCOVERY", "Historical discovery"),
        ("RELIGION", "Religious system"),
        ("PHILOSOPHY", "Philosophical thought"),
        ("LITERATURE", "Literary tradition"),
        ("ART", "Artistic tradition"),
        ("SCIENCE", "Scientific development"),
        ("TECHNOLOGY", "Technological advancement"),
        ("AGRICULTURE", "Agricultural development"),
        ("ARCHITECTURE", "Architectural style"),
        ("TRADE", "Commercial trade"),
        ("MIGRATION", "Population migration"),
        ("REVOLUTION", "Revolutionary movement"),
    ]
    return [create_waveform_symbol(name, "history", description=desc) for name, desc in concepts]


def generate_philosophy() -> List[WaveformSymbol]:
    """Generate philosophy and metaphysics symbols."""
    concepts = [
        ("METAPHYSICS", "Metaphysical study"),
        ("ONTOLOGY", "Ontological study"),
        ("EPISTEMOLOGY", "Epistemological study"),
        ("ETHICS", "Ethical philosophy"),
        ("AESTHETICS", "Aesthetic philosophy"),
        ("LOGIC", "Logical philosophy"),
        ("METAPHOR", "Metaphorical concept"),
        ("EXISTENCE", "Existential concept"),
        ("BEING", "Being concept"),
        ("ESSENCE", "Essence concept"),
        ("SUBSTANCE", "Substance concept"),
        ("FORM", "Form concept"),
        ("MATTER", "Matter concept"),
        ("CAUSALITY", "Causality principle"),
        ("DETERMINISM", "Deterministic view"),
        ("FREE_WILL", "Free will concept"),
        ("KNOWLEDGE", "Knowledge concept"),
        ("TRUTH", "Truth concept"),
        ("FALSEHOOD", "Falsehood concept"),
        ("BELIEF", "Belief concept"),
        ("VIRTUE", "Virtue concept"),
        ("VICE", "Vice concept"),
        ("GOOD", "Good concept"),
        ("EVIL", "Evil concept"),
        ("JUSTICE", "Justice concept"),
        ("DUTY", "Duty concept"),
        ("OBLIGATION", "Obligation concept"),
        ("RIGHTS", "Rights concept"),
        ("RELATIVISM", "Relativistic view"),
        ("ABSOLUTISM", "Absolutistic view"),
    ]
    return [create_waveform_symbol(name, "philosophy", description=desc) for name, desc in concepts]


def generate_art_music_literature() -> List[WaveformSymbol]:
    """Generate art, music, and literature symbols."""
    concepts = [
        ("PAINTING", "Painting art form"),
        ("SCULPTURE", "Sculpture art form"),
        ("DRAWING", "Drawing art form"),
        ("ARCHITECTURE", "Architectural art"),
        ("PHOTOGRAPHY", "Photography art"),
        ("DANCE", "Dance art form"),
        ("THEATER", "Theater art form"),
        ("MUSIC", "Musical art"),
        ("SYMPHONY", "Symphony composition"),
        ("SONATA", "Sonata form"),
        ("CONCERTO", "Concerto composition"),
        ("OPERA", "Opera form"),
        ("POETRY", "Poetic form"),
        ("PROSE", "Prose form"),
        ("NOVEL", "Novel form"),
        ("DRAMA", "Dramatic form"),
        ("COMEDY", "Comedy genre"),
        ("TRAGEDY", "Tragedy genre"),
        ("ROMANCE", "Romance genre"),
        ("NARRATIVE", "Narrative structure"),
        ("CHARACTER", "Character concept"),
        ("PLOT", "Plot structure"),
        ("THEME", "Thematic concept"),
        ("MOTIF", "Motif pattern"),
        ("SYMBOL", "Symbolic representation"),
        ("METAPHOR", "Metaphorical expression"),
        ("ALLEGORY", "Allegorical narrative"),
        ("STYLE", "Artistic style"),
        ("MOVEMENT", "Artistic movement"),
        ("RENAISSANCE_ART", "Renaissance artistic period"),
    ]
    return [create_waveform_symbol(name, "art_music_literature", description=desc) for name, desc in concepts]


def generate_geography_geology() -> List[WaveformSymbol]:
    """Generate geography and geology symbols."""
    concepts = [
        ("GEOGRAPHY", "Geographic study"),
        ("GEOLOGY", "Geological study"),
        ("EARTH", "Earth concept"),
        ("CONTINENT", "Continental mass"),
        ("OCEAN", "Oceanic body"),
        ("MOUNTAIN", "Mountain formation"),
        ("VALLEY", "Valley formation"),
        ("PLAIN", "Plain formation"),
        ("DESERT", "Desert region"),
        ("FOREST", "Forest region"),
        ("TUNDRA", "Tundra region"),
        ("CLIMATE", "Climate pattern"),
        ("WEATHER", "Weather phenomenon"),
        ("PRECIPITATION", "Precipitation form"),
        ("WIND", "Wind phenomenon"),
        ("EROSION", "Erosion process"),
        ("SEDIMENT", "Sedimentary material"),
        ("ROCK", "Rock formation"),
        ("MINERAL", "Mineral substance"),
        ("CRYSTAL", "Crystal structure"),
        ("PLATE_TECTONICS", "Plate tectonics theory"),
        ("EARTHQUAKE", "Seismic event"),
        ("VOLCANO", "Volcanic activity"),
        ("ISLAND", "Island formation"),
        ("RIVER", "River formation"),
        ("LAKE", "Lake formation"),
        ("GLACIER", "Glacial formation"),
        ("FOSSIL", "Fossil remains"),
        ("STRATUM", "Rock layer"),
        ("PALEONTOLOGY", "Fossil study"),
    ]
    return [create_waveform_symbol(name, "geography_geology", description=desc) for name, desc in concepts]


def generate_astronomy_cosmology() -> List[WaveformSymbol]:
    """Generate astronomy and cosmology symbols."""
    concepts = [
        ("ASTRONOMY", "Astronomical study"),
        ("COSMOLOGY", "Cosmological study"),
        ("UNIVERSE", "Universal concept"),
        ("GALAXY", "Galaxy structure"),
        ("STAR", "Stellar object"),
        ("PLANET", "Planetary body"),
        ("MOON", "Lunar body"),
        ("ASTEROID", "Asteroid object"),
        ("COMET", "Cometary object"),
        ("METEOR", "Meteoroid object"),
        ("BLACK_HOLE", "Black hole"),
        ("NEUTRON_STAR", "Neutron star"),
        ("PULSAR", "Pulsar star"),
        ("SUPERNOVA", "Supernova event"),
        ("NEBULA", "Nebular cloud"),
        ("QUASAR", "Quasi-stellar object"),
        ("PULSAR_WIND", "Pulsar wind"),
        ("LIGHT_YEAR", "Distance unit"),
        ("PARALLAX", "Parallax measurement"),
        ("REDSHIFT", "Redshift phenomenon"),
        ("BLUESHIFT", "Blueshift phenomenon"),
        ("DOPPLER_EFFECT", "Doppler effect"),
        ("RADIATION", "Cosmic radiation"),
        ("BIG_BANG", "Big Bang theory"),
        ("EXPANSION", "Universal expansion"),
        ("CONTRACTION", "Universal contraction"),
        ("SINGULARITY", "Singularity point"),
        ("ENTROPY", "Entropic increase"),
        ("ORBITS", "Orbital mechanics"),
        ("GRAVITY_WELL", "Gravitational well"),
    ]
    return [create_waveform_symbol(name, "astronomy_cosmology", description=desc) for name, desc in concepts]


def generate_linguistics() -> List[WaveformSymbol]:
    """Generate linguistics and language symbols."""
    concepts = [
        ("LANGUAGE", "Language system"),
        ("LINGUISTICS", "Linguistic study"),
        ("PHONETICS", "Sound study"),
        ("PHONOLOGY", "Sound system"),
        ("MORPHOLOGY", "Word structure"),
        ("SYNTAX", "Sentence structure"),
        ("SEMANTICS", "Meaning study"),
        ("PRAGMATICS", "Usage context"),
        ("GRAMMAR", "Grammatical system"),
        ("NOUN", "Noun part of speech"),
        ("VERB", "Verb part of speech"),
        ("ADJECTIVE", "Adjective part of speech"),
        ("ADVERB", "Adverb part of speech"),
        ("PREPOSITION", "Preposition part of speech"),
        ("CONJUNCTION", "Conjunction part of speech"),
        ("DIALECT", "Dialect variation"),
        ("ACCENT", "Accent pronunciation"),
        ("ETYMOLOGY", "Word origin"),
        ("VOCABULARY", "Word collection"),
        ("IDIOM", "Idiomatic expression"),
        ("METAPHOR", "Metaphorical language"),
        ("SIMILE", "Simile comparison"),
        ("ANALOGY", "Analogical reasoning"),
        ("TRANSLATION", "Language translation"),
        ("BILINGUAL", "Bilingual ability"),
        ("MULTILINGUAL", "Multilingual ability"),
        ("LITERACY", "Literacy skill"),
        ("WRITING_SYSTEM", "Writing system"),
        ("ALPHABET", "Alphabetic system"),
        ("WRITING", "Written expression"),
    ]
    return [create_waveform_symbol(name, "linguistics", description=desc) for name, desc in concepts]


def generate_general_knowledge() -> List[WaveformSymbol]:
    """Generate general knowledge and meta-concepts."""
    concepts = [
        ("INFORMATION", "Information concept"),
        ("DATA", "Data concept"),
        ("KNOWLEDGE", "Knowledge concept"),
        ("WISDOM", "Wisdom concept"),
        ("UNDERSTANDING", "Understanding concept"),
        ("INTELLIGENCE", "Intelligence concept"),
        ("CREATIVITY", "Creativity concept"),
        ("INNOVATION", "Innovation concept"),
        ("DISCOVERY", "Discovery concept"),
        ("INVENTION", "Invention concept"),
        ("THEORY", "Theoretical framework"),
        ("HYPOTHESIS", "Hypothetical proposal"),
        ("EXPERIMENT", "Experimental method"),
        ("OBSERVATION", "Observational method"),
        ("ANALYSIS", "Analytical method"),
        ("SYNTHESIS", "Synthetic method"),
        ("CRITIQUE", "Critical analysis"),
        ("INFERENCE", "Inferential reasoning"),
        ("DEDUCTION", "Deductive reasoning"),
        ("INDUCTION", "Inductive reasoning"),
        ("ABDUCTION", "Abductive reasoning"),
        ("PARADIGM", "Paradigmatic framework"),
        ("MODEL", "Model concept"),
        ("SIMULATION", "Simulation concept"),
        ("PATTERN", "Pattern recognition"),
        ("SYMMETRY", "Symmetry concept"),
        ("BALANCE", "Balance concept"),
        ("HARMONY", "Harmony concept"),
        ("ORDER", "Order concept"),
        ("CHAOS", "Chaos concept"),
    ]
    return [create_waveform_symbol(name, "general_knowledge", description=desc) for name, desc in concepts]


def symbol_to_dict(symbol: WaveformSymbol) -> dict:
    """Convert symbol to JSON-serializable dict."""
    return {
        "name": symbol.name,
        "frequency": symbol.frequency,
        "phase": symbol.phase,
        "amplitude": symbol.amplitude,
        "harmonic": symbol.harmonic,
        "envelope": symbol.envelope,
        "category": symbol.category,
        "opcode": symbol.opcode,
        "description": symbol.description,
    }


def save_symbols(filepath: str, symbols: List[WaveformSymbol]) -> None:
    """Save symbols to a JSON file."""
    data = [symbol_to_dict(s) for s in symbols]
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
    print(f"Saved {len(symbols)} symbols to {filepath}")


def main() -> int:
    """Generate comprehensive universal knowledge base."""
    generators = [
        ("biology.json", generate_biology),
        ("medicine.json", generate_medicine),
        ("psychology.json", generate_psychology),
        ("sociology.json", generate_sociology),
        ("economics.json", generate_economics),
        ("history.json", generate_history),
        ("philosophy.json", generate_philosophy),
        ("art_music_literature.json", generate_art_music_literature),
        ("geography_geology.json", generate_geography_geology),
        ("astronomy_cosmology.json", generate_astronomy_cosmology),
        ("linguistics.json", generate_linguistics),
        ("general_knowledge.json", generate_general_knowledge),
    ]

    all_symbols: List[WaveformSymbol] = []
    
    for filename, generator_fn in generators:
        symbols = generator_fn()
        save_symbols(filename, symbols)
        all_symbols.extend(symbols)
        print(f"  Generated {len(symbols)} {generator_fn.__doc__.strip()}")

    print(f"\nTotal knowledge symbols generated: {len(all_symbols)}")
    print(f"Symbol categories:")
    categories = {}
    for symbol in all_symbols:
        categories[symbol.category] = categories.get(symbol.category, 0) + 1
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
