
def virus_count(lPath):
    with open(lPath, 'r') as file:
        lines = file.readlines()

    target_line = [line for line in lines if "Infected files:" in line][-1]
    virus_count = int(target_line.split(":")[-1].strip())
    
    return virus_count
