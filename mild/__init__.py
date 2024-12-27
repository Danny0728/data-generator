from mild.phonetic import generate as generate_phonetic
from mild.jargon import generate as generate_jargon

def generate_mild(total_count, generator):
    subtypes = [
        ("phonetic", generate_phonetic),
        ("jargon", generate_jargon),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)
            
