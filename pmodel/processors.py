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
from pmodel.globals import org_lat, org_long, org_alt


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


class TimeZeroProcessor(BaseProcessor):
    """
    TimeZeroProcessor - Processor to zero the time to the start of the flight.

    Data coming from the tracked object will have a time since the boot of the system.
    However, we want to have the time since the start of the flight,
    so this processor will save the first time we receive and subtract all future times by it.

    TODO: Is it possible to receive data out of order, so the first time is not the start time?
    """

    def __init__(self) -> None:
        super().__init__()

        self.start_time = None

    def process(self, container: BaseContainer) -> BaseContainer:
        """
        Process the container.

        This method takes in a container, and sets the time to zero.

        Args:
            container (BaseContainer): Container to process

        Returns:
            BaseContainer: Resultant container
        """

        # Determine if we need to set a start time:

        if self.start_time is None:

            # Set the start time:

            self.start_time = container.time

        # Determine the new time:

        container.time -= self.start_time

        # Return the container:

        return container


class SetOriginProcessor(BaseProcessor):
    """
    SetOriginProcessor - Processor to set the origin of the data.

    When we receive the the first container,
    we extract the position and set it as the origin.
    """

    def __init__(self) -> None:
        super().__init__()

        self.origin_set = False

    def process(self, container: BaseContainer) -> BaseContainer:
        """
        Process the container.

        This method takes in a container, and sets the origin.

        Args:
            container (BaseContainer): Container to process

        Returns:
            BaseContainer: Resultant container
        """

        # Yeah this is not the best way to go about it.
        # Maybe this processor can attach the origin to the container?
        global org_lat, org_long, org_alt

        # Determine if we need to set the origin:

        if not self.origin_set:

            # Set the origin:

            org_lat = container.lat
            org_long = container.long
            org_alt = container.alt

            self.origin_set = True

        # Print the origin:

        print(f"Origin: {org_lat}, {org_long}, {org_alt}")

        # Return the container:

        return container


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
