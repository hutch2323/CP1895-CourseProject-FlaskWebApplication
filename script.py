def main():
    # for i in range(21):
    #     print("self.__player" + str(i+1) + " = player" + str(i+1))

    for i in range(21):
        print("@property")
        print("def player" + str(i+1) + "(self):")
        print("\treturn self.__player" + str(i + 1))
        print()
        print("@player" + str(i + 1) + ".setter")
        print("def player" + str(i + 1) + "(self, player" + str(i+1) + "):")
        print("\tself.__player" + str(i+1) + " = player" + str(i+1))
        print()

if __name__ == "__main__":
    main()