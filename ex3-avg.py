"""
Some other ways to do this:
len(list(company_dict)) - con is it takes up O(N) memory
Use generator functions instead and return a count that gets incremented each iteration PLUS the
"""


def generate_company_dicts():
    file_name = "techcrunch.csv"
    lines = (line for line in open(file_name))
    list_line = (s.rstrip().split(",") for s in lines)
    cols = next(list_line)
    company_dicts = (dict(zip(cols, data)) for data in list_line)
    return company_dicts


def main():
    company_dicts = generate_company_dicts()
    funding = (
        int(company_dict["raisedAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )
    total_series_a = sum(funding)
    company_dicts = generate_company_dicts()
    series_a_companies = (sum(1 for x in company_dicts))
    avg_raised = round(total_series_a / series_a_companies, 2)
    print(f"${total_series_a} raised by {series_a_companies} companies, for an average of ${avg_raised} "
          f"raised per company")


if __name__ == "__main__":
    main()