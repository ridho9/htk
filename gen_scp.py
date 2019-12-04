# pwd = "/home/rid9/Project/tugas/speech/tubes"
# pwd = "/home/rid9/Project/tugas/speech/tubes/wav"
pwd = "wav"

filelist = []

with open("filelist", "r") as f:
    for l in f:
        filelist.append(l.strip())

# for i in range(1, 201):
#     print(f"{pwd}/{nim}_{i:03}.wav {pwd}/{nim}_{i:03}.mfc")
#     # print(f"{pwd}/{nim}_{i:03}.wav")

# for f in filelist[:len(filelist)//10]:
for f in filelist[len(filelist)//10:]:
# for f in filelist:
    #  print(f"{pwd}/{f}.wav {pwd}/{f}.mfc")
    print(f"{pwd}/{f}.wav")
