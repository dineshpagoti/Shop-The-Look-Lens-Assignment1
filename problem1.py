print("Become the programmer you're meant to be!")
class WhiteBox:
    def __init__(self, top, left, height, width):
        self.top = top
        self.left = left
        self.height = height
        self.width = width

def find_white_box(matrix):
    height = len(matrix)
    if height == 0:
        return None
    
    width = len(matrix[0])
    if width == 0:
        return None
    
    # Initialize variables to track the white box
    top_left_x = -1
    top_left_y = -1
    box_width = 0
    box_height = 0
    
    # Finding the top-left corner
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 'w':
                top_left_x = j
                top_left_y = i
                break
        if top_left_x != -1:
            break
    
    # If no white box found
    if top_left_x == -1:
        return None
    
    # Determining width
    for j in range(top_left_x, width):
        if matrix[top_left_y][j] == 'w':
            box_width += 1
        else:
            break
    
    # Determining height
    for i in range(top_left_y, height):
        if matrix[i][top_left_x] == 'w':
            box_height += 1
        else:
            break
    
    return WhiteBox(top=top_left_y, left=top_left_x, height=box_height, width=box_width)

def get_matrix():
    rows = int(input())
    cols = int(input())
    
    matrix = []
    for _ in range(rows):
        row = input().strip().split()[:cols]
        matrix.append(row)
    
    return matrix

# Get input matrix
matrix = get_matrix()

# Find white box
white_box_info = find_white_box(matrix)

if white_box_info:
    white_box_object = {
        'top': white_box_info.top,
        'left': white_box_info.left,
        'height': white_box_info.height,
        'width': white_box_info.width
    }
    print("White box information:")
    print(white_box_object)
else:
    print("No white box found.")
