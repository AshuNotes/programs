def init_env():
    one = "Clean" if int(input("Enter the status of Room 1 (1 Clean / 0 Dirty) : ")) == 1 else "Dirty"
    two = "Clean" if int(input("Enter the status of Room 2 (1 Clean / 0 Dirty) : ")) == 1 else "Dirty"
    return { "room1" : one, "room2" : two }

def suck(env, c_loc):
    if env[c_loc] == "Dirty":
        print(f"sucking the '{c_loc}'")
        env[c_loc] = "Clean"

def sense(env, c_loc):
    return env[c_loc]
    
def is_done(env):
    return all(status == "Clean" for status in env.values())
    
def move(c_loc):
    return "room1" if c_loc == "room2" else "room2"
    
def act(env, c_loc):
    if sense(env, c_loc) == "Dirty":
        suck(env, c_loc)
        return c_loc
    else:
        return move(c_loc)

if __name__ == '__main__':
    env = init_env()
    c_loc = "room1"
    step = 0
    print("\nInitial Environment:", env)
    while not is_done(env):
        print(f"\nStep {step + 1}:")
        c_loc = act(env, c_loc)
        print("Environment State:", env)
        step += 1
    print("\nFinal Environment:", env)