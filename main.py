
def tell_me_a_joke():
# this is comment
    """
    We are only returning a joke here, but in a real application, this function could be more complex,
    """
    return "Why don't scientists trust atoms? Because they make up everything!"

def main():
    joke = tell_me_a_joke()
    print(joke) 
        

if __name__ == "__main__": 
    # to know this file only runs when we execute it directly, and not when we import it as a module in another file.
    main()
