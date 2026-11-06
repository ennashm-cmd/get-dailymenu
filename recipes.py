# recipes.py

LOCAL_RECIPE_DATABASE = {
    "South Indian": {
        "Veg": [
            {
                "gravy": "Arachuvitta Sambar",
                "dry_item": "Beans Carrot Poriyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~420 kcal/person",
                "ingredients": [
                    "100g Toor Dal",
                    "1/2 cup Fresh Coconut",
                    "10 Shallots",
                    "100g Beans",
                    "1 Carrot",
                    "Tamarind",
                    "Sambar Powder"
                ],
                "steps": [
                    "1. Pressure cook toor dal.",
                    "2. Grind roasted coconut, red chilies, and coriander seeds.",
                    "3. Boil vegetables in tamarind water, mix dal and ground paste.",
                    "4. Stir-fry beans and carrot with mustard and coconut.",
                    "5. Temper sambar."
                ],
                "youtube_query": "arachuvitta sambar beans poriyal recipe"
            },
            {
                "gravy": "Chettinad Poondu Kara Kuzhambu",
                "dry_item": "Vazhakkai Varuval (Raw Banana Fry)",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~450 kcal/person",
                "ingredients": [
                    "20 Garlic Cloves",
                    "15 Shallots",
                    "1 Raw Banana",
                    "Tamarind",
                    "Chettinad Spice Mix"
                ],
                "steps": [
                    "1. Extract tamarind juice.",
                    "2. Saut\u00e9 garlic and shallots in sesame oil, add tamarind and spices.",
                    "3. Slice raw banana, coat with spices, and pan fry till crisp."
                ],
                "youtube_query": "poondu kara kuzhambu raw banana fry recipe"
            },
            {
                "gravy": "Tomato Rasam",
                "dry_item": "Potato Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "20 mins",
                "calories": "~380 kcal/person",
                "ingredients": [
                    "3 Tomatoes",
                    "2 Potatoes",
                    "Pepper",
                    "Cumin",
                    "Tamarind",
                    "Garlic"
                ],
                "steps": [
                    "1. Crush pepper, cumin, garlic.",
                    "2. Mash tomatoes in tamarind water, add spices, simmer till frothy.",
                    "3. Saut\u00e9 boiled cubed potatoes with chili powder and curry leaves."
                ],
                "youtube_query": "tomato rasam potato roast recipe"
            },
            {
                "gravy": "Kerala Moru Curry",
                "dry_item": "Cabbage Thoran",
                "base_staple": "Steamed Rice",
                "cooking_time": "20 mins",
                "calories": "~350 kcal/person",
                "ingredients": [
                    "2 cups Yogurt",
                    "200g Cabbage",
                    "Coconut",
                    "Turmeric",
                    "Green Chilies"
                ],
                "steps": [
                    "1. Grind coconut, cumin, green chilies.",
                    "2. Mix into curd, warm gently.",
                    "3. Stir-fry shredded cabbage with coconut and green chili."
                ],
                "youtube_query": "kerala moru curry cabbage thoran recipe"
            },
            {
                "gravy": "Ennai Kathirikai Kuzhambu",
                "dry_item": "Chow Chow Kootu",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~460 kcal/person",
                "ingredients": [
                    "6 Eggplants",
                    "1 Chayote Squash",
                    "50g Moong Dal",
                    "Sesame Oil",
                    "Tamarind"
                ],
                "steps": [
                    "1. Shallow fry slit eggplants.",
                    "2. Prepare tamarind gravy with shallots and fried eggplants.",
                    "3. Boil chayote with moong dal and tempered coconut-cumin paste."
                ],
                "youtube_query": "ennai kathirikai kuzhambu chow chow kootu recipe"
            },
            {
                "gravy": "Vendakkai Puli Kuzhambu",
                "dry_item": "Kovakkai Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~400 kcal/person",
                "ingredients": [
                    "150g Okra",
                    "150g Ivy Gourd",
                    "Tamarind Extract",
                    "Shallots",
                    "Sambar Powder"
                ],
                "steps": [
                    "1. Saut\u00e9 sliced okra until non-sticky.",
                    "2. Simmer tamarind water with shallots, spices, and okra.",
                    "3. Stir-fry round cut ivy gourd with spices until tender."
                ],
                "youtube_query": "vendakkai puli kuzhambu kovakkai fry recipe"
            },
            {
                "gravy": "Spinach Pasi Paruppu Kootu",
                "dry_item": "Seppankizhangu Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~430 kcal/person",
                "ingredients": [
                    "1 Bunch Spinach",
                    "50g Moong Dal",
                    "250g Taro Root",
                    "Chili Powder",
                    "Cumin"
                ],
                "steps": [
                    "1. Boil taro root, slice, toss in spices and deep fry till crisp.",
                    "2. Cook spinach and moong dal, fold in coconut-cumin paste and temper."
                ],
                "youtube_query": "spinach moong dal kootu seppankizhangu roast recipe"
            },
            {
                "gravy": "Mysore Rasam",
                "dry_item": "Senai Kizhangu Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~410 kcal/person",
                "ingredients": [
                    "2 Tomatoes",
                    "200g Yam",
                    "50g Toor Dal",
                    "Mysore Rasam Spice",
                    "Coconut"
                ],
                "steps": [
                    "1. Grind fresh roasted Mysore rasam paste.",
                    "2. Simmer cooked dal water with tomatoes and rasam paste.",
                    "3. Boil yam, coat with spices, pan-roast until golden crisp."
                ],
                "youtube_query": "mysore rasam yam fry recipe"
            },
            {
                "gravy": "Udupi Hotel Style Sambar",
                "dry_item": "Beetroot Poriyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~390 kcal/person",
                "ingredients": [
                    "100g Toor Dal",
                    "1 Beetroot",
                    "Mixed Veggies",
                    "Jaggery",
                    "Udupi Sambar Powder"
                ],
                "steps": [
                    "1. Cook dal and mixed vegetables with tamarind, jaggery, and coconut sambar powder.",
                    "2. Grate beetroot, stir-fry with mustard, green chili, and coconut."
                ],
                "youtube_query": "udupi sambar beetroot poriyal recipe"
            },
            {
                "gravy": "Mampazha Pulissery",
                "dry_item": "Kaya Mezhukkupuratti",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~440 kcal/person",
                "ingredients": [
                    "2 Ripe Small Mangoes",
                    "1 cup Yogurt",
                    "1 Raw Banana",
                    "Coconut Paste",
                    "Shallots"
                ],
                "steps": [
                    "1. Cook ripe mangoes with chili powder, turmeric, and water.",
                    "2. Stir in ground coconut paste and beaten curd.",
                    "3. Stir-fry raw banana slices with shallots and chili in coconut oil."
                ],
                "youtube_query": "mampazha pulissery kaya mezhukkupuratti recipe"
            },
            {
                "gravy": "Sundakkai Vatha Kuzhambu",
                "dry_item": "Pudalangai Poriyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~400 kcal/person",
                "ingredients": [
                    "2 tbsp Sundakkai Vathal",
                    "200g Snake Gourd",
                    "Tamarind",
                    "Sesame Oil",
                    "Grated Coconut"
                ],
                "steps": [
                    "1. Fry dried turkey berries in sesame oil.",
                    "2. Simmer tamarind extract with garlic, shallots, sambar powder, and fried berries.",
                    "3. Saut\u00e9 chopped snake gourd with moong dal and coconut."
                ],
                "youtube_query": "sundakkai vatha kuzhambu pudalangai poriyal recipe"
            },
            {
                "gravy": "Kerala Kalan",
                "dry_item": "Chenena Stems Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~420 kcal/person",
                "ingredients": [
                    "1 Raw Plantain",
                    "1 cup Sour Yogurt",
                    "Coconut Paste",
                    "Black Pepper",
                    "Turmeric"
                ],
                "steps": [
                    "1. Cook cubed plantain with pepper and turmeric.",
                    "2. Add thick yogurt and coconut paste, simmer till gravy is thick.",
                    "3. Stir-fry plantain stems in coconut oil with mustard seeds."
                ],
                "youtube_query": "kerala kalan plantain stir fry recipe"
            },
            {
                "gravy": "Milagu Rasam",
                "dry_item": "Vazhaipoo Usili",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~390 kcal/person",
                "ingredients": [
                    "1 tbsp Black Pepper",
                    "1 cup Banana Flower",
                    "50g Chana Dal",
                    "Tamarind",
                    "Garlic"
                ],
                "steps": [
                    "1. Grind chana dal, steam into dumplings, crumble into usili with banana flower.",
                    "2. Crush pepper, garlic, cumin, boil with tomato tamarind broth, temper in ghee."
                ],
                "youtube_query": "milagu rasam vazhaipoo usili recipe"
            },
            {
                "gravy": "Hotel Style Veg Kurma",
                "dry_item": "Baby Potato Fry",
                "base_staple": "Steamed Rice / Chapathi",
                "cooking_time": "30 mins",
                "calories": "~480 kcal/person",
                "ingredients": [
                    "1 cup Mixed Veggies",
                    "200g Baby Potatoes",
                    "Coconut",
                    "Cashews",
                    "Fennel Seeds"
                ],
                "steps": [
                    "1. Grind coconut, cashews, and fennel into smooth paste.",
                    "2. Simmer veggies with kurma paste.",
                    "3. Parboil baby potatoes, toss in spices, pan-roast until golden crisp."
                ],
                "youtube_query": "veg kurma baby potato fry recipe"
            },
            {
                "gravy": "Kallu Kadai Sambar",
                "dry_item": "Ridge Gourd Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~400 kcal/person",
                "ingredients": [
                    "100g Toor Dal",
                    "1 Ridge Gourd",
                    "Tomatoes",
                    "Shallots",
                    "Moong Dal"
                ],
                "steps": [
                    "1. Cook toor dal with tomatoes and turmeric.",
                    "2. Simmer shallots in sambar broth, mix cooked dal.",
                    "3. Saut\u00e9 ridge gourd cubes with green chilies and moong dal for dry stir-fry."
                ],
                "youtube_query": "hotel style sambar ridge gourd fry recipe"
            },
            {
                "gravy": "Poondu Rasam",
                "dry_item": "Kathirikai Podi Varuval",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~410 kcal/person",
                "ingredients": [
                    "15 Garlic Cloves",
                    "4 Brinjals",
                    "Roasted Spice Powder",
                    "Tamarind",
                    "Cumin"
                ],
                "steps": [
                    "1. Boil crushed garlic, pepper, cumin in tamarind extract.",
                    "2. Quarter brinjals, stuff with spiced roasted dal powder.",
                    "3. Shallow fry stuffed brinjals on low heat."
                ],
                "youtube_query": "poondu rasam kathirikai podi varuval recipe"
            },
            {
                "gravy": "Gongura Pappu",
                "dry_item": "Arbi Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~440 kcal/person",
                "ingredients": [
                    "1 Bunch Sorrel Leaves",
                    "100g Toor Dal",
                    "200g Arbi",
                    "Green Chilies",
                    "Garlic"
                ],
                "steps": [
                    "1. Pressure cook toor dal with fresh sorrel leaves.",
                    "2. Mash dal-gongura mix and temper with garlic and ghee.",
                    "3. Boil, peel, flatten, and crisp fry arbi with red chili powder."
                ],
                "youtube_query": "gongura pappu arbi roast recipe"
            },
            {
                "gravy": "Majjiga Huli",
                "dry_item": "Bhendi Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "20 mins",
                "calories": "~380 kcal/person",
                "ingredients": [
                    "1.5 cups Sour Curd",
                    "200g Okra",
                    "Coconut",
                    "Chana Dal",
                    "Cumin"
                ],
                "steps": [
                    "1. Grind chana dal, coconut, cumin, green chili.",
                    "2. Whisk curd, mix paste, warm gently.",
                    "3. Cut bhindi into strips, coat with cornstarch, crisp fry."
                ],
                "youtube_query": "majjiga huli bhindi fry recipe"
            },
            {
                "gravy": "Tomato Onion Thokku Gravy",
                "dry_item": "Cabbage Carrot Poriyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~390 kcal/person",
                "ingredients": [
                    "4 Tomatoes",
                    "2 Onions",
                    "150g Cabbage",
                    "1 Carrot",
                    "Chili Powder"
                ],
                "steps": [
                    "1. Saut\u00e9 onions and tomatoes in sesame oil with chili powder till oil separates.",
                    "2. Stir-fry shredded cabbage and grated carrot with coconut and green chili."
                ],
                "youtube_query": "tomato onion thokku cabbage poriyal recipe"
            },
            {
                "gravy": "Pasi Paruppu Sambar",
                "dry_item": "Raw Banana Podi Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "20 mins",
                "calories": "~410 kcal/person",
                "ingredients": [
                    "100g Moong Dal",
                    "1 Raw Banana",
                    "Tomatoes",
                    "Idli Podi",
                    "Turmeric"
                ],
                "steps": [
                    "1. Boil moong dal with tomatoes and green chilies.",
                    "2. Steam cubed raw banana, toss with idli podi and oil, roast crisp.",
                    "3. Temper moong dal sambar in ghee."
                ],
                "youtube_query": "moong dal sambar raw banana fry recipe"
            },
            {
                "gravy": "Kollu Rasam",
                "dry_item": "Kollu Thuvaiyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~370 kcal/person",
                "ingredients": [
                    "50g Horsegram",
                    "Tamarind",
                    "Black Pepper",
                    "Cumin",
                    "Garlic"
                ],
                "steps": [
                    "1. Boil horsegram, strain broth for rasam.",
                    "2. Grind remaining cooked horsegram with coconut and red chili for thuvaiyal.",
                    "3. Boil broth with tamarind and pepper, temper in ghee."
                ],
                "youtube_query": "kollu rasam thuvaiyal recipe"
            },
            {
                "gravy": "South Style Chana Gravy",
                "dry_item": "Aloo Cauliflower Fry",
                "base_staple": "Steamed Rice / Chapathi",
                "cooking_time": "30 mins",
                "calories": "~460 kcal/person",
                "ingredients": [
                    "1 cup Black Chana",
                    "1 cup Cauliflower",
                    "1 Potato",
                    "Coconut-Fennel Paste"
                ],
                "steps": [
                    "1. Pressure cook soaked chana.",
                    "2. Simmer with onion, tomato, and coconut-fennel paste.",
                    "3. Toss blanched cauliflower florets and potato cubes with spices, pan-fry."
                ],
                "youtube_query": "south indian chana masala aloo cauliflower fry recipe"
            },
            {
                "gravy": "Manathakkali Vatha Kuzhambu",
                "dry_item": "Broad Beans Poriyal",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~390 kcal/person",
                "ingredients": [
                    "2 tbsp Black Nightshade Berries",
                    "200g Broad Beans",
                    "Tamarind",
                    "Shallots",
                    "Coconut"
                ],
                "steps": [
                    "1. Fry berries in sesame oil.",
                    "2. Boil tamarind extract with sambar powder, small onions, and fried berries.",
                    "3. Chop broad beans, steam, stir-fry with coconut."
                ],
                "youtube_query": "manathakkali vatha kuzhambu avarakkai poriyal recipe"
            },
            {
                "gravy": "Kerala Veg Coconut Milk Stew",
                "dry_item": "Potato Roast",
                "base_staple": "Appam / Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~430 kcal/person",
                "ingredients": [
                    "1 cup Coconut Milk",
                    "1 Potato",
                    "1 Carrot",
                    "Green Chilies",
                    "Coconut Oil"
                ],
                "steps": [
                    "1. Boil diced veggies with thin coconut milk, ginger, green chilies.",
                    "2. Add thick coconut milk, warm gently, drizzle raw coconut oil.",
                    "3. Pan roast potato cubes with black pepper."
                ],
                "youtube_query": "kerala veg stew potato roast recipe"
            },
            {
                "gravy": "Drumstick Leaves Sambar",
                "dry_item": "Raw Plantain Podimas",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~410 kcal/person",
                "ingredients": [
                    "1 cup Fresh Drumstick Leaves",
                    "1 Raw Plantain",
                    "100g Toor Dal",
                    "Lemon Juice",
                    "Green Chilies"
                ],
                "steps": [
                    "1. Cook toor dal. Simmer tamarind water with sambar powder.",
                    "2. Add fresh drumstick leaves, cook 5 mins, stir in dal.",
                    "3. Steam raw plantain, grate, saut\u00e9 with green chilies, ginger, mustard, lemon juice."
                ],
                "youtube_query": "murungai keerai sambar vazhakkai podimas recipe"
            }
        ],
        "Non-Veg": [
            {
                "gravy": "Chettinad Chicken Kuzhambu",
                "dry_item": "Mutton Pepper Fry",
                "base_staple": "Steamed Rice / Parotta",
                "cooking_time": "35 mins",
                "calories": "~580 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Mutton",
                    "Black Pepper",
                    "Fennel Seeds",
                    "Shallots",
                    "Coconut"
                ],
                "steps": [
                    "1. Roast pepper, fennel, coriander, coconut into Chettinad masala.",
                    "2. Cook chicken with shallots and ground masala.",
                    "3. Pressure cook mutton, stir-fry with black pepper and garlic till dry."
                ],
                "youtube_query": "chettinad chicken kuzhambu mutton pepper fry recipe"
            },
            {
                "gravy": "Kerala Meen Curry",
                "dry_item": "Prawn Pepper Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~510 kcal/person",
                "ingredients": [
                    "400g Kingfish",
                    "250g Prawns",
                    "Kudampuli",
                    "Shallots",
                    "Ginger",
                    "Coconut Oil"
                ],
                "steps": [
                    "1. Soak kudampuli.",
                    "2. Cook shallots, ginger, chili powder, and kudampuli in clay pot; add fish and simmer.",
                    "3. Saut\u00e9 prawns with onions, pepper, and curry leaves in coconut oil until dry."
                ],
                "youtube_query": "kerala meen curry prawn pepper roast recipe"
            },
            {
                "gravy": "Nattu Kozhi Kuzhambu",
                "dry_item": "Chicken Chintamani",
                "base_staple": "Steamed Rice / Dosa",
                "cooking_time": "40 mins",
                "calories": "~560 kcal/person",
                "ingredients": [
                    "500g Country Chicken",
                    "300g Boneless Chicken",
                    "Dried Red Chilies",
                    "Shallots",
                    "Sesame Oil"
                ],
                "steps": [
                    "1. Pressure cook country chicken with shallots, tomatoes, and ground curry spices.",
                    "2. Saut\u00e9 deseeded red chilies and shallots in sesame oil, add boneless chicken and cook dry."
                ],
                "youtube_query": "nattu kozhi kuzhambu chicken chintamani recipe"
            },
            {
                "gravy": "Madurai Mutton Kuzhambu",
                "dry_item": "Chicken 65",
                "base_staple": "Steamed Rice / Parotta",
                "cooking_time": "40 mins",
                "calories": "~610 kcal/person",
                "ingredients": [
                    "400g Mutton",
                    "300g Boneless Chicken",
                    "Curd",
                    "Cornstarch",
                    "Fennel Powder"
                ],
                "steps": [
                    "1. Pressure cook mutton with fennel, cumin, coriander, and onion-tomato paste.",
                    "2. Marinate chicken in curd, chili, ginger-garlic, cornstarch.",
                    "3. Deep fry chicken till crisp."
                ],
                "youtube_query": "madurai mutton kuzhambu chicken 65 recipe"
            },
            {
                "gravy": "Andhra Kodi Kura",
                "dry_item": "Royyala Vepudu",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~540 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "250g Prawns",
                    "Guntur Red Chilies",
                    "Poppy Seeds",
                    "Coconut"
                ],
                "steps": [
                    "1. Grind coconut and poppy seeds.",
                    "2. Saut\u00e9 chicken with spicy red chili powder and poppy paste.",
                    "3. Stir-fry prawns with green chilies, onions, garlic, and pepper till dry."
                ],
                "youtube_query": "andhra kodi kura royyala vepudu recipe"
            },
            {
                "gravy": "Nethili Meen Kuzhambu",
                "dry_item": "Vanjaram Fish Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~480 kcal/person",
                "ingredients": [
                    "250g Anchovies",
                    "2 Slices Vanjaram",
                    "Tamarind",
                    "Shallots",
                    "Rice Flour"
                ],
                "steps": [
                    "1. Boil tamarind water with shallots, chili powder, coriander powder; add anchovies.",
                    "2. Marinate Vanjaram fish with chili powder, lemon, rice flour.",
                    "3. Tawa fry fish until crisp."
                ],
                "youtube_query": "nethili meen kuzhambu vanjaram fish fry recipe"
            },
            {
                "gravy": "Malabar Chicken Curry",
                "dry_item": "Kerala Fish Roast",
                "base_staple": "Kerala Parotta / Rice",
                "cooking_time": "35 mins",
                "calories": "~570 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Fish Steaks",
                    "Coconut Milk",
                    "Shallots",
                    "Fennel"
                ],
                "steps": [
                    "1. Saut\u00e9 chicken with roasted coconut paste and coconut milk.",
                    "2. Sear fish steaks in coconut oil.",
                    "3. Saut\u00e9 shallots, ginger, curry leaves, and coat fried fish in thick dry masala."
                ],
                "youtube_query": "malabar chicken curry kerala fish roast recipe"
            },
            {
                "gravy": "Egg Thokku Gravy",
                "dry_item": "Chicken Pepper Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~500 kcal/person",
                "ingredients": [
                    "4 Boiled Eggs",
                    "300g Chicken",
                    "Onions",
                    "Tomatoes",
                    "Black Pepper"
                ],
                "steps": [
                    "1. Make deep cuts on boiled eggs, simmer in thick spicy tomato onion thokku.",
                    "2. Saut\u00e9 chicken with onions, garlic, black pepper, and fennel till bone-dry."
                ],
                "youtube_query": "egg thokku gravy chicken pepper roast recipe"
            },
            {
                "gravy": "Crab Curry",
                "dry_item": "Squid Roast",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "500g Crabs",
                    "300g Squid Rings",
                    "Black Pepper",
                    "Cumin",
                    "Fennel",
                    "Tamarind"
                ],
                "steps": [
                    "1. Grind pepper, cumin, fennel, garlic, coconut.",
                    "2. Cook crabs with ground masala, shallots, tamarind.",
                    "3. Saut\u00e9 squid rings on high heat with chilies, garlic, pepper till dry."
                ],
                "youtube_query": "crab curry squid roast recipe"
            },
            {
                "gravy": "Gongura Mutton Curry",
                "dry_item": "Chicken Varuval",
                "base_staple": "Steamed Rice",
                "cooking_time": "40 mins",
                "calories": "~620 kcal/person",
                "ingredients": [
                    "400g Mutton",
                    "300g Chicken",
                    "1 Bunch Sorrel Leaves",
                    "Shallots",
                    "Red Chili Powder"
                ],
                "steps": [
                    "1. Mash cooked gongura leaves.",
                    "2. Pressure cook mutton, simmer with gongura paste and red chili powder.",
                    "3. Saut\u00e9 chicken with shallots, ginger-garlic, curry leaves until dry."
                ],
                "youtube_query": "gongura mutton chicken varuval recipe"
            },
            {
                "gravy": "Kottayam Fish Curry",
                "dry_item": "Mutton Kola Urundai",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~530 kcal/person",
                "ingredients": [
                    "400g Fish",
                    "250g Minced Mutton",
                    "Kudampuli",
                    "Roasted Chana Dal",
                    "Fennel"
                ],
                "steps": [
                    "1. Boil fish in clay pot with dark chili powder, ginger, and kudampuli.",
                    "2. Grind minced mutton with chana dal, fennel, and coconut into small balls; deep fry till crisp."
                ],
                "youtube_query": "kottayam fish curry mutton kola urundai recipe"
            },
            {
                "gravy": "Hyderabadi Dum Chicken Gravy",
                "dry_item": "Tala Hua Gosht",
                "base_staple": "Bagara Rice / Steamed Rice",
                "cooking_time": "40 mins",
                "calories": "~640 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Boneless Mutton",
                    "Curd",
                    "Fried Onions",
                    "Mint"
                ],
                "steps": [
                    "1. Marinate chicken with curd, fried onions, mint, spices; dum cook.",
                    "2. Boil boneless mutton.",
                    "3. Stir-fry mutton in oil with green chilies, pepper, lemon juice till dry."
                ],
                "youtube_query": "hyderabadi dum chicken tala hua gosht recipe"
            },
            {
                "gravy": "Kerala Duck Curry",
                "dry_item": "Chicken Chukka",
                "base_staple": "Appam / Steamed Rice",
                "cooking_time": "45 mins",
                "calories": "~650 kcal/person",
                "ingredients": [
                    "500g Duck Meat",
                    "300g Chicken",
                    "Coconut Milk",
                    "Shallots",
                    "Curry Leaves"
                ],
                "steps": [
                    "1. Pressure cook duck meat with potato, spices, thin coconut milk; finish with thick coconut milk.",
                    "2. Saut\u00e9 chicken with small onions, black pepper, fennel, and curry leaves till dry."
                ],
                "youtube_query": "kerala tharavu curry chicken chukka recipe"
            },
            {
                "gravy": "Mangalorean Fish Gassi",
                "dry_item": "Mangalorean Chicken Sukka",
                "base_staple": "Neer Dosa / Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~590 kcal/person",
                "ingredients": [
                    "400g Pomfret",
                    "400g Chicken",
                    "Grated Coconut",
                    "Byadgi Chilies",
                    "Tamarind"
                ],
                "steps": [
                    "1. Grind Byadgi chilies, coriander, cumin, tamarind, coconut; simmer fish in gravy.",
                    "2. Cook chicken with onion-tomato, fold in roasted coconut dry spice mix for Sukka."
                ],
                "youtube_query": "mangalorean fish gassi chicken sukka recipe"
            },
            {
                "gravy": "Mathi Kuzhambu",
                "dry_item": "Nethili Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~470 kcal/person",
                "ingredients": [
                    "300g Sardines",
                    "200g Anchovies",
                    "Tamarind",
                    "Shallots",
                    "Cornstarch"
                ],
                "steps": [
                    "1. Boil sardines in acidic tamarind water with shallots and chili powder.",
                    "2. Marinate anchovies in chili powder, turmeric, ginger-garlic, cornstarch, lemon.",
                    "3. Deep fry anchovies until extra crisp."
                ],
                "youtube_query": "mathi kuzhambu nethili fry recipe"
            },
            {
                "gravy": "Mutton Elumbu Kuzhambu",
                "dry_item": "Mutton Liver Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "40 mins",
                "calories": "~520 kcal/person",
                "ingredients": [
                    "400g Mutton Rib Bones",
                    "250g Mutton Liver",
                    "Black Pepper",
                    "Cumin",
                    "Shallots"
                ],
                "steps": [
                    "1. Pressure cook mutton bones with crushed pepper, cumin, garlic, shallots for broth gravy.",
                    "2. Clean and cube mutton liver.",
                    "3. Saut\u00e9 liver with shallots, cumin, black pepper, curry leaves till cooked and dry."
                ],
                "youtube_query": "mutton elumbu kuzhambu eeral varuval recipe"
            },
            {
                "gravy": "Chicken Salna",
                "dry_item": "Egg Pepper Fry",
                "base_staple": "Parotta / Rice",
                "cooking_time": "30 mins",
                "calories": "~530 kcal/person",
                "ingredients": [
                    "300g Chicken",
                    "4 Boiled Eggs",
                    "Coconut",
                    "Cashews",
                    "Poppy Seeds",
                    "Fennel Seeds"
                ],
                "steps": [
                    "1. Blend coconut, cashews, poppy seeds, fennel; cook chicken with tomato base and paste for thin salna.",
                    "2. Halve boiled eggs, toss in pan with butter, black pepper, onions, curry leaves."
                ],
                "youtube_query": "chicken salna egg pepper fry recipe"
            },
            {
                "gravy": "Prawn Curry",
                "dry_item": "Chicken Pallipalayam",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~540 kcal/person",
                "ingredients": [
                    "300g Prawns",
                    "300g Chicken",
                    "Coconut Bits",
                    "Shallots",
                    "Red Chili Bits"
                ],
                "steps": [
                    "1. Simmer cleaned prawns with onion, tomato, tamarind water.",
                    "2. For Pallipalayam chicken: saut\u00e9 shallots, broken red chilies, sliced coconut bits in sesame oil; add chicken and cook completely dry."
                ],
                "youtube_query": "prawn kuzhambu chicken pallipalayam recipe"
            },
            {
                "gravy": "Chettinad Egg Curry",
                "dry_item": "South Style Fish Chilly",
                "base_staple": "Steamed Rice / Chapathi",
                "cooking_time": "25 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "4 Boiled Eggs",
                    "250g Fish Cubes",
                    "Chettinad Masala",
                    "Capsicum",
                    "Onions"
                ],
                "steps": [
                    "1. Saut\u00e9 onions, garlic, Chettinad spices, add water and boiled eggs.",
                    "2. Marinate fish cubes, shallow fry.",
                    "3. Toss fried fish with capsicum, onion wedges, green chilies in dry pan."
                ],
                "youtube_query": "chettinad egg curry fish chilly recipe"
            },
            {
                "gravy": "Vellore Mutton Curry",
                "dry_item": "Chicken Ghee Roast",
                "base_staple": "Steamed Rice / Dosa",
                "cooking_time": "40 mins",
                "calories": "~630 kcal/person",
                "ingredients": [
                    "400g Mutton",
                    "300g Chicken",
                    "Byadgi Chilies",
                    "Ghee",
                    "Tamarind",
                    "Garlic"
                ],
                "steps": [
                    "1. Pressure cook mutton with garlic, onions, tomatoes, and ground spices.",
                    "2. Roast Byadgi chilies, peppercorns, coriander seeds, grind with garlic and tamarind.",
                    "3. Saut\u00e9 chicken in ghee with paste until dark red and dry."
                ],
                "youtube_query": "vellore mutton curry chicken ghee roast recipe"
            },
            {
                "gravy": "Nethili Meen Avial Gravy",
                "dry_item": "Karuvadu Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~450 kcal/person",
                "ingredients": [
                    "250g Fresh Anchovies",
                    "100g Dried Salted Fish",
                    "Coconut",
                    "Plantain",
                    "Coconut Oil"
                ],
                "steps": [
                    "1. Cook veggies and fresh anchovies; fold in coconut-cumin paste, raw coconut oil, and curry leaves for Avial.",
                    "2. Soak dried fish, wash, stir-fry with onions and chili powder till crispy."
                ],
                "youtube_query": "nethili meen avial karuvadu fry recipe"
            },
            {
                "gravy": "Rayalaseema Chicken Kura",
                "dry_item": "Mutton Vepudu",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~600 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Mutton",
                    "Spicy Red Chili Powder",
                    "Garam Masala",
                    "Shallots"
                ],
                "steps": [
                    "1. Prepare fiery chicken gravy with Guntur red chili powder and tomato base.",
                    "2. Pressure cook mutton.",
                    "3. Stir-fry mutton in pan with crushed garlic, green chilies, pepper powder till dry."
                ],
                "youtube_query": "rayalaseema chicken kura mutton vepudu recipe"
            },
            {
                "gravy": "Coastal Meen Kuzhambu",
                "dry_item": "Crab Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~500 kcal/person",
                "ingredients": [
                    "400g Sea Fish",
                    "300g Small Crabs",
                    "Tamarind",
                    "Fennel Seeds",
                    "Shallots"
                ],
                "steps": [
                    "1. Cook fish in tamarind-onion tomato base tempered with fenugreek.",
                    "2. Toss small crabs with shallots, fennel powder, red chili powder, garlic; stir-fry till orange-red and dry."
                ],
                "youtube_query": "meen kuzhambu crab fry recipe"
            },
            {
                "gravy": "Coorg Pork / Mutton Curry",
                "dry_item": "Coorg Chicken Dry Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "40 mins",
                "calories": "~670 kcal/person",
                "ingredients": [
                    "500g Meat",
                    "300g Chicken",
                    "Kachampuli Vinegar",
                    "Roasted Dark Masala",
                    "Garlic"
                ],
                "steps": [
                    "1. Roast spices dark, grind into paste.",
                    "2. Cook meat with dark paste, garlic, finish with Kachampuli vinegar.",
                    "3. Stir-fry chicken with dark roasted spices and curry leaves till crisp brown."
                ],
                "youtube_query": "pandi curry chicken dry fry recipe"
            },
            {
                "gravy": "Ambur Chicken Curry",
                "dry_item": "Mutton Brain Fry",
                "base_staple": "Steamed Rice / Samba Rice",
                "cooking_time": "30 mins",
                "calories": "~550 kcal/person",
                "ingredients": [
                    "400g Chicken",
                    "2 Goat Brains",
                    "Red Chili Paste",
                    "Curd",
                    "Garlic",
                    "Black Pepper"
                ],
                "steps": [
                    "1. Saut\u00e9 onions, garlic, soaked red chili paste, curd, and chicken for Ambur style gravy.",
                    "2. Boil goat brain with turmeric, chop, saut\u00e9 with shallots and black pepper till crisp."
                ],
                "youtube_query": "ambur chicken curry mutton brain fry recipe"
            }
        ]
    },
    "North Indian": {
        "Veg": [
            {
                "gravy": "Paneer Butter Masala",
                "dry_item": "Aloo Gobi Sukhi Subzi",
                "base_staple": "Butter Naan / Jeera Rice",
                "cooking_time": "30 mins",
                "calories": "~520 kcal/person",
                "ingredients": [
                    "200g Paneer",
                    "1 cup Cauliflower",
                    "2 Potatoes",
                    "4 Tomatoes",
                    "10 Cashews",
                    "Butter",
                    "Kasuri Methi"
                ],
                "steps": [
                    "1. Puree boiled tomatoes and cashews.",
                    "2. Cook paste in butter, add Kashmiri chili, garam masala, fresh cream, paneer cubes.",
                    "3. Stir-fry cauliflower and potato cubes with cumin, turmeric, amchur."
                ],
                "youtube_query": "paneer butter masala aloo gobi dry recipe"
            },
            {
                "gravy": "Dal Tadka",
                "dry_item": "Bhindi Do Pyaza",
                "base_staple": "Jeera Rice / Roti",
                "cooking_time": "25 mins",
                "calories": "~430 kcal/person",
                "ingredients": [
                    "100g Arhar Dal",
                    "200g Bhindi",
                    "2 Onions",
                    "2 Tomatoes",
                    "Ghee",
                    "Cumin Seeds"
                ],
                "steps": [
                    "1. Pressure cook dal with turmeric.",
                    "2. Heat ghee, fry cumin, garlic, onions, tomatoes; pour over dal.",
                    "3. Chop bhindi, stir-fry with cubed onions and amchur on high heat."
                ],
                "youtube_query": "dal tadka bhindi do pyaza recipe"
            },
            {
                "gravy": "Palak Paneer",
                "dry_item": "Jeera Aloo",
                "base_staple": "Roti / Paratha",
                "cooking_time": "25 mins",
                "calories": "~460 kcal/person",
                "ingredients": [
                    "1 Bunch Spinach",
                    "200g Paneer",
                    "3 Boiled Potatoes",
                    "1 tbsp Cumin Seeds",
                    "Garlic"
                ],
                "steps": [
                    "1. Blanch spinach, puree with green chilies.",
                    "2. Saut\u00e9 garlic, add spinach puree, simmer, mix paneer cubes and cream.",
                    "3. Heat oil, crackle cumin seeds, toss boiled potato cubes with spices."
                ],
                "youtube_query": "palak paneer jeera aloo recipe"
            },
            {
                "gravy": "Punjabi Rajma Masala",
                "dry_item": "Baingan Bharta",
                "base_staple": "Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~480 kcal/person",
                "ingredients": [
                    "1 cup Rajma",
                    "1 Large Eggplant",
                    "Onions",
                    "Tomatoes",
                    "Ginger-Garlic Paste"
                ],
                "steps": [
                    "1. Pressure cook soaked rajma.",
                    "2. Roast eggplant over flame, peel and mash.",
                    "3. Saut\u00e9 onion-tomato ginger paste, add rajma, simmer.",
                    "4. Saut\u00e9 mashed eggplant with chopped onions and tomatoes."
                ],
                "youtube_query": "punjabi rajma masala baingan bharta recipe"
            },
            {
                "gravy": "Chole Masala",
                "dry_item": "Aloo Shimla Mirch",
                "base_staple": "Bhature / Puri",
                "cooking_time": "35 mins",
                "calories": "~500 kcal/person",
                "ingredients": [
                    "1 cup Kabuli Chana",
                    "2 Capsicums",
                    "2 Potatoes",
                    "Chole Masala Powder"
                ],
                "steps": [
                    "1. Boil chickpeas with tea bag for dark color.",
                    "2. Saut\u00e9 onions, tomato puree, chole masala; add chickpeas and simmer.",
                    "3. Dice capsicum and potatoes; stir-fry in oil with cumin and coriander powder."
                ],
                "youtube_query": "chole masala aloo shimla mirch recipe"
            },
            {
                "gravy": "Kadai Paneer",
                "dry_item": "Methi Matar Malai Dry",
                "base_staple": "Roti / Naan",
                "cooking_time": "30 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "200g Paneer",
                    "1 cup Green Peas",
                    "1 cup Chopped Fenugreek Leaves",
                    "Whole Spice Roast",
                    "Heavy Cream"
                ],
                "steps": [
                    "1. Coarsely crush roasted coriander and dry red chilies.",
                    "2. Saut\u00e9 onions, capsicum, tomatoes, crushed spices, and paneer.",
                    "3. Cook fenugreek leaves and green peas; finish with cream and kasuri methi."
                ],
                "youtube_query": "kadai paneer methi matar recipe"
            },
            {
                "gravy": "Dal Makhani",
                "dry_item": "Kurkuri Bhindi",
                "base_staple": "Butter Naan / Rice",
                "cooking_time": "40 mins",
                "calories": "~550 kcal/person",
                "ingredients": [
                    "1/2 cup Urad Dal",
                    "2 tbsp Rajma",
                    "200g Bhindi",
                    "Besan",
                    "Butter",
                    "Fresh Cream"
                ],
                "steps": [
                    "1. Slow-cook soaked black lentils and rajma with butter and tomato puree; finish with heavy cream.",
                    "2. Slice bhindi thin lengthwise, coat with besan, red chili, chaat masala, rice flour; deep fry crisp."
                ],
                "youtube_query": "dal makhani kurkuri bhindi recipe"
            },
            {
                "gravy": "Shahi Paneer",
                "dry_item": "Mixed Veg Dry Fry",
                "base_staple": "Jeera Rice / Roti",
                "cooking_time": "30 mins",
                "calories": "~510 kcal/person",
                "ingredients": [
                    "200g Paneer",
                    "1 cup Mixed Veggies",
                    "Cashew-Yogurt Paste",
                    "Cardamom",
                    "Butter"
                ],
                "steps": [
                    "1. Make white rich gravy using onion-cashew paste, curd, cream, and green cardamom; simmer paneer.",
                    "2. Saut\u00e9 diced mixed vegetables with cumin, ginger juliennes, and amchur powder on high heat."
                ],
                "youtube_query": "shahi paneer mix veg dry recipe"
            },
            {
                "gravy": "Punjabi Kadi Pakora",
                "dry_item": "Aloo Baingan Dry",
                "base_staple": "Steamed Basmati Rice",
                "cooking_time": "35 mins",
                "calories": "~470 kcal/person",
                "ingredients": [
                    "1 cup Sour Curd",
                    "1 cup Besan",
                    "2 Potatoes",
                    "2 Small Eggplants",
                    "Ajwain"
                ],
                "steps": [
                    "1. Deep fry small besan-onion pakoras.",
                    "2. Whisk curd and besan with water, simmer with turmeric, add pakoras.",
                    "3. Cut potatoes and eggplant into cubes; saut\u00e9 with cumin, chili powder, and amchur."
                ],
                "youtube_query": "punjabi kadhi pakora aloo baingan recipe"
            },
            {
                "gravy": "Kashmiri Dum Aloo",
                "dry_item": "Lauki Chana Dal Dry",
                "base_staple": "Roti / Rice",
                "cooking_time": "30 mins",
                "calories": "~460 kcal/person",
                "ingredients": [
                    "12 Baby Potatoes",
                    "1/2 Bottle Gourd",
                    "50g Chana Dal",
                    "Kashmiri Chili",
                    "Fennel Powder"
                ],
                "steps": [
                    "1. Prick and deep fry baby potatoes.",
                    "2. Whisk curd with fennel powder, dry ginger, Kashmiri chili; simmer fried potatoes.",
                    "3. Cook diced bottle gourd and chana dal dry, temper with cumin."
                ],
                "youtube_query": "kashmiri dum aloo lauki chana dal recipe"
            },
            {
                "gravy": "Matar Paneer",
                "dry_item": "Gobi Matar Dry",
                "base_staple": "Roti / Paratha",
                "cooking_time": "25 mins",
                "calories": "~470 kcal/person",
                "ingredients": [
                    "150g Paneer",
                    "1 cup Green Peas",
                    "1 Cauliflower",
                    "Onion-Tomato Paste",
                    "Garam Masala"
                ],
                "steps": [
                    "1. Saut\u00e9 onion-tomato-ginger paste, add peas and spices, simmer with paneer cubes.",
                    "2. Chop cauliflower florets; stir-fry with ginger, cumin, green chilies, amchur."
                ],
                "youtube_query": "matar paneer gobi dry recipe"
            },
            {
                "gravy": "Veg Makhanwala",
                "dry_item": "Arbi Tuk",
                "base_staple": "Butter Roti / Rice",
                "cooking_time": "30 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "1.5 cups Chopped Veggies",
                    "200g Arbi",
                    "Butter",
                    "Tomato Puree",
                    "Chaat Masala"
                ],
                "steps": [
                    "1. Prepare buttery tomato gravy with cashews and cream, stir in boiled veggies.",
                    "2. Boil arbi, flatten, double deep fry until super crispy; dust with chaat masala."
                ],
                "youtube_query": "veg makhanwala arbi tuk recipe"
            },
            {
                "gravy": "Lauki Kofta Curry",
                "dry_item": "Bhindi Masala Dry",
                "base_staple": "Roti / Rice",
                "cooking_time": "35 mins",
                "calories": "~450 kcal/person",
                "ingredients": [
                    "1 Grated Lauki",
                    "200g Bhindi",
                    "Besan",
                    "Onion-Tomato Puree",
                    "Amchur"
                ],
                "steps": [
                    "1. Squeeze lauki, mix with besan and spices, roll into balls, deep fry koftas.",
                    "2. Prepare onion-tomato gravy, drop in koftas.",
                    "3. Slit bhindi and saut\u00e9 with amchur and coriander powder."
                ],
                "youtube_query": "lauki kofta curry bhindi masala dry recipe"
            },
            {
                "gravy": "Malai Kofta",
                "dry_item": "Aloo Pyaz Dry Subzi",
                "base_staple": "Naan / Jeera Rice",
                "cooking_time": "35 mins",
                "calories": "~540 kcal/person",
                "ingredients": [
                    "100g Cottage Cheese",
                    "2 Boiled Potatoes",
                    "2 Onions",
                    "Cashews",
                    "Heavy Cream"
                ],
                "steps": [
                    "1. Mash potato and paneer with cornstarch, deep fry koftas.",
                    "2. Make silky cashew-cream gravy with sweet spices and drop koftas.",
                    "3. Saut\u00e9 potato cubes and onion wedges with turmeric and cumin."
                ],
                "youtube_query": "malai kofta aloo pyaz dry recipe"
            },
            {
                "gravy": "Rajasthani Panchmel Dal",
                "dry_item": "Gatte Ki Subzi Dry",
                "base_staple": "Bati / Roti / Rice",
                "cooking_time": "35 mins",
                "calories": "~480 kcal/person",
                "ingredients": [
                    "5 Lentils Blend",
                    "1 cup Besan",
                    "Curd",
                    "Ghee",
                    "Asafoetida"
                ],
                "steps": [
                    "1. Pressure cook all 5 lentils together; temper with ghee, cloves, red chili, and hing.",
                    "2. Knead besan dough with spices, roll into logs, boil, slice, pan-fry till golden."
                ],
                "youtube_query": "panchmel dal gatte ki subzi recipe"
            },
            {
                "gravy": "Sarson Ka Saag",
                "dry_item": "Aloo Methi Dry",
                "base_staple": "Makki Ki Roti",
                "cooking_time": "40 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "2 cups Mustard Greens",
                    "1 cup Spinach",
                    "3 Potatoes",
                    "Fresh Methi",
                    "White Butter"
                ],
                "steps": [
                    "1. Boil and mash sarson and spinach; thicken with maize flour, temper with garlic and butter.",
                    "2. Dice potatoes and saut\u00e9 with chopped fresh fenugreek leaves and chili powder."
                ],
                "youtube_query": "sarson ka saag aloo methi dry recipe"
            },
            {
                "gravy": "Methi Chana Dal Gravy",
                "dry_item": "Tindora Fry",
                "base_staple": "Roti / Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~420 kcal/person",
                "ingredients": [
                    "100g Chana Dal",
                    "1 cup Methi Leaves",
                    "200g Tindora",
                    "Tomatoes",
                    "Amchur"
                ],
                "steps": [
                    "1. Pressure cook chana dal. Saut\u00e9 fresh methi leaves, onions, tomatoes; combine dal.",
                    "2. Slice tindora thin, stir-fry with turmeric, red chili, and amchur till crispy."
                ],
                "youtube_query": "methi chana dal tindora fry recipe"
            },
            {
                "gravy": "Mushroom Masala Gravy",
                "dry_item": "Corn Capsicum Dry Fry",
                "base_staple": "Roti / Rice",
                "cooking_time": "25 mins",
                "calories": "~440 kcal/person",
                "ingredients": [
                    "200g Mushrooms",
                    "1 cup Sweet Corn",
                    "1 Capsicum",
                    "Onion-Tomato Puree",
                    "Kasuri Methi"
                ],
                "steps": [
                    "1. Saut\u00e9 mushrooms. Cook onion-tomato ginger gravy, add mushrooms and kasuri methi.",
                    "2. Saut\u00e9 sweet corn kernels and capsicum with butter, black pepper, and chaat masala."
                ],
                "youtube_query": "mushroom masala corn capsicum dry recipe"
            },
            {
                "gravy": "Kashmiri Chaman",
                "dry_item": "Nadru Crisp Fry",
                "base_staple": "Steamed Basmati Rice",
                "cooking_time": "30 mins",
                "calories": "~470 kcal/person",
                "ingredients": [
                    "200g Paneer",
                    "150g Lotus Stem",
                    "Turmeric",
                    "Fennel Powder",
                    "Dry Ginger Powder"
                ],
                "steps": [
                    "1. Shallow fry paneer cubes, simmer in golden gravy made with fennel, ginger powder, and curd.",
                    "2. Thinly slice lotus stem, deep fry till golden, toss with Kashmiri spices."
                ],
                "youtube_query": "kashmiri paneer nadru fry recipe"
            },
            {
                "gravy": "Soya Chaap Gravy Masala",
                "dry_item": "Jeera Matar Dry",
                "base_staple": "Roti / Rumali Roti",
                "cooking_time": "30 mins",
                "calories": "~500 kcal/person",
                "ingredients": [
                    "4 Soya Chaap Sticks",
                    "1.5 cups Green Peas",
                    "Onion Paste",
                    "Tomato Puree",
                    "Cream"
                ],
                "steps": [
                    "1. Cut soya chaap, shallow fry, cook in spicy onion-tomato gravy with cream.",
                    "2. Saut\u00e9 green peas in ghee with cumin seeds, green chili, and black pepper."
                ],
                "youtube_query": "soya chaap masala jeera matar recipe"
            },
            {
                "gravy": "Amritsari Chole Gravy",
                "dry_item": "Nutrela Soya Badi Dry",
                "base_staple": "Amritsari Kulcha / Paratha",
                "cooking_time": "35 mins",
                "calories": "~490 kcal/person",
                "ingredients": [
                    "1 cup Kabuli Chana",
                    "1 cup Soya Chunks",
                    "Anardana Powder",
                    "Tea Bag",
                    "Ghee"
                ],
                "steps": [
                    "1. Boil chickpeas with tea bag. Cook with roasted anardana powder and garlic-ghee temper.",
                    "2. Boil soya chunks, squeeze water, stir-fry with onions, capsicum, and dry spices."
                ],
                "youtube_query": "amritsari chole soya chunks dry recipe"
            },
            {
                "gravy": "Kaju Butter Masala",
                "dry_item": "Aloo Soyabean Dry",
                "base_staple": "Roti / Naan",
                "cooking_time": "25 mins",
                "calories": "~530 kcal/person",
                "ingredients": [
                    "1 cup Cashews",
                    "1 Potato",
                    "1/2 cup Soya Chunks",
                    "Tomato Puree",
                    "Butter"
                ],
                "steps": [
                    "1. Roast cashews in butter, simmer in rich tomato-cream gravy.",
                    "2. Boil soya chunks and potato cubes; stir-fry with cumin, red chili, and garam masala."
                ],
                "youtube_query": "kaju butter masala aloo soya dry recipe"
            },
            {
                "gravy": "Dahi Aloo Gravy",
                "dry_item": "Pyaz Bhindi Dry",
                "base_staple": "Puri / Roti",
                "cooking_time": "25 mins",
                "calories": "~440 kcal/person",
                "ingredients": [
                    "4 Boiled Potatoes",
                    "200g Bhindi",
                    "1 cup Whisked Curd",
                    "2 Onions",
                    "Hing"
                ],
                "steps": [
                    "1. Saut\u00e9 potato cubes with hing and cumin, add whisked curd with turmeric and red chili, simmer gently.",
                    "2. Chop bhindi and onion wedges; stir-fry until tender."
                ],
                "youtube_query": "dahi aloo pyaz bhindi recipe"
            },
            {
                "gravy": "Navratan Korma",
                "dry_item": "Aloo Methi Sukhi Subzi",
                "base_staple": "Butter Naan / Rice",
                "cooking_time": "35 mins",
                "calories": "~510 kcal/person",
                "ingredients": [
                    "1.5 cups Mixed Veg & Fruits",
                    "2 Potatoes",
                    "Fresh Methi",
                    "Nuts",
                    "Cream"
                ],
                "steps": [
                    "1. Boil veggies and paneer; prepare sweet cream cashew korma sauce.",
                    "2. Saut\u00e9 diced potatoes with chopped fresh methi leaves, turmeric, and garlic till crisp dry."
                ],
                "youtube_query": "navratan korma aloo methi dry recipe"
            },
            {
                "gravy": "Mix Veg Handi Gravy",
                "dry_item": "Baingan Potato Fry",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~460 kcal/person",
                "ingredients": [
                    "1 cup Mixed Veggies",
                    "2 Small Eggplants",
                    "1 Potato",
                    "Handi Spices",
                    "Butter"
                ],
                "steps": [
                    "1. Saut\u00e9 veggies in butter, cook in handi with onion-tomato paste and cream.",
                    "2. Cut brinjal and potato into strips; saut\u00e9 with turmeric, red chili, and amchur."
                ],
                "youtube_query": "mix veg handi baingan aloo fry recipe"
            }
        ],
        "Non-Veg": [
            {
                "gravy": "Butter Chicken",
                "dry_item": "Chicken Tikka Dry",
                "base_staple": "Butter Naan / Jeera Rice",
                "cooking_time": "35 mins",
                "calories": "~620 kcal/person",
                "ingredients": [
                    "500g Boneless Chicken",
                    "4 Tomatoes",
                    "50g Butter",
                    "Heavy Cream",
                    "Cashews"
                ],
                "steps": [
                    "1. Marinate chicken in curd and spices, grill for Tikka.",
                    "2. Puree boiled tomatoes and cashews; simmer in butter with spices, cream, and grilled chicken."
                ],
                "youtube_query": "butter chicken chicken tikka dry recipe"
            },
            {
                "gravy": "Punjabi Chicken Curry",
                "dry_item": "Mutton Seekh Kebab",
                "base_staple": "Roti / Steamed Rice",
                "cooking_time": "35 mins",
                "calories": "~590 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Minced Mutton",
                    "Onion-Tomato Paste",
                    "Ghee"
                ],
                "steps": [
                    "1. Prepare robust Punjabi gravy with brown fried onions, garlic, tomato puree, and chicken.",
                    "2. Mold spiced minced mutton onto skewers and pan-fry till charred."
                ],
                "youtube_query": "punjabi chicken curry mutton seekh kebab recipe"
            },
            {
                "gravy": "Mutton Rogan Josh",
                "dry_item": "Chicken Tangdi Fry",
                "base_staple": "Steamed Basmati Rice / Naan",
                "cooking_time": "45 mins",
                "calories": "~640 kcal/person",
                "ingredients": [
                    "500g Mutton",
                    "4 Chicken Drumsticks",
                    "Kashmiri Red Chili",
                    "Fennel Powder",
                    "Curd"
                ],
                "steps": [
                    "1. Sear mutton in mustard oil; add curd, Kashmiri chili, fennel, ginger powder; slow cook till tender.",
                    "2. Marinate drumsticks in spices, pan roast until golden crisp."
                ],
                "youtube_query": "mutton rogan josh chicken tangdi fry recipe"
            },
            {
                "gravy": "Shahi Chicken Korma",
                "dry_item": "Fish Amritsari",
                "base_staple": "Butter Naan / Rice",
                "cooking_time": "30 mins",
                "calories": "~600 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Fish Fillets",
                    "Cashew-Almond Paste",
                    "Fried Onions",
                    "Besan",
                    "Ajwain"
                ],
                "steps": [
                    "1. Make creamy gravy with fried onion paste, yogurt, cashews, cardamom.",
                    "2. Coat fish fillets with besan, ajwain, chili powder, lemon; deep fry till crispy."
                ],
                "youtube_query": "shahi chicken korma fish amritsari recipe"
            },
            {
                "gravy": "Kadhai Chicken",
                "dry_item": "Chicken Malai Tikka",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~580 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Boneless Chicken",
                    "Capsicum",
                    "Crushed Whole Spices",
                    "Heavy Cream"
                ],
                "steps": [
                    "1. Saut\u00e9 chicken with capsicum, onions, tomatoes, and crushed kadhai spices.",
                    "2. Marinate boneless chicken in cream, cheese, cardamom, and green chili; pan-grill till brown."
                ],
                "youtube_query": "kadhai chicken malai tikka dry recipe"
            },
            {
                "gravy": "Mutton Do Pyaza",
                "dry_item": "Tandoori Chicken Pan Dry",
                "base_staple": "Roti / Naan",
                "cooking_time": "40 mins",
                "calories": "~630 kcal/person",
                "ingredients": [
                    "500g Mutton",
                    "500g Whole Chicken Legs",
                    "4 Onions",
                    "Curd",
                    "Tandoori Masala"
                ],
                "steps": [
                    "1. Pressure cook mutton with sliced onions; stir in onion cubes and tomato base.",
                    "2. Marinate chicken legs with tandoori masala and curd; pan-roast with butter."
                ],
                "youtube_query": "mutton do pyaza tandoori chicken pan recipe"
            },
            {
                "gravy": "Chicken Bhuna Masala",
                "dry_item": "Punjabi Egg Bhurji",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~540 kcal/person",
                "ingredients": [
                    "400g Chicken",
                    "4 Eggs",
                    "Onions",
                    "Tomatoes",
                    "Green Chilies",
                    "Butter"
                ],
                "steps": [
                    "1. Cook chicken on high heat, roasting continuously with thick onion-tomato gravy.",
                    "2. Scramble eggs in butter with finely chopped onions, tomatoes, green chilies."
                ],
                "youtube_query": "chicken bhuna masala egg bhurji recipe"
            },
            {
                "gravy": "Bihari Fish Curry",
                "dry_item": "Mustard Fish Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "30 mins",
                "calories": "~520 kcal/person",
                "ingredients": [
                    "500g Rohu Fish",
                    "Yellow Mustard Seeds",
                    "Garlic",
                    "Tomatoes",
                    "Turmeric"
                ],
                "steps": [
                    "1. Grind yellow mustard and garlic into smooth paste.",
                    "2. Marinate fish with paste, shallow fry.",
                    "3. Cook half fried fish in mustard-tomato curry gravy until bubbling."
                ],
                "youtube_query": "bihari fish curry mustard fish fry recipe"
            },
            {
                "gravy": "Rara Chicken",
                "dry_item": "Chicken Lemon Pepper Fry",
                "base_staple": "Roti / Naan",
                "cooking_time": "35 mins",
                "calories": "~620 kcal/person",
                "ingredients": [
                    "400g Chicken Pieces",
                    "200g Chicken Keema",
                    "Black Pepper",
                    "Lemon Juice"
                ],
                "steps": [
                    "1. Prepare gravy using minced chicken, onions, tomatoes; add chicken bone pieces and simmer.",
                    "2. Toss boneless chicken pieces with pepper and butter, finish with lemon juice."
                ],
                "youtube_query": "chicken rara lemon pepper chicken recipe"
            },
            {
                "gravy": "Awadhi Mutton Korma",
                "dry_item": "Mutton Shami Kebab",
                "base_staple": "Mughlai Paratha / Rice",
                "cooking_time": "45 mins",
                "calories": "~650 kcal/person",
                "ingredients": [
                    "500g Mutton",
                    "250g Minced Mutton",
                    "50g Chana Dal",
                    "Kewra Water",
                    "Cashew Paste"
                ],
                "steps": [
                    "1. Boil minced mutton with chana dal, grind smooth, shape patties, shallow fry.",
                    "2. Slow cook mutton in aromatic gravy made with fried onions, cashew paste, yogurt, kewra water."
                ],
                "youtube_query": "awadhi mutton korma shami kebab recipe"
            },
            {
                "gravy": "Chicken Saagwala",
                "dry_item": "Aloo Keema Dry",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~560 kcal/person",
                "ingredients": [
                    "400g Chicken",
                    "200g Minced Mutton",
                    "1 Potato",
                    "Spinach Puree",
                    "Garlic"
                ],
                "steps": [
                    "1. Saut\u00e9 chicken with garlic, ginger, onion-tomato masala; stir in spinach puree.",
                    "2. Saut\u00e9 minced mutton and potato cubes with cumin, red chili, and dry spices until dry."
                ],
                "youtube_query": "chicken saagwala aloo keema dry recipe"
            },
            {
                "gravy": "Dhaba Style Egg Curry",
                "dry_item": "Chicken Kasuri Dry",
                "base_staple": "Roti / Rice",
                "cooking_time": "25 mins",
                "calories": "~510 kcal/person",
                "ingredients": [
                    "4 Boiled Eggs",
                    "300g Chicken",
                    "Kasuri Methi",
                    "Onion-Tomato Gravy",
                    "Garlic"
                ],
                "steps": [
                    "1. Shallow fry boiled eggs, drop into rustic spicy onion-tomato garlic gravy.",
                    "2. Stir-fry chicken pieces with generous crushed kasuri methi, butter, and black pepper till dry."
                ],
                "youtube_query": "dhaba style egg curry chicken kasuri dry recipe"
            },
            {
                "gravy": "Pahari Mutton Curry",
                "dry_item": "Chicken Lollipop Dry",
                "base_staple": "Steamed Rice / Roti",
                "cooking_time": "40 mins",
                "calories": "~610 kcal/person",
                "ingredients": [
                    "500g Mutton",
                    "6 Chicken Lollipops",
                    "Curd",
                    "Mustard Oil",
                    "Chili Garlic Sauce"
                ],
                "steps": [
                    "1. Pressure cook mutton in mustard oil with onions, curd, coriander seeds.",
                    "2. Marinate lollipops, deep fry till crisp, toss in hot chili garlic sauce."
                ],
                "youtube_query": "pahari mutton curry chicken lollipop recipe"
            },
            {
                "gravy": "Keema Matar Gravy",
                "dry_item": "Dhaba Chicken Fry Sukha",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~590 kcal/person",
                "ingredients": [
                    "300g Minced Mutton",
                    "1 cup Green Peas",
                    "300g Chicken",
                    "Lemon"
                ],
                "steps": [
                    "1. Saut\u00e9 minced mutton with green peas, ginger-garlic, tomatoes, and spices.",
                    "2. Fry chicken pieces with chopped garlic, green chilies, coriander powder, lemon juice till dry."
                ],
                "youtube_query": "keema matar gravy dhaba chicken fry recipe"
            },
            {
                "gravy": "Chicken Handi Gravy",
                "dry_item": "Fish Tikka Tandoori Dry",
                "base_staple": "Roti / Rice",
                "cooking_time": "30 mins",
                "calories": "~570 kcal/person",
                "ingredients": [
                    "400g Chicken",
                    "300g Fish Cubes",
                    "Curd",
                    "Kasuri Methi",
                    "Handi Masala"
                ],
                "steps": [
                    "1. Slow cook chicken in clay handi with onion, tomato, yogurt, and fresh ground spices.",
                    "2. Marinate fish cubes with curd, ajwain, tandoori masala; pan-grill till charred."
                ],
                "youtube_query": "chicken handi fish tikka recipe"
            },
            {
                "gravy": "Mutton Nihari Gravy",
                "dry_item": "Chicken Kalmi Kebab",
                "base_staple": "Khamiri Roti / Naan",
                "cooking_time": "50 mins",
                "calories": "~660 kcal/person",
                "ingredients": [
                    "500g Mutton Shank",
                    "3 Chicken Leg Thigh Pieces",
                    "Nihari Masala",
                    "Wheat Slurry"
                ],
                "steps": [
                    "1. Slow cook mutton shanks with Nihari spices, thicken gravy with wheat flour slurry.",
                    "2. Marinate chicken leg pieces in cashew paste, curd, cream; pan-roast dry."
                ],
                "youtube_query": "mutton nihari chicken kalmi kebab recipe"
            },
            {
                "gravy": "Chicken Tariwala",
                "dry_item": "Mutton Sukha North Style",
                "base_staple": "Steamed Basmati Rice",
                "cooking_time": "35 mins",
                "calories": "~570 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "300g Mutton",
                    "Onions",
                    "Tomatoes",
                    "Ghee"
                ],
                "steps": [
                    "1. Prepare thin broth gravy with onions, tomatoes, coriander, and chicken.",
                    "2. Stir-fry cooked mutton in ghee with chopped garlic, dark roasted spices, and black pepper till bone-dry."
                ],
                "youtube_query": "chicken tariwala mutton sukha recipe"
            },
            {
                "gravy": "Machher Jhol",
                "dry_item": "Spiced Boiled Egg Fry",
                "base_staple": "Steamed Rice",
                "cooking_time": "25 mins",
                "calories": "~480 kcal/person",
                "ingredients": [
                    "400g Katla Fish",
                    "4 Eggs",
                    "Kalonji Seeds",
                    "Green Chilies",
                    "Mustard Oil"
                ],
                "steps": [
                    "1. Fry fish lightly in mustard oil.",
                    "2. Saut\u00e9 kalonji and green chilies, add water, turmeric, cumin; simmer fish.",
                    "3. Slice boiled eggs, coat with turmeric and chili powder, shallow fry crisp."
                ],
                "youtube_query": "machher jhol spiced egg fry recipe"
            },
            {
                "gravy": "Chicken Lababdar",
                "dry_item": "Chicken Reshmi Kebab",
                "base_staple": "Butter Naan / Rice",
                "cooking_time": "35 mins",
                "calories": "~610 kcal/person",
                "ingredients": [
                    "500g Boneless Chicken",
                    "Capsicum",
                    "Cashew Paste",
                    "Cream",
                    "Kasuri Methi"
                ],
                "steps": [
                    "1. Cook chicken in rich onion-tomato-cashew gravy with fine chopped capsicum.",
                    "2. Marinate boneless chicken in cream, cashew paste, white pepper; pan-grill till dry brown."
                ],
                "youtube_query": "chicken lababdar chicken reshmi kebab recipe"
            },
            {
                "gravy": "Mutton Saagwala",
                "dry_item": "Desi Chicken Popcorn Fry",
                "base_staple": "Roti / Paratha",
                "cooking_time": "40 mins",
                "calories": "~620 kcal/person",
                "ingredients": [
                    "400g Mutton",
                    "250g Boneless Chicken",
                    "Spinach Puree",
                    "Garlic",
                    "Cornstarch"
                ],
                "steps": [
                    "1. Pressure cook mutton, simmer in spinach puree tempered with fried garlic and ghee.",
                    "2. Marinate bite-sized chicken with red chili and cornstarch, deep fry crunchy."
                ],
                "youtube_query": "mutton saagwala chicken popcorn recipe"
            },
            {
                "gravy": "Chicken Changezi",
                "dry_item": "Tandoori Prawns Pan Dry",
                "base_staple": "Khamiri Roti / Rice",
                "cooking_time": "35 mins",
                "calories": "~600 kcal/person",
                "ingredients": [
                    "500g Chicken",
                    "250g Prawns",
                    "Milk",
                    "Cream",
                    "Tomato Puree",
                    "Tandoori Masala"
                ],
                "steps": [
                    "1. Fry chicken; cook thick sauce made of milk, cream, tomato, fried onion paste, combine chicken.",
                    "2. Marinate prawns in curd, tandoori masala, lemon; pan fry in butter till crisp dry."
                ],
                "youtube_query": "chicken changezi tandoori prawns recipe"
            },
            {
                "gravy": "Mutton Beliram",
                "dry_item": "Chicken Angara Tikka Dry",
                "base_staple": "Roti / Naan",
                "cooking_time": "45 mins",
                "calories": "~650 kcal/person",
                "ingredients": [
                    "500g Mutton",
                    "300g Boneless Chicken",
                    "1 cup Curd",
                    "Coriander Seeds",
                    "Charcoal Piece"
                ],
                "steps": [
                    "1. Slow cook mutton with curd, crushed coriander seeds, sliced onions, ghee.",
                    "2. Grill marinated chicken, smoke using hot charcoal bit and ghee."
                ],
                "youtube_query": "mutton beliram chicken angara tikka recipe"
            },
            {
                "gravy": "Chicken White Korma",
                "dry_item": "Mutton Boti Fry Dry",
                "base_staple": "Naan / Rice",
                "cooking_time": "35 mins",
                "calories": "~590 kcal/person",
                "ingredients": [
                    "400g Chicken",
                    "250g Mutton Boti",
                    "White Pepper",
                    "Cashew Paste",
                    "Curd"
                ],
                "steps": [
                    "1. Cook chicken in white gravy made with curd, cashew paste, white pepper.",
                    "2. Boil small boneless mutton boti pieces, stir-fry in ghee with garlic, red chili, black pepper till dry."
                ],
                "youtube_query": "chicken white korma mutton boti fry recipe"
            },
            {
                "gravy": "Keema Kaleji Gravy",
                "dry_item": "Chicken Kasturi Kabab",
                "base_staple": "Roti / Paratha",
                "cooking_time": "30 mins",
                "calories": "~580 kcal/person",
                "ingredients": [
                    "250g Minced Mutton",
                    "150g Mutton Liver",
                    "300g Chicken",
                    "Kasuri Methi"
                ],
                "steps": [
                    "1. Saut\u00e9 minced mutton with onion-tomato gravy; add liver pieces towards the end.",
                    "2. Marinate chicken in egg, kasuri methi, curd, yellow chili powder; pan-roast dry."
                ],
                "youtube_query": "keema kaleji gravy chicken kasturi kabab recipe"
            },
            {
                "gravy": "Mutton Paya Curry",
                "dry_item": "Chicken Wings Dry Roast",
                "base_staple": "Naan / Khamiri Roti / Rice",
                "cooking_time": "50 mins",
                "calories": "~630 kcal/person",
                "ingredients": [
                    "4 Mutton Trotters",
                    "6 Chicken Wings",
                    "Onions",
                    "Whole Spices",
                    "Ghee"
                ],
                "steps": [
                    "1. Pressure cook trotters with onions, ginger-garlic, whole spices for 45 mins.",
                    "2. Marinate chicken wings in chili powder, garlic, vinegar; pan-roast in butter till sticky dry."
                ],
                "youtube_query": "mutton paya curry chicken wings dry roast recipe"
            }
        ]
    }
}
