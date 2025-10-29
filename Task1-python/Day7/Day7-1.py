import random 
import statistics
from pathlib import Path


def filegenerate(filename,rows,cols):
    base_path = Path(__file__).parent
    file_path = base_path / filename
    with open (file_path,'w') as f:
        for _ in range(rows):
            row=[str(random.randint(0,100)) for _ in range(cols)]
            f.write(','.join(row)+'\n')
    return file_path

def read_column(file_path, col):
    column_data = []
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) > col:
                column_data.append(int(parts[col]))
    return column_data

def compute_stats(data):
    stats = {
        "max": max(data),
        "min": min(data),
        "mean": sum(data) / len(data),
        "median": statistics.median(data)
    }
    return stats

if __name__ == "__main__":
    filename = "data.csv"
    rows, cols = 100, 3
    file_path = filegenerate(filename, rows, cols)
    
    col_index = 2
    column_data = read_column(file_path, col_index)
    
    stats = compute_stats(column_data)
    print(f"Statistics for column {col_index}:")
    print(f"Max: {stats['max']}")
    print(f"Min: {stats['min']}")
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
