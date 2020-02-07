import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Vring', type=float, help="VRING in RMS")

    args = parser.parse_args()
    Vring = args.Vring

    print('Calculate RTTH & ILR from VRING(RMS)\n')
    print(f'VRING(RMS)  = {Vring:.2f} Vrms\n')
    print(f'RTTH(@3REN) = {(0.54*Vring/2.5):.2f} mA')
    print(f'ILR(@3REN)  = {(1.4*Vring/2.5):.2f} mA\n')
    print(f'RTTH(@5REN) = {(0.54*Vring/1.6):.2f} mA')
    print(f'ILR(@5REN)  = {(1.4*Vring/1.6):.2f} mA')

if __name__ == "__main__":
    main()
