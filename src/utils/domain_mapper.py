DOMAIN_MAP = {
    "information-technology": "IT",
    "engineering": "Software Development",
    "digital-media": "Marketing",
    "public-relations": "Marketing",
    "sales": "Sales",
    "accountant": "Finance",
    "banking": "Finance",
    "finance": "Finance",
    "hr": "HR",
    "designer": "Design",
    "business-development": "Sales",
    "consultant": "Operations",
    "aviation": "Operations",
    "construction": "Operations",
    "healthcare": "Operations",
    "agriculture": "Operations",
    "automobile": "Operations",
    "bpo": "Operations",
    "arts": "Design",
    "apparel": "Design",

    "data scientist": "Data Science",
    "data science": "Data Science",
    "machine learning engineer": "Data Science",
    "data analyst": "Data Science",
    "software engineer": "IT",
    "web developer": "IT",
    "marketing": "Marketing",
    "digital marketing": "Marketing",
    "operations": "Operations"
}

#def map_domain(category):
#    return DOMAIN_MAP.get(category, "Other")

#def map_domain(category):
#    if not category:
#        return "Other"
#
#    category = category.lower().strip()
#
#    return DOMAIN_MAP.get(category, "Other")

def map_domain(category):
    if not category:
        return "Other"

    category = category.lower().strip()

    for key in DOMAIN_MAP:
        if key in category:
            return DOMAIN_MAP[key]

    return "Other"
