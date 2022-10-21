from typing import Annotated

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

from flytekit import task, workflow, kwtypes
from flytekit.types.pickle import FlytePickle
from flytekit.types.structured import StructuredDataset


# 🍷 Create a type for the wine dataset
WineDataset = Annotated[
    StructuredDataset,
    kwtypes(
        alcohol=float,
        malic_acid=float,
        ash=float,
        alcalinity_of_ash=float,
        magnesium=float,
        total_phenols=float,
        flavanoids=float,
        nonflavanoid_phenols=float,
        proanthocyanins=float,
        color_intensity=float,
        hue=float,
        od280_od315_of_diluted_wines=float,
        proline=float,
        target=int,
    )
]


@task
def get_data() -> pd.DataFrame:
    return load_wine(as_frame=True).frame.rename(columns=lambda x: x.replace("/", "_"))


@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


# Update the train_model task:
# 1. 🎒 Set `cache=True` with a `cache_version` string to prevent re-running the function
#    given the same inputs.
# 2. 🔄 Add `retries=3` to retry the task in the event of system-level failures.
# 3. 🍷 Annotate the `data` argument with the `WineDataset` type that we defined above.
# 4. 📄 Add a `hyperparameters: dict` input to experiment with different model settings.
@task(cache=True, cache_version="1", retries=3)
def train_model(hyperparameters: dict, data: WineDataset) -> FlytePickle:
    data: pd.DataFrame = data.open(pd.DataFrame).all()
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(**hyperparameters).fit(features, target)


# 📄 Add a `hyperparameters: dict` input to the workflow to feed into `train_model`
@workflow
def training_workflow(hyperparameters: dict) -> FlytePickle:
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(hyperparameters=hyperparameters, data=processed_data)


if __name__ == "__main__":
    print(
        "Running training_workflow() "
        f"{training_workflow(hyperparameters={'max_iter': 1000})}"
    )
