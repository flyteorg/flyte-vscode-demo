# Inspect the Results

Navigate to the URL produced as the result of running pyflyte run. This will take you to FlyteConsole, the web UI used
to manage Flyte entities such as tasks, workflows, and executions.

<!-- gif -->

There are a few features about FlyteConsole worth noting in this gif:

- The default execution view shows the list of tasks executing in sequential order.
- When you click on a *task* in the execution view, a right-hand panel pops up to display metadata about the task execution, including logs, inputs, outputs, and task metadata.
- Clicking on the **Graph** tab shows the execution graph of the workflow, providing visual information about the topology of the graph and the state of each node as the workflow progresses.
- Clicking on the **Timeline** tab shows the time taken
- On completion, you can inspect the outputs of each task, and ultimately, the overarching workflow.
