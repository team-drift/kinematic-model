"""
This file showcases the functionality of the pmodel library.    
"""

from pmodel.containers import Coordinates
from pmodel.pipeline import Pipeline
from pmodel.processors import *
from pmodel.globals import *

# Create a pipeline:

pipeline = Pipeline()

# Add some processors to the pipeline:

pipeline.append(print_process)
pipeline.append(null_process)
pipeline.append(TimeZeroProcessor())
pipeline.append(print_process)
pipeline.append(SetOriginProcessor())

# Create a container:

container = Coordinates(5, 1, 1, 1, 1, 1, 1)
container2 = Coordinates(7, 2, 2, 2, 2, 2, 2)

# Process first container:

pipeline(container)

# Process second container:

pipeline(container2)
