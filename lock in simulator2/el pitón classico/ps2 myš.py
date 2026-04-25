# Formát: [Byte1, Byte2(X), Byte3(Y), Byte4(Wheel/ExtraButtons)]
# Byte1: [?|?|Y_sign|X_sign|1|Middle|Right|Left]
# Byte4: [0|0|Back|Forward|W|W|W|W]

packets = [
    # 1. Rýchly pohyb doprava hore (X=+20, Y=+20), žiadne tlačidlá
    [0x08, 0x14, 0x14, 0x00],
    
    # 2. Scrollovanie kolieskom nadol (-1) počas pohybu
    # Koliesko -1 v 4-bitovom dvojkovom doplnku je 0xF (1111)
    [0x08, 0x05, 0x05, 0x0F],
    
    # 3. Kliknutie bočným tlačidlom "Forward" (štvrtý byte, bit 4)
    [0x08, 0x00, 0x00, 0x10],
    
    # 4. Stlačenie PRAVÉHO tlačidla (Byte1, bit 1) a pohyb doľava (X=-10)
    # X_sign (bit 4) = 1, Byte 1 = 0x1A (00011010), Byte 2 = 0xF6 (-10)
    [0x1A, 0xF6, 0x00, 0x00],
    
    # 5. Uvoľnenie pravého tlačidla a kliknutie STREDNÝM tlačidlom (Byte1, bit 2)
    [0x0C, 0x00, 0x00, 0x00],
    
    # 6. Pohyb nadol (Y=-30) so stlačeným ĽAVÝM tlačidlom (Drag)
    # Y_sign (bit 5) = 1, Byte 1 = 0x29 (00101001), Byte 3 = 0xE2 (-30)
    [0x29, 0x00, 0xE2, 0x00]
]

x = 0
y = 0
wheel = 0

def printPackets(packets):
    global x, y, wheel

    

    for i in packets:
        left = "-"
        right = "-"
        middle = "-"
        forward = "-"
        back = "-"


        if (i[0] & 0x10) >> 4 == 1:
            x -= int(i[1])
        elif (i[0] & 0x10) >> 4 == 0:
            x += int(i[1])

        if (i[0] & 0x20) >> 5 == 1:
            y -= int(i[2])
        elif (i[0] & 0x20) >> 5 == 0:
            y += int(i[2])
        
        if i[0] & 0x01 == 1:
            left = "L"
        if (i[0] & 0x02) >> 1 == 1:
            right = "R"
        if (i[0] & 0x04) >> 2 == 1:
            middle = "M"

        if (i[3] & 0x10) >> 4 == 1:
            forward = "F"
        if (i[3] & 0x20) >> 5 == 1:
            back = "B"


        wheel += int(i[3] & 0x0F)
        

        print(f"X = {x}, Y = {y}, Wheel = {wheel}, Buttons = {left}{middle}{right}, {forward}{back}")



printPackets(packets)