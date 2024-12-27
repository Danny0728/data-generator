from dataset_generator import DatasetGenerator
from config import MODEL, BATCH_SIZE, TOTAL_COUNT, LABELS

if __name__ == "__main__":
    try:
        generator = DatasetGenerator(model=MODEL, 
                                     batch_size=BATCH_SIZE, 
                                     total_count=TOTAL_COUNT,
                                     labels=LABELS)
        generator.generate_all()
    except ValueError as e:
        print(f"Error: {e}")
