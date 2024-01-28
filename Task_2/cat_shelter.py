import sys

def process_log_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Cannot open \"{filename}\"!")
        sys.exit(1)

def analyze_cat_data(lines):
    total_visits, intruder_attacks, total_time = 0, 0, 0
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.split(',')
        if parts[0] == 'OURS':
            total_visits += 1
            entry_time, exit_time = int(parts[1]), int(parts[2])
            visit_length = exit_time - entry_time
            visit_lengths.append(visit_length)
            total_time += visit_length
        elif parts[0] == 'THEIRS':
            intruder_attacks += 1

    return total_visits, intruder_attacks, total_time, visit_lengths

def format_time(minutes):
    return f"{minutes // 60} Hours, {minutes % 60} Minutes"

def main():
    if len(sys.argv) < 2:
        print("Missing command line argument!")
        sys.exit(1)

    lines = process_log_file(sys.argv[1])
    total_visits, intruders, total_time, visit_lengths = analyze_cat_data(lines)

    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {total_visits}")
    print(f"Other Cats: {intruders}\n")
    print(f"Total Time in House: {format_time(total_time)}\n")

    if total_visits > 0:
        avg_visit = sum(visit_lengths) // total_visits
        print(f"Average Visit Length: {avg_visit} Minutes")
        print(f"Longest Visit:        {max(visit_lengths)} Minutes")
        print(f"Shortest Visit:       {min(visit_lengths)} Minutes")
    else:
        print("No visits from the correct cat.")

if __name__ == "__main__":
    main()
