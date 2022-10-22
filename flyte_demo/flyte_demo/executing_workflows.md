# Executing Flyte Workflows

You can run the `training_workflow` locally with:

```
pyflyte run flyte_demo/workflows/flyte_workflow.py training_workflow
```

<!-- Run locally in terminal -->

Although this may not catch all the errors you may encounter in production,
doing this helps during the development and debugging process.

Once you're happy with the state of your code, you can run your workflow
on a Flyte cluster with the `--remote` flag:

```
pyflyte run --remote flyte_demo/workflows/flyte_workflow.py training_workflow
```

<!-- Run remotely in terminal -->

**Expected output:** You should see a URL to the workflow execution on your demo Flyte cluster:

```
Go to https://sandbox.union.ai/console/projects/flytesnacks/domains/development/executions/<execution_name> to see execution in the console.
```

Where <execution_name> is a unique identifier for the workflow execution.
