import pymem

STATIC_SUN_BASE = 0x731C50
SUN_OFFSETS = [0x868, 0x5578]

def resolve_pointer_chain(pm, base, offsets):
    addr = pm.read_int(base)
    for offset in offsets[:-1]:
        addr = pm.read_int(addr + offset)
    addr += offsets[-1]
    return addr

def patch_cooldowns(pm):
    code_address = pm.base_address + 0x958C5
    pm.write_bytes(code_address, b'\x90\x90', 2)
    print(f"[+] Cooldowns disabled (patched at {hex(code_address)})")

def restore_cooldowns(pm):
    code_address = pm.base_address + 0x958C5
    pm.write_bytes(code_address, b'\x7E\x14', 2)
    print(f"[+] Cooldowns restored (original bytes at {hex(code_address)})")

def sun_editor(pm):
    sun_address = resolve_pointer_chain(pm, STATIC_SUN_BASE, SUN_OFFSETS)
    sun_value = int(input("Enter new sun value between 0-9999: "))
    pm.write_int(sun_address, sun_value)

    print(f"[+] Sun value set to {sun_value} at {hex(sun_address)}")

def cooldown_menu(pm):
    while True:
        print("""
            ======================
               Cooldown Options
            ======================

            1. Disable Cooldowns
            2. Restore Cooldowns
            0. Return to Main Menu
        """)
        cd_choice = input("Select an option: ")
        
        if cd_choice == '1':
            patch_cooldowns(pm)
        elif cd_choice == '2':
            restore_cooldowns(pm)
        elif cd_choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input, please try again.")

def one_hit_kill_menu(pm):
    while True:
        print("""
            ======================
             One Hit Kill Options
            ======================

            1. Enable One Hit Kill
            2. Disable One Hit Kill
            0. Return to Main Menu
        """)

        oh_choice = input("Select an option: ")

        if oh_choice == '1':
            one_hit_kill(pm)
        elif oh_choice == '2':
            one_hit_kill_disabler(pm)
        elif oh_choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input, please try again.")

def one_hit_kill(pm):
    base = pm.base_address
    
    pm.write_bytes(base + 0x145DF1, b'\x29\xED\x90\x90', 4)
    pm.write_bytes(base + 0x142223, b'\xEB\x08', 2)
    pm.write_bytes(base + 0x142214, b'\x90\x90', 2)

    print("[+] 1-Hit Kill Patch Applied Successfully.")

def one_hit_kill_disabler(pm):
    base = pm.base_address
    
    pm.write_bytes(base + 0x145DF1, b'\x89\x6C\x24\x18', 4)
    pm.write_bytes(base + 0x142223, b'\x8B\x0D\xAC\xF4\x72\x00', 6)
    pm.write_bytes(base + 0x142214, b'\x03\xCA', 2)
    pm.write_bytes(base + 0x7169B, b'\x5C', 1)

    print("[+] 1-Hit Kill Patch Disabled.")

def infinite_plant_health_menu(pm):
    while True:
        print("""
            ===============================
             Infinite Plant Health Options
            ===============================

            1. Enable Infinite Plant Health
            2. Disable Infinite Plant Health
            0. Return to Main Menu
        """)

        ip_choice = input("Select an option: ")

        if ip_choice == '1':
            infinite_plant_health(pm)
        elif ip_choice == '2':
            infinite_plant_health_disabler(pm)
        elif ip_choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input, please try again.")

def infinite_plant_health(pm):
    base = pm.base_address

    pm.write_bytes(base + 0x1447A0, b'\x90', 1)
    print("[+] Infinite Plant Health Applied Successfully.")

def infinite_plant_health_disabler(pm):
    base = pm.base_address

    pm.write_bytes(base + 0x1447A0, b'\x83\x46\x40\xFC', 4)
    print("[+] Infinite Plant Health Disabled.")


def main():
    pm = pymem.Pymem("popcapgame1.exe")

    while True:
        print("""
        ============================================
         Welcome to the PvZ Python Toolbox by Aaron
        ============================================

        This toolkit includes multiple memory editing tools for
        Plants vs. Zombies GOTY (2009)

        Available features:
        1. Modify Sun Level
        2. Disable Plant Cooldowns
        3. Activate 1-Hit Kill (ASM Patchs)
        4. Activate Infinite Plant Health
        5. Exit

        For educational and personal use only.
        Please ensure PvZ is running before using any tools.

        Select a tool from the menu to begin.
        """)

        choice = input("Enter the number of the tool you'd like to use: ")

        if choice == "1":
            print(">> Opening Sun Level Editor...")
            sun_editor(pm)
        
        elif choice == "2":
            print(">> Launching Cooldown Disabler...")
            cooldown_menu(pm)
        
        elif choice == "3":
            print(">> Applying 1-Hit Kill Patch...")
            one_hit_kill_menu(pm)

        elif choice == "4":
            print(">> Applying Infinite Plant Health...")
            infinite_plant_health_menu(pm)

if __name__ == "__main__":
    main()
