"""
Components for holding drone data.

In this case, a 'container' is a class that holds data on a specific state.
These containers are usually constructed using incoming data,
which are then used elsewhere in the model for computations.
"""


class BaseContainer:
    """
    BaseContainer - Base class for containers.

    This class contains some common functionality that all containers should have.
    As of now, all containers must have a time associated with them.
    We represent time in MS since the boot, which will not align with 'wall time'.
    We provide some functionality for converting between the two,
    and converting to other time formats.
    """

    def __init__(self, time: int) -> None:

        self.time: int = time  # Time since boot in milliseconds

    def __str__(self) -> str:
        return f"Time: {self.time}"


class PrincipalAxes(BaseContainer):
    """
    PrincipalAxes - Container for principal axes data.
    
    This class holds the data representing the principal axes of the relevant object:

     - pitch - Pitch angle in radians.
     - roll - Roll angle in radians.
     - yaw - Yaw angle in radians.

    This class also contains the velocity of each axis:

     - vpitch - Pitch velocity in radians per second.
     - vroll - Roll velocity in radians per second.
     - vyaw - Yaw velocity in radians per second.
    """

    def __init__(self, time: int, pitch: float, roll: float, yaw: float, vpitch: float, vroll: float, vyaw: float) -> None:

        super().__init__(time)

        # Axes angles:

        self.pitch: float = pitch
        self.roll: float = roll
        self.yaw: float = yaw

        # Axes velocities:

        self.vpitch: float = vpitch
        self.vroll: float = vroll
        self.vyaw: float = vyaw

    def __str__(self) -> str:
        return super().__str__() + f", Pitch: {self.pitch}, Roll: {self.roll}, Yaw: {self.yaw}"


class Coordinates(BaseContainer):
    """
    PositionCord - Container for coordinate position data.

    This class holds the data representing the GPS coordinates of the relevant object:

     - lat - Latitude in degrees.
     - long - Longitude in degrees.
     - alt - Altitude in meters.

    This class also contains the velocity of each axis:

     - vx - Velocity in X axis in meters per second.
     - vy - Velocity in Y axis in meters per second.
     - vz - Velocity in Z axis in meters per second.

    TODO:
    Add relative altitude, if that is useful
    """

    def __init__(self, time: int, lat: float, long: float, alt: float, vlat: float, vlong: float, valt: float) -> None:

        super().__init__(time)

        # Position coordinates:

        self.lat = lat
        self.long = long
        self.alt = alt

        # Position velocities:

        self.vlat = vlat
        self.vlong = vlong
        self.valt = valt

    def __str__(self) -> str:
        return super().__str__() + f", Lat: {self.lat}, Long: {self.long}, Alt: {self.alt}"


class Position(BaseContainer):
    """
    Position - Container for position data.

    This class holds the data representing the position of the relevant object.
    The position in represented in meters relative to the reference location.
    Usually, this reference location is the position of the observer.

     - x - X position in meters.
     - y - Y position in meters.
     - z - Z position in meters.

    This class also contains the velocity of each axis:

     - vx - Velocity in X axis in meters per second.
     - vy - Velocity in Y axis in meters per second.
     - vz - Velocity in Z axis in meters per second.

    This container is probably the one we will be using for our operations?
    """

    def __init__(self, time: int, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> None:

        super().__init__(time)

        # Position coordinates:

        self.x = x
        self.y = y
        self.z = z

        # Position velocities:

        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self) -> str:
        return super().__str__() + f", X: {self.x}, Y: {self.y}, Z: {self.z}"
