import pandas as pd

class Cleanig_Data():

    def sales_data_cleaning(self, sales_data):

        sales_data = sales_data[['INVOICEDAT', 'BRANCHNO', 'Make', 'Model', 'SALEPRICE', 'COSTPRICE', 'METALPROFIT', 'BODYCOLOUR']]
        sales_data.drop_duplicates(inplace=True)

        sales_data.Make = sales_data.Make.str.lower()

        # Step 1: Replace similar or duplicate names to consolidate them
        # You can adjust or add replacements based on similarity
        sales_data['Make'] = sales_data['Make'].replace({
            ' ford': 'ford', 'fiesta': 'ford', 'ford kuga': 'ford', 'vw golf': 'volkswagen', 
            'mercedes benz': 'mercedes', 'polestar': 'volvo', 'kuga': 'ford',
            'fiat\\abarth': 'fiat', 'abarth': 'fiat', 'f0rd': 'ford',
            'fo[rd': 'ford', 'foird': 'ford', 'forde': 'ford'
        })

        # Step 2: Count occurrences and categorize low-frequency names
        threshold = 139 # You can adjust this threshold for what qualifies as "low-count"
        make_counts = sales_data['Make'].value_counts()
        low_count_makes = make_counts[make_counts < threshold].index

        # Replace low-count names with "Other"
        sales_data['Make_new'] = sales_data['Make'].apply(lambda x: 'Other' if x in low_count_makes else x)


        sales_data.Model = sales_data.Model.str.lower()

        car_variants = {
        "Ford Fiesta Variants": [
            "fiesta",
            "fiesta titanium x",
            "fiesta zetec turbo",
            "fiesta vignale",
            "fiesta van",
            "fiesta st-3 turbo hatchback",
            "fiesta titanium turbo hat",
            "fiesta zetec tdci 70 hatc",
            "fiesta titanium 90 tdci h",
            "fiesta edge",
            "fiesta zetec climate",
            "fiesta base tdci car deri",
            "fiesta titanium hatchback",
            "fiesta edge 60",
            "fiesta hatchback special editi",
            "fiesta vignale hatchback"
        ],
        "Ford Focus Variants": [
            "focus",
            "focus rs",
            "focus vignale",
            "focus cc",
            "focus titanium turbo hatc",
            "focus titanium tdci hatch",
            "focus active",
            "focus st-line",
            "focus style",
            "focus lx",
            "focus 1.6 style 5dr",
            "focus hat 1.0 125 titanium x e",
            "focus active x",
            "focus c-max",
            "focus estate",
            "focus diesel hatchback",
            "focus hatchback"
        ],
        "Ford Transit Variants": [
            "transit",
            "transit custom",
            "transit connect",
            "transit custom 2.0",
            "transit courier",
            "transit custom ms-rt",
            "transit custom 290 limite",
            "transit custom 280 l1 die",
            "transit tipper",
            "transit 350 l2 diesel fwd",
            "transit van",
            "transit custom 320 l2 die",
            "transit connect retail"
        ],
        "Ford Kuga Variants": [
            "kuga",
            "kuga titanium edition tdc",
            "kuga st-line first editio",
            "kuga titanium x tdci hatc",
            "kuga vignale",
            "kuga diesel estate",
            "ford new kuga st-line x e"
        ],
        "Ford Puma Variants": [
            "puma",
            "ford puma",
            "puma 1.0 ecb hy mhev 155 st-li",
            "ford puma titanium mhev 1",
            "puma 1.0 ecoboost hbd mhev 125",
            "puma hatchback"
        ],
        "Ford Ranger Variants": [
            "ranger",
            "ranger diesel special edi",
            "ranger diesel pick up dou",
            "ranger ms-rt"
        ],
        "Ford Mondeo Variants": [
            "mondeo",
            "mondeo vignale",
            "mondeo titanium x bs ed t",
            "mondeo diesel estate"
        ],
        "Volkswagen Golf Variants": [
            "golf",
            "golf sv",
            "golf plus",
            "golf match hatchback"
        ],
        "BMW Series Models": [
            "1 series",
            "2 series",
            "3 series",
            "4 series",
            "5 series",
            "6 series",
            "8 series",
            "320d m sport auto",
            "330i m sport a",
            "116d m sport auto",
            "m2",
            "m3",
            "m4",
            "m5"
        ],
        "Audi A-Series Models": [
            "a1",
            "a3",
            "a4",
            "a5",
            "a6",
            "a7",
            "a8"
        ],
        "Nissan Qashqai Variants": [
            "qashqai",
            "qashqai visia",
            "qashqai+2",
            "qashqai acenta dci 2wd",
            "qashqai diesel hatchback"
        ],
        "Mini Cooper Variants": [
            "cooper",
            "cooper clubman",
            "cooper clubman estate"
        ],
        "Land Rover Range Rover Variants": [
            "range rover",
            "range rover evoque",
            "range rover velar",
            "range rover sport"
        ]
        }

        # Replace models in 'Model' column based on car_variants
        def map_variants(model):
            for main_model, variants in car_variants.items():
                if model in variants:
                    return main_model
            return model  # Return original if no match found

        sales_data['Model'] = sales_data['Model'].apply(map_variants)


        # You can adjust or add replacements based on similarity
        # Make a copy of the 'Model' column to apply changes
        sales_data['Model_new'] = sales_data['Model']

        # Loop through each category in car_variants to replace values
        for category, models in car_variants.items():
            sales_data['Model_new'] = sales_data['Model_new'].replace(models, category)

        # Step 2: Count occurrences and categorize low-frequency names
        threshold = 45 # You can adjust this threshold for what qualifies as "low-count"
        make_counts = sales_data['Model_new'].value_counts()
        low_count_makes = make_counts[make_counts < threshold].index

        # Replace low-count names with "Other"
        sales_data['Model_new'] = sales_data['Model_new'].apply(lambda x: 'Other' if x in low_count_makes else x)

        sales_data = sales_data.drop_duplicates()
    
        return sales_data
    



    
    




