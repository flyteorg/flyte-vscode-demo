from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression


def get_data():
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame


def process_data(data):
    """Simplify the task from a 3-class to a binary classification problem."""
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))


def train_model(data):
    """Train a model on the wine dataset."""
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=1000).fit(features, target)


def training_workflow():
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data)
    return train_model(processed_data)


if __name__ == "__main__":
    print(f"Running training_workflow() {training_workflow()}")
