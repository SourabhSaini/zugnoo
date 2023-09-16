import noise


def map_noise_to_color(value):
    color_value = int((value + 1.0) / 2.0 * 255) 
        return (color_value, color_value, color_value) 

# Main function to show Perlin noise on LED panel 
def main(): 
    try: 
        while True: 
            # Generate Perlin noise grid 
                scale = 0.2 
                octaves = 6 
                persistence = 0.5 
                lacunarity = 2.0 
                grid = [] 
                for y in range(64): 
                    row = [] 
                    for x in range(64): 
                        n = noise.pnoise2(
                                x * scale, 
                                y * scale, 
                                octaves=octaves, 
                                persistence=persistence, 
                                lacunarity=lacunarity)
                        row.append(n) 
                    grid.append(row)

                # Map Perlin noise values to colors and display on LED matrix
                for y in range(64):
                    for x in range(64):
                        color = map_noise_to_color(grid[y][x])
                        matrix.SetPixel(x, y, *color)
                time.sleep(0.05)  # Adjust the sleep time for display speed                                          
