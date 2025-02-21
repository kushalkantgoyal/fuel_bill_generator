import calendar
import math
import random

from app.receipt_generator import generate_fuel_bill_with_logo_png


def generate_random_day(year, month, from_date, to_date=None):
    if not to_date:
        num_days = calendar.monthrange(year, month)[1]
    else:
        num_days = to_date

    # Generate a random day within the valid range
    return random.randint(from_date, num_days)


# Example usage:

def generate_body(YEAR=2024, START_MONTH=1, END_MONTH=12, VEHICLE_NO="RJ14UE5201", OUTPUT_PATH="fuel_bills",
                  RECEIPT_NO_START=573992422, product_name='DIESEL', title_line_1="Welcome To BPCL",
                  title_line_2="SHARMA BROTHERS", title_line_3="TONK ROAD JAIPUR",
                  month_to_opening_highest_closing_price: dict = None):

    if month_to_opening_highest_closing_price is None:
        month_to_opening_highest_closing_price = {
            2024: {
                1: [90.04, 91.94, 89.88],
                2: [89.88, 91.94, 90.04],
                3: [90.04, 91.94, 89.88],
                4: [89.88, 91.94, 90.04],
                5: [90.04, 91.94, 89.88],
                6: [89.88, 91.94, 90.04],
                7: [90.04, 91.94, 89.88],
                8: [89.88, 91.94, 90.04],
                9: [90.04, 91.94, 89.88],
                10: [89.88, 91.94, 90.04],
                11: [90.04, 91.94, 89.88],
                12: [89.88, 91.94, 90.04]
            }
        }

    logo_path = "resources/BPCL_logo.jpeg"

    receipt_no = random.randint(RECEIPT_NO_START, 10 ** (math.floor(math.log10(abs(RECEIPT_NO_START))) + 1) - 1)

    for month in range(START_MONTH, END_MONTH + 1):
        random_day1 = generate_random_day(year=YEAR, month=month, from_date=1, to_date=9)
        random_date1 = f"{YEAR:04d}-{month:02d}-{random_day1:02d}"

        random_day2 = generate_random_day(year=2024, month=month, from_date=random_day1 + 7, to_date=19)
        random_date2 = f"{YEAR:04d}-{month:02d}-{random_day2:02d}"

        random_day3 = generate_random_day(year=2024, month=month, from_date=random_day2 + 9)
        random_date3 = f"{YEAR:04d}-{month:02d}-{random_day3:02d}"

        dates = [random_date1, random_date2, random_date3]
        i = 0
        for dt in dates:
            generate_fuel_bill_with_logo_png(
                output_path=OUTPUT_PATH,
                logo_path=logo_path,
                date=dt,
                time=f"{random.randint(7, 21):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}",
                fuel_rate=month_to_opening_highest_closing_price[YEAR][month][i],
                volume=random.randint(22, 33),
                vehicle_no=VEHICLE_NO,
                mode="Cash",
                product=product_name,
                receipt_no=receipt_no,
                title_line_1=title_line_1,
                title_line_2=title_line_2,
                title_line_3=title_line_3
            )
            i += 1
            receipt_no = random.randint(receipt_no, receipt_no + random.randint(90003, 300000))



month_to_diesel_rajasthan_opening_highest_closing_price: dict = {
    2024: {
        1: [90.04, 91.94, 89.88],
        2: [89.88, 91.94, 90.04],
        3: [90.04, 91.94, 89.88],
        4: [89.88, 91.94, 90.04],
        5: [90.04, 91.94, 89.88],
        6: [89.88, 91.94, 90.04],
        7: [90.04, 91.94, 89.88],
        8: [89.88, 91.94, 90.04],
        9: [90.04, 91.94, 89.88],
        10: [89.88, 91.94, 90.04],
        11: [90.04, 91.94, 89.88],
        12: [89.88, 91.94, 90.04]
    },
    2025: {
        1: [90.80, 90.80, 90.80],
        2: [90.80, 90.19, 90.80]
    }
}
generate_body(YEAR=2025, START_MONTH=1, END_MONTH=2, VEHICLE_NO="RJ14UE5201", OUTPUT_PATH="/tmp/fuel_bills",
              RECEIPT_NO_START=573992422, product_name='DIESEL', title_line_1="Welcome To BPCL",
              title_line_2="SHARMA BROTHERS", title_line_3="TONK ROAD JAIPUR",
              month_to_opening_highest_closing_price=month_to_diesel_rajasthan_opening_highest_closing_price)
