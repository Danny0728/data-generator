from safe.safe import generate


def generate_safe(total_count, generator):
    subtypes = [
        ("safe", generate),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)