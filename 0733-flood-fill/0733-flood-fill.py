class Solution:
    def floodFill(self, image, sr, sc, color):

        start_color = image[sr][sc]

        def flood_fill(x, y):
            if x < 0 or x >= len(image):
                return
            if y < 0 or y >= len(image[0]):
                return

            if image[x][y] == color:
                return

            if image[x][y] != start_color:
                return

            image[x][y] = color

            flood_fill(x - 1, y)  # Up
            flood_fill(x + 1, y)  # Down
            flood_fill(x, y + 1)  # Right
            flood_fill(x, y - 1)  # Left

        flood_fill(sr, sc)

        return image