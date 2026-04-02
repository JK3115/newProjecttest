
def load_log(filepath):
    lines=[]
    with open(filepath,"r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def extract_ip(line):
    ip = line.split()[2]
    return ip

def count_ips(lines):
    ip_counts = {}
    for line in lines:
        ip = extract_ip(line)
        if ip not in ip_counts:
            ip_counts[ip] = 1 
        else:
            ip_counts[ip] += 1
    return ip_counts

def get_top_ips(ip_counts,n):
     sorted_ips=sorted(ip_counts, key=lambda x: ip_counts[x], reverse=True)
     return sorted_ips[:n]

def print_results(top_ips,ip_counts):
    for ip in top_ips:
        print(f"{ip} - {ip_counts[ip]}")

def main():
    get_lines= load_log("access.log")
    ip_count= count_ips(get_lines)
    max_ips = get_top_ips(ip_count,3)
    print_results(max_ips,ip_count)
if __name__ == "__main__":
    main()