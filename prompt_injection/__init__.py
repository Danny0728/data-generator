from prompt_injection.prompt_injection import generate


def generate_injections(total_count, generator):
    subtypes = [
        ("prompt_injection", generate),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)