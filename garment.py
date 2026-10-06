def calculate_production_time(quantity,minutes_per_garment,workers,efficiency):
    total_minutes = quantity * minutes_per_garment
    theoretical_minutes = total_minutes / workers
    actual_minutes = theoretical_minutes / (efficiency / 100)
    actual_hours = actual_minutes / 60
    return actual_hours

print("!!! Garment Production Time Calculator !!!")
quantity = int(input("Enter the quantity of garments to produce: "))
minutes_per_garment = float(input("Enter the minutes required to produce one garment: "))
workers = int(input("Enter the number of workers: "))
efficiency = float(input("Enter the efficiency percentage : "))

production_time = calculate_production_time(quantity, minutes_per_garment, workers, efficiency)
print("\n Estimated production time: " ,round(production_time, 2), "hours")