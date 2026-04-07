"""
Problem: Walking Robot Simulation

A robot starts at position (0, 0) on an infinite 2D grid, facing north.

You are given:
- An array of integers `commands`, where:
    - -2 means turn left 90 degrees
    - -1 means turn right 90 degrees
    - 1 <= x <= 9 means move forward x units
- A list of obstacles, where each obstacle is given as [x, y]

Rules:
- The robot moves one step at a time.
- If the robot encounters an obstacle, it stops moving forward for that command
  (but continues processing the next command).
- The robot cannot move onto a cell with an obstacle.

Return:
- The maximum Euclidean distance squared from the origin (0, 0) that the robot
  reaches at any point during its movement.

Example:
Input: commands = [4, -1, 3], obstacles = []
Output: 25
Explanation: Robot moves to (3, 4), distance squared = 3^2 + 4^2 = 25

Constraints:
- 1 <= commands.length <= 10^4
- -2 <= commands[i] <= 9
- 0 <= obstacles.length <= 10^4
- -3 * 10^4 <= xi, yi <= 3 * 10^4
"""

class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = (
            60013  # Slightly larger than 2 * max coordinate value
        )

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Store obstacles in a set for efficient lookup
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        # Define direction vectors: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0  # 0: North, 1: East, 2: South, 3: West

        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:  # Turn left
                current_direction = (current_direction + 3) % 4
                continue

            # Move forward
            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y

            max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared

    # Hash function to convert (x, y) coordinates to a unique integer value
    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.HASH_MULTIPLIER * y
    
# ------------------ TEST CASES ------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Basic movement
        {
            "commands": [4, -1, 3],
            "obstacles": [],
            "expected": 25,
            "desc": "Simple move and turn"
        },
        # With obstacle blocking
        {
            "commands": [4, -1, 4, -2, 4],
            "obstacles": [[2, 4]],
            "expected": 65,
            "desc": "Obstacle blocks path"
        },
        # Only turns, no movement
        {
            "commands": [-1, -1, -1, -1],
            "obstacles": [],
            "expected": 0,
            "desc": "Only turning"
        },
        # Move in square
        {
            "commands": [1, -1, 1, -1, 1, -1, 1],
            "obstacles": [],
            "expected": 2,
            "desc": "Square path"
        },
        # Immediate obstacle
        {
            "commands": [5],
            "obstacles": [[0, 1]],
            "expected": 0,
            "desc": "Blocked immediately"
        },
        # Large movement no obstacles
        {
            "commands": [9, 9, 9, 9],
            "obstacles": [],
            "expected": 324,
            "desc": "Straight line north"
        },
    ]

    for i, test in enumerate(tests):
        result = sol.robotSim(test["commands"], test["obstacles"])
        print(f"Test {i+1}: {test['desc']}")
        print(f"Expected: {test['expected']}, Got: {result}")
        print("PASS" if result == test["expected"] else "FAIL")
        print("-" * 40)