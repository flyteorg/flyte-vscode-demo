"""Convert your Python Workflow to a Flyte Workflow

Next, we'll see how easy it is to port our plain Python workflow to a
Flyte workflow. Simply decorate the three functions with the `@task`
decorator and the main `training_workflow` entrypoint with the `@workflow`
decorator, and you're set!

Tasks are the fundamental units of compute in Flyte. You can think of them
as pure, containerized functions that understand the input and output types
based on the type hints that you give it.

Workflows allow you to combine these tasks together into more complex
pipelines, where data is passed from one task to the next automatically, so
you don't have to worry about how it's serialized and deserialized.
"""

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

from flytekit import task, workflow
from flytekit.types.pickle import FlytePickle


@task
def get_data() -> pd.DataFrame:
    return load_wine(as_frame=True).frame


@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


@task
def train_model(data: pd.DataFrame) -> FlytePickle:
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=1000).fit(features, target)


@workflow
def training_workflow() -> FlytePickle:
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(data=processed_data)


if __name__ == "__main__":
    print(f"Running training_workflow() {training_workflow()}")
