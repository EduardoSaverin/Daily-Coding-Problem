class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        point = 'N'
        x ,y = 0,0
        for char in instructions:
            if char == 'G':
                x,y = self.move(point, [x,y])
                # print(point, x, y)
            elif char == 'L':
                if point == 'N':
                    point = 'W'
                elif point == 'W':
                    point = 'S'
                elif point == 'S':
                    point = 'E'
                else:
                    point = 'N'
            elif char == 'R':
                if point == 'N':
                    point = 'E'
                elif point == 'E':
                    point = 'S'
                elif point == 'S':
                    point = 'W'
                else:
                    point = 'N'
        # print('Final',point, x, y)
        return True if point != 'N' or (x == 0 and y == 0) else False
                
    def move(self, point, coordinates):
        x,y = coordinates[0], coordinates[1]
        if point == 'N':
            y += 1
        elif point == 'E':
            x += 1
        elif point == 'W':
            x -= 1
        else:
            y -= 1
        return [x,y]