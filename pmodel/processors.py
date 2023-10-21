"""
This file contains components for developing processors,
and some default built-in processors.

A 'processor' is a callable that takes a single container as input,
and returns a resulting container.
Processors *must* return a container, even if processing is done in place.
A processor can be a simple function, or a class that provides a callable interface.
For complex processors that must maintain state, it is recommended to use the 'BaseProcessor'
class, defined below.
Processors can do many things, including but not limited to:

 - Altering the data in the container in some way
 - Converting to a new container type
 - Logging container information for debugging
"""

from pmodel.containers import BaseContainer


class BaseProcessor:
    """
    A base class for processors.

    A 'processor' is a callable object that takes in a container
    and does something with it.
    Once processing is done, then the processor *must* return a container,
    even if processing is done in place.
    Processors are not required to utilize this class or be classes,
    but for processors that must maintain state, it is recommended to use this class.

    This class implements a callable interface for processors,
    allowing them to be utilized in pipelines.
    For implementing your own functionality, it is recommended to
    override the 'process' method, which will be called when processing is necessary.
    """

    def process(container: BaseContainer) -> BaseContainer:
        """
        Process the container.

        This method is called when processing is necessary.
        This method should be overridden by subclasses.

        Args:
            container (BaseContainer): Container to process

        Raises:
            NotImplementedError: This method must be overridden by subclasses

        Returns:
            BaseContainer: Resultant container
        """

        raise NotImplementedError

    def __call__(self, container: BaseContainer) -> BaseContainer:
        """
        Call method for this processor.

        We simply call the 'process' method, which should be overridden by subclasses.

        Args:
            container (BaseContainer): Container to process

        Returns:
            BaseContainer: Resultant container
        """

        # Simply call the processing method:

        return self.process(container)


###
# Builtin Processors
###


def null_process(container: BaseContainer) -> BaseContainer:
    """
    Does nothing!
    We simply return the container provided to us.

    Args:
        container (BaseContainer): Container to not process

    Returns:
        BaseContainer: Container we were given
    """

    return container


def print_process(container: BaseContainer) -> BaseContainer:
    """
    Print the container to stdout.

    Args:
        container (BaseContainer): Container to print

    Returns:
        BaseContainer: Container we were given
    """

    print(container)

    return container
