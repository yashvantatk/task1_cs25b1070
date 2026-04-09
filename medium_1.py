import numpy as np




def transform_coordinates(obj_coordinates, rover_pos, rover_rot_deg):


   x_deg, y_deg, z_deg = rover_rot_deg


   # Convert degrees to radians
   x = np.radians(x_deg)
   y = np.radians(y_deg)
   z = np.radians(z_deg)


   # Rotation around X-axis
   Rx = np.array([
       [1, 0, 0],
       [0, np.cos(x), -np.sin(x)],
       [0, np.sin(x), np.cos(x)]
   ])


   # Rotation around Y-axis
   Ry = np.array([
       [np.cos(y), 0, np.sin(y)],
       [0, 1, 0],
       [-np.sin(y), 0, np.cos(y)]
   ])


   # Rotation around Z-axis
   Rz = np.array([
       [np.cos(z), -np.sin(z), 0],
       [np.sin(z), np.cos(z), 0],
       [0, 0, 1]
   ])


   #Z * Y * X - Matrice multiplication using @ feature
   R_combined = Rz @ Ry @ Rx


   #Format inputs as numpy vector arrays
   P_coordinates = np.array(obj_coordinates)
   T_rover = np.array(rover_pos)


   # P_world = (R * P_coordinates) + T
   P_rotated = R_combined @ P_coordinates
   P_world = P_rotated + T_rover


   return tuple(np.round(P_world, 3).tolist())


if __name__ == "__main__":
   obj_1 = eval(input("Object coordinates(separated by commas):\t"))
   pos_1 = eval(input("Rover position(separated by commas):\t"))
   rot_1 = eval(input("Rover rotation(in degrees(separated by commas)):\t"))
   world_coords = transform_coordinates(obj_1, pos_1, rot_1)
   print(f"Output: {world_coords}")
