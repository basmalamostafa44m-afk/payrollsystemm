# define function to calculate the bonus
def calculate_bonus(base_salary,performing_rate):
    if performing_rate == 5:
        bonus_percentage = 0.2
    elif performing_rate >= 3:
        bonus_percentage = 0.1
    else :
        bonus_percentage = 0.0
    return bonus_percentage*base_salary
# define function to calculate taxes
def calculate_tax(gross_salary):
    if gross_salary> 7000:
        tax_percentage = 0.15
    elif gross_salary >=3000 :
        tax_percentage = 0.1
    else :
        tax_percentage = 0.0
    return tax_percentage*gross_salary
# core runtime app
def main_hr_app():
    print("======Corporate Payroll System======")
    emp_name = input("Enter employee name: ").strip().capitalize()

    while not emp_name.replace(" ","").isalpha():   # validate name to check if it only contains chars or not
        print("Invalid employee name. Please try again.")
        emp_name = input("Enter employee name: ").strip().capitalize()

    department = input("Enter department name: ").strip().capitalize()

    base_salary = float(input("Enter base salary (EGP): "))
    while base_salary<0:   # validate base salary
        print("Invalid base salary. Please try again.")
        base_salary = float(input("Enter base salary (EGP): "))

    rating = int (input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:   # validate rating
        print("Invalid rating. Please try again.")
        rating = int(input("Enter rating (1-5): "))

    # start functions and calculations
    bonus = calculate_bonus(base_salary,rating)
    gross_salary=bonus+base_salary
    tax = calculate_tax(gross_salary)
    net_salary=gross_salary-tax

    # Outputs
    print("\n"+"="*40)
    print(f"Payroll Statement for: {emp_name} who is working in {department} department")
    print("=" * 40)
    print(f"Base salary:            {base_salary:.2f} EGP")
    print(f"Earned bonus:           {bonus:.2f} EGP")
    print(f"Tax deductions:         {tax:.2f} EGP")
    print("-" * 40)
    print(f"NET PAYABLE CASH:        {net_salary:.2f} EGP")
    print("=" * 40)

# calling main program
main_hr_app()





