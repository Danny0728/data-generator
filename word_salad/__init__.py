from word_salad.word_salad import generate as generate_word_salad
from word_salad.grammatical import generate as generate_grammatical

def generate_wordsalad(total_count, generator):
    subtypes = [
        ("word salad", generate_word_salad),
        ("grammatical", generate_grammatical),
    ]

    generator.generate_subcategory(subtypes, total_count , generator.file_path)
