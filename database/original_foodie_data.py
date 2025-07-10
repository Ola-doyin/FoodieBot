# FoodieDatabase.py
# This is a sample database just to illustrate how the Foodie AI assistant can access user and menu data.

from datetime import datetime

# Registered users and their details
users_db = {
    "oladoyin": {
        "customer_id": 1,
        "name": "Oladoyin",
        "wallet_balance": 26005.00,
        "last_orders": [
            {"food": ["Jollof Rice", "Chicken", "Plantain"], "date": "2025-07-10", "time": "13:45"},
            {"food": ["Pounded Yam", "Egusi", "Goat Meat"], "date": "2025-07-09", "time": "14:30"},
            {"food": ["Fried Yam", "Peppered Chicken"], "date": "2025-07-08", "time": "11:15"},
            {"food": ["Village Rice", "Fish Sauce"], "date": "2025-07-07", "time": "15:10"},
            {"food": ["Rice And Beans", "Gizz Dodo", "Zobo Drink"], "date": "2025-07-06", "time": "18:20"},
            {"food": ["Chapman"], "date": "2025-07-05", "time": "10:00"},
        ]
    },
    "daniel": {
        "customer_id": 2,
        "name": "Daniel",
        "wallet_balance": 3700.00,
        "last_orders": [
            {"food": ["Ofada Rice/Sauce", "Boiled Egg", "Palmwine"], "date": "2025-07-09", "time": "12:10"},
            {"food": ["Ofada Rice/Sauce", "Boiled Egg"], "date": "2025-07-06", "time": "12:50"},
            {"food": ["Amala", "Ewedu", "Gbegiri", "Assorted"], "date": "2025-07-05", "time": "14:00"},
            {"food": ["White Rice", "Moi Moi", "Fried Potatoes"], "date": "2025-07-02", "time": "17:40"},
        ]
    },
    "frankfelix": {
        "customer_id": 3,
        "name": "FrankFelix",
        "wallet_balance": 13904.00,
        "last_orders": [
            {"food": ["Spaghetti Jollof", "Egg Sauce"], "date": "2025-07-10", "time": "19:10"},
            {"food": ["Yam Porridge", "Fried Plantain"], "date": "2025-07-08", "time": "13:10"},
            {"food": ["Ewa Agoyin", "Chicken (Small)", "Zobo Drink"], "date": "2025-07-06", "time": "09:50"},
            {"food": ["Semovita", "Ogbono", "Ponmo"], "date": "2025-07-05", "time": "14:30"},
            {"food": ["Fruit Salad", "Puff Puff"], "date": "2025-07-04", "time": "10:20"},
            {"food": ["Boiled Yam", "Catfish Pepper Soup"], "date": "2025-07-03", "time": "18:30"},
        ]
    },
    "y.k": {
        "customer_id": 4,
        "name": "Y.K",
        "wallet_balance": 18003.00,
        "last_orders": [
            {"food": ["Eba", "Edikaikong", "Cow Leg"], "date": "2025-07-10", "time": "13:15"},
            {"food": ["Special Fried Rice", "Turkey (Small)", "Milk Shake"], "date": "2025-07-09", "time": "16:00"},
            {"food": ["Boiled Plantain", "Egg Sauce", "Shrimps"], "date": "2025-07-08", "time": "20:00"},
        ]
    },
    "blessing": {
        "customer_id": 5,
        "name": "Blessing",
        "wallet_balance": 35700.00,
        "last_orders": [
            {"food": ["Fried Rice", "Moi Moi", "Croaker Fish"], "date": "2025-07-10", "time": "14:00"},
            {"food": ["Semovita", "Seafood Okro"], "date": "2025-07-09", "time": "15:40"},
            {"food": ["Akara", "Cooked Pap"], "date": "2025-07-08", "time": "07:30"},
            {"food": ["Gizz Dodo", "Boiled Yam", "Zobo Drink"], "date": "2025-07-07", "time": "12:10"},
            {"food": ["Palmwine"], "date": "2025-07-06", "time": "18:20"},
            {"food": ["Ogbono", "Goat Meat", "Water"], "date": "2025-07-05", "time": "14:50"},
            {"food": ["Catfish Pepper Soup", "Pounded Yam"], "date": "2025-07-04", "time": "20:10"},
        ]
    },
    "crystal": {
        "customer_id": 6,
        "name": "Crystal",
        "wallet_balance": 7910.00,
        "last_orders": [
            {"food": ["Fruit Salad", "Milk Shake"], "date": "2025-07-10", "time": "11:45"},
        ]
    }
}


menu_db = {
    "sides": [
        {"name": "Puff Puff", "price": 400},
        {"name": "Fried Yam", "price": 400},
        {"name": "Fried Potatoes", "price": 400},
        {"name": "Fruit Salad", "price": 500},
        {"name": "Akara", "price": 500},
        {"name": "Cooked Pap", "price": 300},
        {"name": "Peppered Ponmo", "price": 250},
        {"name": "Peppered Chicken", "price": 850},
        {"name": "Round Panla", "price": 600},
        {"name": "Shrimps", "price": 1200}
    ],
    
    "main_menu": [
        {"name": "Jollof Rice", "price": 900},
        {"name": "Village Rice", "price": 1000},
        {"name": "Ofada Rice/Sauce", "price": 1700},
        {"name": "Coconut Rice", "price": 1200},
        {"name": "White Rice", "price": 800},
        {"name": "Rice And Beans", "price": 800},
        {"name": "Special Fried Rice", "price": 1200},
        {"name": "Ewa Agoyin", "price": 600},
        {"name": "Beans Porridge", "price": 500},
        {"name": "Yam Porridge", "price": 700},
        {"name": "Boiled Yam", "price": 500},
        {"name": "Spaghetti Jollof", "price": 700},
        {"name": "Farm House Porridge", "price": 800}
    ],
    
    "soups": [
        {"name": "Egusi", "price": 900},
        {"name": "Efo Riro", "price": 900},
        {"name": "Edikaikong", "price": 900},
        {"name": "Afang", "price": 900},
        {"name": "Ogbono", "price": 900},
        {"name": "Ewedu", "price": 100},
        {"name": "Gbegiri", "price": 100},
        {"name": "Catfish Pepper Soup", "price": 1000},
        {"name": "Bitter Leaf Soup", "price": 900},
        {"name": "Seafood Okro", "price": 3500},
        {"name": "White Soup", "price": 1500},
        {"name": "Oha Soup", "price": 900}
    ],

    "proteins": [
        {"name": "Hake Fish", "price": 1200},
        {"name": "Titus", "price": 1000},
        {"name": "Turkey (Big)", "price": 2000},
        {"name": "Turkey (Small)", "price": 1200},
        {"name": "Chicken", "price": 1700},
        {"name": "Chicken (Small)", "price": 850},
        {"name": "Cow Leg", "price": 1000},
        {"name": "Goat Meat", "price": 1500},
        {"name": "Beef", "price": 700},
        {"name": "Assorted", "price": 500},
        {"name": "Ponmo", "price": 500},
        {"name": "Panla", "price": 600},
        {"name": "Boiled Egg", "price": 250},
        {"name": "Croaker Fish", "price": 2000},
        {"name": "Roasted Cat Fish", "price": 2000}
    ],
    
    "swallows": [
        {"name": "Amala", "price": 500},
        {"name": "Pounded Yam", "price": 400},
        {"name": "Semo", "price": 300},
        {"name": "Eba", "price": 200}
    ],
    
    "extras": [
        {"name": "Plantain", "price": 500},
        {"name": "Egg Sauce", "price": 500},
        {"name": "Moi Moi", "price": 500},
        {"name": "Fish Sauce", "price": 1000},
        {"name": "Boiled Plantain", "price": 900},
        {"name": "Gizz Dodo", "price": 900},
        {"name": "Ofada Sauce", "price": 900}
    ],

    "drinks": [
        {"name": "Palmwine", "price": 700},
        {"name": "Zobo Drink", "price": 500},
        {"name": "Chapman", "price": 700},
        {"name": "Soda", "price": 400},
        {"name": "Milk Shake", "price": 800},
        {"name": "Apple Juice", "price": 700},
        {"name": "Blackcurrant Juice", "price": 600},
        {"name": "Caprison", "price": 300},
        {"name": "Malt", "price": 500},
        {"name": "Water", "price": 200}
    ],
    
    "settings": {
        "takeaway_pack_price": 500,
        "vat_percentage": 7.5
    }
}
