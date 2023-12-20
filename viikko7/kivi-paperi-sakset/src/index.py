from luo_peli import luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in ["a", "b", "c"]:
            luo_peli(vastaus)
        else:
            break


if __name__ == "__main__":
    main()
