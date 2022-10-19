# Flyte Hosted Sandbox Demo

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Setup

For the jupyter notebook in `flyte_demo/inspecting_results.ipynb` to work,
the following environment variables need to be set:

```
export FLYTE_AWS_ENDPOINT="http://localhost:30084/"
export FLYTE_AWS_ACCESS_KEY_ID="minio"
export FLYTE_AWS_SECRET_ACCESS_KEY="miniostorage"
```

## Examples

This repo contains scripts and notebooks that contained in this notebook
should be presented via the Flyte VSCode extension in the following order:

1. Create a Model Training Workflow in Python: `flyte_demo/workflows/python_workflow.py`
2. Convert your Python Workflow to a Flyte Workflow: `flyte_demo/workflows/flyte_workflow.py`
3. Executing Workflows Locally: `pyflyte run flyte_workflow.py training_workflow`
4. Executing Workflows on a Flyte Cluster: `pyflyte run --remote flyte_workflow.py training_workflow`
5. Inspect the Results: `flyte_demo/inspecting_results.ipynb`
6. Next Steps:



## NOTE
1. This APP name is also added to ``docker_build_and_tag.sh`` - ``APP_NAME``
2. We recommend using a git repository and this the ``docker_build_and_tag.sh``
   to build your docker images
3. We also recommend using pip-compile to build your requirements.
