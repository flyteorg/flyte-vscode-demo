# Flyte Hosted Sandbox Demo

This repo contains source code for the [sandbox.union.ai](https://sandbox.union.ai/) demo.

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

1. Create a Model Training Workflow in Python: `flyte_demo/workflows/python_workflow.py` (with corresponding `.md` file)
2. Convert your Python Workflow to a Flyte Workflow: `flyte_demo/workflows/flyte_workflow.py` (with corresponding `.md` file)
2. Executing your Flyte Workflows: `flyte_demo/executing_workflows.md`
3. Inspect the Results on Flyte console: `flyte_demo/inspect_the_results.md`
4. Interacting with the Flyte Console: `flyte_demo/interact_with_a_flyte_cluster.ipynb`
5. Iterating on your Workflows: `flyte_demo/workflows/iterating.py` (with corresponding `.md` file)
6. Parallelizing your Workflows: `flyte_demo/workflows/parallelism.py` (with corresponding `.md` file)
7. What's Next: `flyte_demo/whats_next.md`


## NOTE
1. This APP name is also added to ``docker_build_and_tag.sh`` - ``APP_NAME``
2. We recommend using a git repository and this the ``docker_build_and_tag.sh``
   to build your docker images
3. We also recommend using pip-compile to build your requirements.
