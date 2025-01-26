from toxicity.toxicity import generate


def generate_toxicity(total_count, generator):
    subtypes = [
        ("toxicity", generate),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)