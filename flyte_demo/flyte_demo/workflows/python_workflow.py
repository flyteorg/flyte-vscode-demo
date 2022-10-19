"""Create a Model Training Workflow in Plain Python

In this first example, we're going to create a simple model training
workflow in plain Python using the wine dataset and sklearn. As you can see,
we define three functions for getting data, processing data, and training a
model, which we put together into a function called `training_workflow`.

You can run this locally by running

```python
python python_workflow.py
```
"""

from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression


def get_data():
    return load_wine(as_frame=True).frame


def process_data(data):
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


def train_model(data):
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=1000).fit(features, target)


def training_workflow():
    data = get_data()
    processed_data = process_data(data)
    return train_model(processed_data)


if __name__ == "__main__":
    print(f"Running training_workflow() {training_workflow()}")
