def tower_of_hanoi(number_of_disks, from_rod, to_rod, aux_rod):
    global c
    c += 1
    if number_of_disks == 1:
        print("Moved from", from_rod, "to", to_rod)
        return
    tower_of_hanoi(number_of_disks - 1, from_rod, aux_rod, to_rod)
    print("Moved from", from_rod, "to", to_rod)
    tower_of_hanoi(number_of_disks - 1, aux_rod, to_rod, from_rod)


n = 4
c = 0
tower_of_hanoi(n, 'A', 'C', 'B')
print(c)
