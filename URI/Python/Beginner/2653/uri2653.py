if __name__ == "__main__":
    gems = []
    while True:
        try:
            gems.append(input())
        except EOFError:
            print(len(set(gems)))
            break
