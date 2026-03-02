import sys
# membuat tuple
logsApps = ("User1 Login", "User2 Login")
print(logsApps)
print("Memiliki ukuran Tuple", sys.getsizeof(logsApps))

logsApps = ["user1 Login", "User2 Login"]

# buktikan bahwa tuple bersifat immutable / tidak dapat diubah
# menambahkan elemen ke dalam tuple
logsApps.append("user3 Login")
# update elemen tuple
logsApps[0] = "user4 Login"
# menghapus elemen tuple
logsApps.remove("user2 Login")

# pembuktian bahwa tuple bisa diakses dengan index
print(logsApps[0]) #akses index ke-0
print(logsApps[-1]) #akses index ke-1

# Slice dan copy
print(logsApps[0;1])
backup_logsAppS = logsApps[:]
print