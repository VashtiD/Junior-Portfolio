# Vashti Dalchand
# Period 1-2
# 2/27/25
# Python Coding Challenges

# Question 1: Calculate the volume of a sphere

import math  # We import math to use math functions like pi

def sphere_volume(radius):
    # Formula to calculate the volume of a sphere with a given radius
    volume = (4/3) * math.pi * (radius**3)
    return volume  # Return the calculated volume

# Calculate the volume for a sphere with a radius of 5
volume_result = sphere_volume(5)  
# Print the result in a nice format
print(f"1. The volume of a sphere of 5 radius is {volume_result:.3}f")

# Question 2: Calculate the total cost of buying books

def w_cost(copies):
    # Price of a single book before discount
    cover_price = 24.95  
    # The discount percentage
    discount = 0.40  
    # Cost of shipping for the first book
    ship_first = 3  
    # Cost of shipping for each additional book
    ship_after = 0.75  
    
    # Calculate the discounted price of one book
    discount_price = cover_price * (1 - discount)  
    # Total cost of all the books purchased
    total_book_cost = discount_price * copies  
    # Calculate total shipping cost
    shipping_cost = ship_first + (ship_after * (copies - 1))  
    # Add book cost and shipping cost for the grand total
    total = total_book_cost + shipping_cost  
    # Print the final total in a nice format
    print(f"2. Your total is $ {total:.2f}")

# Calculate the total cost for buying 60 copies of the book
w_cost(60)

# Question 3: Calculate what time you will arrive home after a run

def running_time(start_hour, start_minutes):
    # Define easy pace in seconds (8 minutes and 15 seconds)
    easy_pace = 8 * 60 + 15  
    # Define tempo pace in seconds (7 minutes and 12 seconds)
    tempo_pace = 7 * 60 + 12  
    
    # Total running time for the workout in seconds
    total_time_seconds = easy_pace * 2 + (tempo_pace * 3)  
    
    # Convert total running time from seconds to minutes and seconds
    total_minutes = total_time_seconds // 60  
    total_seconds = total_time_seconds % 60  
    
    # Calculate the end time after adding running time to the start time
    end_minutes = total_minutes + start_minutes  
    end_hour = start_hour  
    
    # If the end minutes are 60 or more, we need to carry over to the next hour
    if end_minutes >= 60:
        end_hour += end_minutes // 60  # Add extra hours
        end_minutes = end_minutes % 60  # Keep minutes under 60
    
    # Return the new end hour and minutes
    return end_hour, end_minutes  

# Calculate what time you will arrive home after starting at 6:52 AM
end_hour, end_minutes = running_time(6, 52)  
# Print the arrival time in a nice format
print(f"3. You will arrive at home for breakfast at {end_hour},{end_minutes} AM.")
