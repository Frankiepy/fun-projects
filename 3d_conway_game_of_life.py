# Import necessary libraries for Panda3D and time
from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeomNode, GeomVertexData, Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import GeomVertexFormat, LVector3, Point3, Material
from panda3d.core import NodePath
import time

# Create a custom application class that inherits from ShowBase
class MyApp(ShowBase):

    def __init__(self):
        super().__init__()

        # Dictionary to store the location and references to cubes (3D cells in the grid)
        self.cube_locs = {}

        # Call the add_lighting function to set up lighting for the scene
        self.add_lighting()

        # Prepare the scene with some initial settings
        self.prep()

        # Wait for 1 second before starting the application
        time.sleep(1)

        # Start the main application loop
        self.run_app()

        # Uncomment the next line to create a grid of cubes (currently not used)
        # cube_list = [[ [self.make_cube(x,y,z) for x in range(-5,5)] for y in range(20,30)] for z in range(-5,5)]

    def make_cube(self, x, y, z):
        """
        Creates a cube at the specified (x, y, z) position in the 3D scene.
        """
        cube = self.loader.loadModel("models/box")  # Load the cube model from Panda3D
        cube.reparentTo(self.render)  # Attach the cube to the scene's render node (this makes it visible)
        cube.setPos(x * 2, y * 2, z * 2)  # Set the cube's position in 3D space
        self.cube_locs[(x, y, z)] = cube  # Save the cube's location in the cube_locs dictionary
        return cube

    def add_lighting(self):
        """
        Adds basic lighting to the scene, including ambient and directional lights.
        """
        from panda3d.core import AmbientLight, DirectionalLight

        # Create an ambient light with a soft color
        ambient_light = AmbientLight("ambient_light")
        ambient_light.set_color((0.5, 0.5, 0.5, 1))  # Set the ambient light's color
        self.render.set_light(self.render.attach_new_node(ambient_light))  # Attach it to the scene

        # Create a directional light (similar to sunlight)
        directional_light = DirectionalLight("directional_light")
        directional_light.set_color((0.8, 0.8, 0.8, 1))  # Set the directional light's color
        directional_light_nodepath = self.render.attach_new_node(directional_light)
        directional_light_nodepath.set_hpr(0, -60, 0)  # Set the direction of the light
        self.render.set_light(directional_light_nodepath)  # Attach it to the scene

    def cubes_around(self, x, y, z):
        """
        Checks the cubes around a given (x, y, z) location.
        Returns the count of neighboring cubes and the list of empty neighboring coordinates.
        """
        cubes_around = 0  # Counter for neighboring cubes
        empty_coords = []  # List to store coordinates of empty neighboring spaces

        # Loop over each of the 26 possible neighbors in a 3x3x3 grid (including the current cube)
        for i in range(-1, 2):  # Looping over -1, 0, and 1
            for j in range(-1, 2):
                for k in range(-1, 2):
                    # Check if the neighbor is a cube (cube_locs stores all active cubes)
                    if (x + i, y + j, z + k) in self.cube_locs and (i, j, k) != (0, 0, 0):
                        cubes_around += 1  # Increment count of neighboring cubes
                    elif (x + i, y + j, z + k) not in self.cube_locs:
                        empty_coords.append((x + i, y + j, z + k))  # Add empty neighbor's coordinate to the list

        # Return the count of neighboring cubes and the list of empty coordinates
        return cubes_around, empty_coords

    def run_app(self):
        """
        Sets up the app to run continuously, updating the scene with each frame.
        """
        # Add the update method to the task manager to run repeatedly
        self.taskMgr.add(self.update, "update_task")

    def update(self, task):
        """
        The update function is called repeatedly to advance the simulation.
        It calculates the next state of the cells (cubes) based on the Game of Life rules.
        """
        # Ensure lighting and anti-aliasing settings are applied each time
        self.add_lighting()
        self.render.set_antialias(True)

        # Set the camera's position and view
        self.camera.set_pos(10, -40, 20)
        self.camera.look_at(0, 25, 0)

        # Make an initial cube at a given location
        self.make_cube(4, 3, 3)

        # Make a copy of the cube_locs dictionary for processing
        temp_cube_locs = self.cube_locs.copy()
        around_spots = {}  # Dictionary to track empty spots around cubes

        # Process each cube in the current configuration
        for x, y, z in temp_cube_locs:
            # Get the count of surrounding cubes and the list of empty neighboring coordinates
            cubes_around, empty_coords = self.cubes_around(x, y, z)

            # For each empty neighboring coordinate, increment its counter in around_spots
            for coord in empty_coords:
                if coord not in around_spots:
                    around_spots[coord] = 1
                else:
                    around_spots[coord] += 1

            # Apply Conway's Game of Life rules: 
            # If the cube has less than 2 or more than 3 neighbors, it dies (is removed)
            if cubes_around <= 1 or cubes_around > 3:
                self.cube_locs[(x, y, z)].removeNode()  # Remove the cube from the scene
                del self.cube_locs[(x, y, z)]  # Remove it from the cube_locs dictionary

        # Check the empty spots around cubes for potential births
        for x, y, z in around_spots:
            # A new cube is born if exactly 3 neighboring cubes are alive
            if around_spots[(x, y, z)] == 3:
                self.make_cube(x, y, z)  # Create a new cube at the empty spot

        # Pause briefly to control the speed of the simulation
        time.sleep(.5)

        # Continue updating the simulation
        return task.cont

    def prep(self):
        """
        Prepares the initial setup for the Game of Life by asking the user to input coordinates
        for the initial active cubes.
        """
        # Ask the user to input coordinates for active cubes (x, y, z)
        while True:
            read = map(int, input("Type in an x,y,z coordinate to add a cube or hit enter to start the simulation: ").split(','))
            try:
                # Get input from the user and split it into x, y, z
                x, y, z = read
                # Create a cube at the specified coordinates
                self.make_cube(x-5, y+20, z-5)
            except Exception:
                if read == "":
                    break  # Break the loop if the user provides invalid input
                else:
                    print('invalid input')
        print("out")

# Create an instance of the MyApp class and run the app
app = MyApp()
app.run()


#Type in point x,y,z: 5,5,5
#Type in point x,y,z: 4,5,5
#Type in point x,y,z: 4,3,3
#Type in point x,y,z: 5,4,5
