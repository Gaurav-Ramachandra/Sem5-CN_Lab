import time
import random

NOF_PACKETS = 5

def send_packet(p_size, o_rate):
    while p_size > 0:
        sent = min(p_size, o_rate)
        print(f"Packet of size {sent} Transmitted---", end='')
        p_size -= sent
        print(f"Bytes Remaining to Transmit: {p_size}")
        time.sleep(1)  # Simulate time delay between packets

def main():
    p_sizes = [random.randint(0, 99) for _ in range(NOF_PACKETS)]
    for i, size in enumerate(p_sizes):
        print(f"packet[{i}]:{size} bytes")

    o_rate = int(input("Enter the Output rate: "))
    b_size = int(input("Enter the Bucket Size: "))

    for i, size in enumerate(p_sizes):
        print(f"\nIncoming Packet size: {size}")
        if size > b_size:
            print(f"Incoming packet size ({size}bytes) is Greater than bucket capacity ({b_size}bytes)-PACKET REJECTED")
            continue

        print(f"Bytes remaining to Transmit: {size}")
        send_packet(size, o_rate)

if __name__ == "__main__":
    main()
