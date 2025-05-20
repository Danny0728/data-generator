import json
from mild import generate_mild
from noise import generate_noise
from word_salad import generate_wordsalad
from tqdm import tqdm
from bias import generate_bias
from safe import generate_safe
from toxicity import generate_toxicity
from prompt_injection import generate_injections


class DatasetGenerator:
    def __init__(self, model, batch_size, total_count, labels):
        """
        Initialize the Dataset Generator with common settings.
        model: Model to be used for all data generation.
        batch_size: Number of entries to save to file in each batch.
        """
        self.model = model
        self.batch_size = batch_size
        if not self.is_power_of_two(total_count):
            raise ValueError(f"Total count {total_count} must be a power of two.")
        
        self.total_count = total_count
        self.labels = labels
    
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        """
        Check if a number is a power of two.
        """
        return n > 0 and (n & (n - 1)) == 0
    
    def save_to_jsonl(self, data, file_path):
        """
        Save a list of dictionaries to a JSONL file.
        """
        with open(file_path, 'a') as f:
            for entry in data:
                f.write(json.dumps(entry) + '\n')

    def generate_each_category(self, generate_func, total_count, file_path):
        """
        Generate data for a specific category using a given function.
        generate_func: Function to generate data for the category.
        total_count: Total number of entries to generate per category.
        file_path: Path to save the generated data.
        """
        self.file_path = file_path
        generate_func(total_count, self)

    
    def generate_subcategory(self, subtypes, total_count_per_parent_category, file_path):
        """
        Centralized method to generate data for multiple subcategories.
            subtypes: List of tuples with subtype name and generation function.
            total_count: Total number of rows to generate across all subcategories.
            file_path_template: Template for the file path to save each subcategory's data.
        """
        count_per_subtype = total_count_per_parent_category // len(subtypes)
        for subtype_name, generate_func in subtypes:
            
            generated_count = 0
            all_data = []

            with tqdm(total=count_per_subtype, desc=f"Generating {subtype_name}") as pbar:
                while generated_count < count_per_subtype:
                    data = generate_func()
                    if data:
                        all_data.append(data)
                        generated_count += 1
                        pbar.update(1)

                    if len(all_data) >= self.batch_size or generated_count == count_per_subtype:
                        self.save_to_jsonl(all_data, file_path)
                        all_data = []

            # print(f"Completed generating {count_per_subtype} examples for subtype: {subtype_name}.")

    def generate_all(self):
        """
        Generate datasets for all categories.
        total_count: Total number of entries to generate across all categories.
        """
        folder_path = "dataset/train"
        categories = [
            # ("mild", generate_mild, f"{folder_path}/mild.jsonl"),
            # ("noise", generate_noise, f"{folder_path}/noise.jsonl"),
            # ("word salad", generate_wordsalad, f"{folder_path}/word_salad.jsonl"),
            # ("bias", generate_bias, f"{folder_path}/bias.jsonl")
            # ("safe", generate_safe, f"{folder_path}/safe.jsonl")
            # ("toxicity", generate_toxicity, f"{folder_path}/toxicity.jsonl")
            ("prompt_injection", generate_injections, f"{folder_path}/prompt_injection.jsonl")

        ]

        count_per_category = self.total_count // len(categories)

        # print(f"There will be {count_per_category} rows of data in each parent category {self.labels}")

        with tqdm(total=len(categories), desc="Overall Dataset Progress") as category_pbar:
            for category_name, generate_func, file_path in categories:
                # print(f"CATEGORY NAME: {category_name} FILEPATH: {file_path}")
                print(f"\nGenerating {count_per_category} examples for category: {category_name} \n")
                self.generate_each_category(generate_func, count_per_category, file_path)
                category_pbar.update(1)
