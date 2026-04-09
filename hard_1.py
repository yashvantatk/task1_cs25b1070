import collections
import os


def solve_arena_mission():
   # Creating the mock sample.txt file based on the problem description
   with open("sample.txt", "w") as f:
       f.write("2303\n5102\n3044\n3402")


   obstacles = set()
   print("reading sample.txt for obstacle coordinates...")


   with open("sample.txt", "r") as f:
       for line in f:
           line = line.strip()
           if not line:
               continue


           # Extract N, E, S, W distances digit by digit
           n = int(line[0])
           e = int(line[1])
           s = int(line[2])
           w = int(line[3])


           # Calculate net vector from [0,0]
           x = e - w
           y = n - s
           obstacles.add((x, y))
           print(f"Raw: {line} -> Net Coordinate: ({x}, {y})")


   # The destination is [10, 10], so we need an 11x11 grid
   grid_size = 11


   # Initialize the arena
   arena = [[1 for _ in range(grid_size)] for _ in range(grid_size)]


   # Place the obstacles
   for ox, oy in obstacles:
       # Only place if the obstacle falls within our 11x11 boundary
       if 0 <= ox < grid_size and 0 <= oy < grid_size:
           arena[oy][ox] = 0


   print("\n--- Arena Map (1 = Safe, 0 = Obstacle) ---")
   # Printing from top (y=10) down to bottom (y=0)
   for y in range(grid_size - 1, -1, -1):
       print(arena[y])


   # Shortest Path Calculation
   start = (0, 0)
   destination = (10, 10)


   # Queue stores the path taken so far
   queue = collections.deque([[start]])
   seen = {start}


   shortest_path = None


   while queue:
       current_path = queue.popleft()
       cx, cy = current_path[-1]


       # If we reached the target, save the path and stop searching
       if (cx, cy) == destination:
           shortest_path = current_path
           break


       # Explore 4 directions: North(+y), South(-y), East(+x), West(-x)
       directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


       for dx, dy in directions:
           nx, ny = cx + dx, cy + dy


           # Check if the next move is within bounds, is safe (1), and hasn't been visited
           if 0 <= nx < grid_size and 0 <= ny < grid_size:
               if arena[ny][nx] == 1 and (nx, ny) not in seen:
                   seen.add((nx, ny))
                   queue.append(current_path + [(nx, ny)])


   print("\n--- Mission Report ---")
   if shortest_path:
       print(f"Destination [10, 10] reached successfully!")
       print(f"Total steps required: {len(shortest_path) - 1}")
       print("Path taken (x, y):")
       print(" -> ".join([str(pos) for pos in shortest_path]))
   else:
       print("MISSION FAILED: No valid path to destination due to obstacles.")


if __name__ == "__main__":
   solve_arena_mission()
