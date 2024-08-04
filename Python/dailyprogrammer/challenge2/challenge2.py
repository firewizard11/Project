import math


if __name__ == '__main__':
    user_choice = input("""Which Formula would you like: 
1. Weight
2. Velocity
3. Equations of Motion
4. Momentum
""")
    
    if user_choice == '1': # Weight
        mass: float = float(input('Enter the mass: '))
        gravity: float = float(input('Enter the gravity: '))
        print(f'Weight = {mass * gravity}')
    elif user_choice == '2': # Velocity
        displacement: float = float(input('Enter the displacement: '))
        time: float = float(input('Enter the time: '))
        print(f'Velocity = {displacement / time}')
    elif user_choice == '3': # Equations of motion
        pass
    elif user_choice == '4': # Momentum
        mass: float = float(input('Enter the mass: '))
        velocity: float = float(input('Enter the velocity: '))
        print(f'Momentum = {mass * velocity}')
