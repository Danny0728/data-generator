from noise.typographical import generate as generate_typographical
from noise.repetitive import generate as generate_repetitive
from noise.algorithmic import generate as generate_algorithmic

def generate_noise(total_count, generator):
    """
    Generate data for the noise category using the centralized generate_subcategory method.
    :param total_count: Total rows of data to generate for the noise category.
    :param generator: Instance of DatasetGenerator.
    """
    subtypes = [
        ("typographical", generate_typographical),
        ("repetitive", generate_repetitive),
        ("algorithmic", generate_algorithmic),
    ]
    generator.generate_subcategory(subtypes, total_count, generator.file_path)
