# Iterate on your Workflows

The training workflow we've been working with so far works, but to
make it even more useful, we can leverage some more built-in Flyte
features, which you can see in `iterating.py`.

## Structured Datasets

Flyte come with its own type system, supporting almost all of the
[built-in Python types](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/flyte_python_types.html#sphx-glr-auto-core-type-system-flyte-python-types-py),
but it also exposes a [`StructuredDataset`](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/type_system/structured_dataset.html) type,
which we can use to create types for objects like `pandas.DataFrame`s.

## Caching

Add `cache=True` with a `cache_version` string to the `@task` decorator to [cache](https://docs.flyte.org/projects/cookbook/en/latest/auto/core/flyte_basics/task_cache.html#sphx-glr-auto-core-flyte-basics-task-cache-py) the output of the task. This
will ensure that you don't re-run the task if you give it the same exact inputs.

## Retries

In the event of system-level or external errors, setting `@task(..., retries=n)` (where
`n` is an integer) gives you the ability to automatically retry the task execution.

## Updating Tasks

You can refactor your tasks and workflows like you would regular Python code. In
the `iterating.py` script you can see that we've added a `hyperparameter: dict`
argument to the `train_model` and `training_workflow` so that you can train models
with different settings.

Once you're happy with the updates, simply rerun it with:

```
pyflyte run --remote flyte_demo/workflows/iterating.py training_workflow --hyperparameters '{"C": 0.1, "max_iter": 1000}'
```
