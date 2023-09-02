# NAMESPACES: Local Scope vs. Global Scope vs. without using Global

# Example 1: Local Scope - Changes the enemies value only inside the function
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"Enemies inside the function: {enemies}")

increase_enemies()
print(f"Enemies outside the function: {enemies}")


# Example 2: Global Scope - Changes the enemies value globally
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside the function: {enemies}")

increase_enemies()
print(f"Enemies outside the function: {enemies}")


# Example 3: Without using Global scope, change the value of enemies "Globally"
enemies = 1
def increase_enemies():
    return enemies + 1
print(f"Enemies: {enemies}")   # Prints the enemies value - no change
enemies = increase_enemies()
print(f"Enemies: {enemies}")   # Prints the enemies value - value changed because of the function and the assignment