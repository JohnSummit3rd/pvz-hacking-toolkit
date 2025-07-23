import pymem

SUN_ADDRESS = 0x29382C50
print(type(pymem.ressources.kernel32.CreateToolhelp32Snapshot))

def set_sun_value(pm, address, new_value):
    pm.write_int(address, new_value)
    print(f"[+] Sun value set to {new_value} at address {hex(address)}")

def main():
    pm = pymem.Pymem("PlantsVsZombies.exe")

    new_sun = int(input("Enter new sun value: "))
    set_sun_value(pm, SUN_ADDRESS, new_sun)

if __name__ == "__main__":
    main()