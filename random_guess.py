# -*- coding: utf-8 -*-
import random


def main():
    old_secret = 999
    while True:
        secret = random.randint(0, 100)
        if secret == old_secret:
            secret = random.randint(1, 100)
#           print "Skrivno število je enako kot prejšnje. Generiram novega...: %s" % secret
#       print "Skrivno število je: %s" % secret
        try:
            guess = int(raw_input("Vpiši številko: "))
            if guess == secret:
                print "Čestitam, uganil si iskano število!"
                try_again = (raw_input("Želiš ponovno igrati? (da/ne) ")).lower()
                if try_again == 'ne':
                    print "Ah, nisi zabaven. Čau."
                    break
            else:
                print "a-a! Nisi uganil! Poskusi ponovno."
        except ValueError:
            print "Napačen vnos. Poskusi vpisati številko..."
        old_secret = secret


if __name__ == "__main__":
    main()
