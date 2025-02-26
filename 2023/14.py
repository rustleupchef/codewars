nums = input().split()

holes = int(nums[0])
employees = int(nums[1])
time = int(nums[2])
hours, minutes = int(nums[3].split(":")[0]), int(nums[3].split(":")[1])

if (hours < 11): hours += 12
minutes += (hours * 60) - 660

planted = (minutes // time) * employees
employeesPlanting = holes - planted

if employeesPlanting < 0: employeesPlanting = 0
if employeesPlanting > employees: employeesPlanting = employees

if employeesPlanting == 0:
    print("COFFEE TIME!")
elif employeesPlanting == employees:
    print("Everybody planting trees! More work to do!")
else:
    print(f"{employeesPlanting} people are still planting trees and {employees - employeesPlanting} people have gone for coffee")