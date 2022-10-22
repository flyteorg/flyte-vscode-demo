from dataclasses import dataclass
from typing import Annotated, List

import pandas as pd
from dataclasses_json import dataclass_json
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

from flytekit import task, workflow, map_task
from flytekit.types.pickle import FlytePickle
from flytekit.types.structured import StructuredDataset


# 📦 Define a TrainArgs dataclass to contain hyperparameters and the dataset
@dataclass_json
@dataclass
class TrainArgs:
    hyperparameters: dict
    data: StructuredDataset


@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame


@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Simplify the task from a 3-class to a binary classification problem."""
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


# 🧱 Define a prepare_train_args task to prepare the collection of inputs to
# the map task
@task
def prepare_train_args(hp_grid: List[dict], data: StructuredDataset) -> List[TrainArgs]:
    return [TrainArgs(hp, data) for hp in hp_grid]


# ✨ Update the train_model task to accept a single argument of type TrainArgs
@task(cache=True, cache_version="1", retries=3)
def train_model(args: TrainArgs) -> FlytePickle:
    """Train a model on the wine dataset."""
    data: pd.DataFrame = args.data.open(pd.DataFrame).all()
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(**args.hyperparameters).fit(features, target)


@workflow
def training_workflow(hp_grid: List[dict]) -> List[FlytePickle]:
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    # 🎁 wrap the train_model task in map_task, with a concurrency of 5 executions
    # at any given time.
    return map_task(train_model, concurrency=5)(
        args=prepare_train_args(hp_grid=hp_grid, data=processed_data)
    )


if __name__ == "__main__":
    hp_grid = [{"C": x, "max_iter": 1000} for x in (0.1, 0.01, 0.001)]
    print(
        "Running training_workflow() "
        f"{training_workflow(hp_grid=hp_grid)}"
    )
