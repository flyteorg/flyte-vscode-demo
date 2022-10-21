# Convert your Python Workflow to a Flyte Workflow

Next, we'll see how easy it is to port our plain Python workflow to a
Flyte workflow. Simply decorate the three functions with the `@task`
decorator and the main `training_workflow` entrypoint with the `@workflow`
decorator, and you're set!

**Tasks** are the fundamental units of compute in Flyte. You can think of them
as pure, containerized functions that understand the input and output types
based on the type hints that you give it.

**Workflows** allow you to combine these tasks together into more complex
pipelines, where data is passed from one task to the next automatically, so
you don't have to worry about how it's serialized and deserialized.

Besides the `@task` and `@workflow` decorators, you'll notice that there
are a few more differences in the Flyte workflow compared to the plain Python
workflow:

1. The function signatures have type hints for input arguments and outputs.
   This is because Flyte is a strongly typed orchestration language, allowing
   it to analyze the compatibility of tasks even before running the code.
2. Inside the `training_workflow`, tasks are invoked with keyword arguments
   (`process_data(data=data)`) instead of positional arguments
   (`process_data(data)`). Flyte workflow syntax is actually a DSL
   (domain-specific language) for constructing graphs and only supports
   a subset of Python syntax.
3. The output of tasks in `@workflow`-decorated functions are not actual
   materialized values: they are actually `Promises`. These promises
   *cannot* be operated on like regular values: they can only be passed
   as arguments to downstream tasks and other Flyte-specific constructs.
   Try inserting a `print(processed_data)` statement in `training_workflow`
   to see that it's a promise and not an actual value.
