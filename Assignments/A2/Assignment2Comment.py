''' 
    COMP 1005/1405 Section A/C/D/E - Assignment two example code commenting for functions.
    Project Details
        Name: Sean Benjamin
        Student #: 100XXXXXXX
        Date: October 15, 2024
    
    External Libraries Used
        None
    
'''


def calcArea(h, w):
    """
    Function Description:
        The purpose of this function is to calculate the area of a rectangle.
    Parameters:
        h (float): height of the rectangle
        w (float): width of the rectangle
    Return:
        float: area of the rectangle 
    """
    area = h * w
    return area
    

# Call the calcArea function and print out the area
print(calcArea(3.9 ,5.2))