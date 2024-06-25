import pygame
import math

pygame.init()

# Load car image and scale it
def scale_image(image, scale_percent):
    width = int(image.get_width() * scale_percent / 100)
    height = int(image.get_height() * scale_percent / 100)
    return pygame.transform.scale(image, (width, height))

car_image = pygame.image.load('/Users/mustafa/Desktop/myـthesis/ML_for_Vehicle_Model/vehacle.png')
car_image = scale_image(car_image, 3)  

# Constant based on lidar resolution
LIDAR_RESOLUTION = 240
# Lidar resolution divided by 4 to simplify the visualization
VISUALIZATION_RESOLUTION = 240

def GetDataFromArduino(line):
    data = line[:-3]
    print(data)
    d_list= data.split(",")
    return d_list

def GenerateLinePositions(numberOfLines):
    angle = 360/numberOfLines
    lines = []
    for x in range(numberOfLines):
        lines.append([300 * math.cos((x+1)*angle/180 * math.pi), 300 * math.sin((x+1)*angle/180 * math.pi)])
    return lines

line_positions = GenerateLinePositions(VISUALIZATION_RESOLUTION)

# Set up the drawing window
screen = pygame.display.set_mode([800, 800])

sysfont = pygame.font.get_default_font()
font1 = pygame.font.SysFont(sysfont, 72)

file1 = open('/Users/mustafa/Desktop/myـthesis/ML_for_Vehicle_Model/Dataset/data1.txt', 'r')

Lines = file1.readlines()

for line in Lines:
    distances = GetDataFromArduino(line)
    print(len(distances))
    if(len(distances) == LIDAR_RESOLUTION):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        # Fill the background with white
        screen.fill((250, 250, 250))

        for x in range(VISUALIZATION_RESOLUTION):
            if distances[x] == 0:
                distances[x] = 20
            a = int(float(distances[x]))/2000
            if x in [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 176, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223]:
                pygame.draw.circle(screen, (255,0,0), (line_positions[x][0]*a+400, line_positions[x][1]*a+400), 3)
            else:
                pygame.draw.circle(screen, (0,0,0), (line_positions[x][0]*a+400, line_positions[x][1]*a+400), 2)
        
        # Define car position
        car_rect = car_image.get_rect()
        car_rect.center = (400, 400)

        # Draw car at the center
        screen.blit(car_image, car_rect)
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(500)  #
pygame.quit()
