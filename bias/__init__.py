from bias.bias import generate

def generate_bias(total_count, generator):
    subtypes = [
        ("bias", generate),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)