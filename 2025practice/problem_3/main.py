#Problem 3 solution
def main():
    counter = 0
    while True:
        line = input()
        if line == "<TERMINATE>":
            break
        counter += 1
    
    if counter == 1:
        print("Hey, ChatGPT, I need a code!")
    else:
        print(f"Hey, ChatGPT, I need {counter} codes!")

if __name__ == "__main__":
    main()