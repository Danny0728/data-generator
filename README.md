# gibberish-data-generator

This repository provides a simple tool to generate random gibberish data. It relies on a `config.py` file for quick adjustments to model parameters, batch sizes, labels, and the total number of data samples.

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
