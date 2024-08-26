import tkinter as tk
import math
import time
from PIL import Image

# Define the path for the blank icon
icon_path = 'C:\\Users\\Frank\\Desktop\\blank.ico'

# Create a blank (transparent) ICO file if it doesn't exist
def create_blank_ico(path):
    size = (16, 16)  # Size of the icon
    image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent image
    image.save(path, format="ICO")

# Create the blank ICO file
create_blank_ico(icon_path)

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title('')
        self.root.iconbitmap(icon_path)  # Set the custom icon
        self.canvas = tk.Canvas(self.root, width=150, height=150, bg='white')
        self.canvas.pack()
        self.center_x = 75
        self.center_y = 75
        self.clock_radius = 56.25
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        # Draw the clock face without a border
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                fill='lightgrey', outline='lightgrey')

        # Draw the hour marks
        for i in range(12):
            angle = math.radians(i * 30)
            x = self.center_x + self.clock_radius * 0.85 * math.sin(angle)
            y = self.center_y - self.clock_radius * 0.85 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i if i != 0 else 12), font=('Arial', 6, 'bold'))

    def update_clock(self):
        self.canvas.delete('hands')  # Remove old hands

        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Draw the hour hand
        hour_angle = math.radians((hours + minutes / 60) * 30)
        hour_hand_length = self.clock_radius * 0.5
        hour_x = self.center_x + hour_hand_length * math.sin(hour_angle)
        hour_y = self.center_y - hour_hand_length * math.cos(hour_angle)
        self.canvas.create_line(self.center_x, self.center_y, hour_x, hour_y, width=2.25, fill='black', tags='hands')

        # Draw the minute hand
        minute_angle = math.radians((minutes + seconds / 60) * 6)
        minute_hand_length = self.clock_radius * 0.75
        minute_x = self.center_x + minute_hand_length * math.sin(minute_angle)
        minute_y = self.center_y - minute_hand_length * math.cos(minute_angle)
        self.canvas.create_line(self.center_x, self.center_y, minute_x, minute_y, width=1.5, fill='black', tags='hands')

        # Draw the second hand
        second_angle = math.radians(seconds * 6)
        second_hand_length = self.clock_radius * 0.9
        second_x = self.center_x + second_hand_length * math.sin(second_angle)
        second_y = self.center_y - second_hand_length * math.cos(second_angle)
        self.canvas.create_line(self.center_x, self.center_y, second_x, second_y, width=0.75, fill='red', tags='hands')

        self.root.after(1000, self.update_clock)  # Update every second

root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
