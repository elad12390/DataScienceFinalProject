from svgtrace import trace
def main():
    with open("./test.svg", "w") as colour:
        colour.write(trace("./test.png"))
        colour.close()

main()