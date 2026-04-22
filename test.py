import subprocess
from pathlib import Path
from ucsbcs154lab3_cpu import test


mipsRegs = {
    '$zero': 0, '$at': 1,
    '$v0': 2, '$v1': 3,
    '$a0': 4, '$a1': 5, '$a2': 6, '$a3': 7,
    '$t0': 8, '$t1': 9, '$t2': 10, '$t3': 11,
    '$t4': 12, '$t5': 13, '$t6': 14, '$t7': 15,
    '$s0': 16, '$s1': 17, '$s2': 18, '$s3': 19,
    '$s4': 20, '$s5': 21, '$s6': 22, '$s7': 23,
    '$t8': 24, '$t9': 25,
    '$k0': 26, '$k1': 27,
    '$gp': 28, '$sp': 29, '$fp': 30, '$ra': 31
}


expectedRegisters = {

}

expectedMem = {
     
}


for file in Path("tests").iterdir():
        if file.is_file():
            print(f"Testing : {file}")
            subprocess.run(["bash", "mips_to_hex.sh", str(file), "i_mem_init.txt"], check=True)
            with open(file) as f:
                foundAnswers = False
                for line in f:
                     if "# ANSWER" not in line and not foundAnswers:
                          continue
                     elif "# ANSWER" in line and not foundAnswers:
                        foundAnswers = True
                     eq = line.find("=") - 1
                     if line[2] == "$":
                        expectedRegisters[mipsRegs[line[2:eq]]] = int(line[eq+3:])
                     elif line[2] == "m":
                        expectedMem[int(line[line.find("[")+1: line.find("]")])] = int(line[eq+3:line.find('\t', eq+3)])
                if not foundAnswers: print(f"Didn't find answers section in {file}")
                dmem, rf = test()
                if len(expectedRegisters) > 0:
                    for regNum, val in rf.items():
                        assert expectedRegisters[regNum] == val, f"Failed reg {regNum} in {file}. Expected value: {expectedRegisters[regNum]}, got value {val}"

                if len(expectedMem) > 0:
                    for memAddr, val in dmem.items():
                        assert expectedMem[memAddr] == val, f"Failed mem {memAddr} in {file}. Expected value: {expectedMem[memAddr]}, got value {val}" 
                expectedRegisters = {

                }

                expectedMem = {
                    
                }


print("Passed all tests!")
