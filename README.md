# gibberish-data-generator

A simple utility for generating random gibberish data. This repository includes a `config.py` file for customizing parameters such as the model name, batch size, labels, and the total number of data samples. Additionally, a `tqdm` progress bar is integrated to show real-time progress during data generation.

---

## Configuration: `config.py`

Below is an example of what the `config.py` file might look like:

```python
# config.py

MODEL = "llama3.1"
BATCH_SIZE = 100
LABELS = ['mild', 'noise', 'word salad']
TOTAL_COUNT = 4096
```

## Parameter Descriptions:

`MODEL`: The name or identifier for the model. `(Default: "llama3.1")`

`BATCH_SIZE`: The number of records after which you want to append them to file. (Default: 100)

`LABELS`: Categories that can be assigned to the generated text. (Default: ['mild', 'noise', 'word salad']). <br> If you change the labels you have to make changes in the respective system and user prompts as well.

`TOTAL_COUNT`: The total number of data samples to generate. (Default: 4096)

## Run the code `generate.py`
```terminal
python generate.py
```
