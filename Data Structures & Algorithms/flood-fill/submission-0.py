class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        within = lambda x, y: (x >= 0) and (x < m) and (y >= 0) and (y < n)
        source_color = image[sr][sc]

        def paint(x, y):
            if image[x][y] == color: return

            left, right = x - 1, x + 1
            top, bottom = y - 1, y + 1
            
            image[x][y] = color

            if within(left, y) and image[left][y] == source_color:
                paint(left, y)

            if within(right, y) and image[right][y] == source_color:
                paint(right, y)
            
            if within(x, top) and image[x][top] == source_color:
                paint(x, top)
            
            if within(x, bottom) and image[x][bottom] == source_color:
                paint(x, bottom)

        paint(sr, sc)
        return image