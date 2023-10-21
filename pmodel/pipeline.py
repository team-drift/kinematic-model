"""
This file contains a basic framework for processing incoming data.

The goals of this system is to provide a modular, hot-swappable
system for processing incoming data. This will allow us to easily
alter the processing pipeline without having to change the rest of
project in a meaningful way, allowing for (hopefully)
easy configuration and testing.

The basic idea is that we have a set of processors (see elsewhere) that preforms an action
on incoming data. These processors are then chained together in a pipeline,
which containers are submitted to, processed by each processor in the pipeline,
and then outputted to be used elsewhere in the model.

A 'pipeline' is a list of processors that are chained together.
A pipeline is a callable that takes in a container,
which then processes the container through each processor in the pipeline in order.
A pipeline is used to process data before it is considered by the prediction model.
"""

from collections import UserList

from pmodel.containers import BaseContainer
from pmodel.processors import BaseProcessor


class Pipeline(UserList):
    """
    Pipeline for processing incoming containers.

    A pipeline is a list of processors that are chained together.
    They are executed in order on the incoming containers.
    The index of the processor in the pipeline is the order in which it is executed,
    meaning that lower indexes are executed first.
    
    This class inherits from the built-in list class,
    so we support all of the list operations.
    Processors can be popped, appended, inserted, ect.

    This class is a callable, so it can be called with a container as an argument.
    The final result of the pipeline is returned.
    Interestingly enough, this class can be treated as a processor,
    meaning that a pipeline can be a processor in another pipeline,
    allowing for nested processing pipelines.

    TODO: Maybe something more structured?
    My problem is that if some processors are incompatible,
    then we will see problems.
    """

    def __call__(self, container: BaseContainer) -> BaseContainer:
        """
        Process the container through the pipeline.

        This method takes in a container, and processes it through each processor
        in the pipeline in order. The result of the last processor is returned.

        Args:
            container (BaseContainer): Container to process

        Returns:
            BaseContainer: Resultant container
        """

        # Process the container through each processor in the pipeline
        for processor in self.data:
            container = processor(container)

        # Return the final container
        return container
