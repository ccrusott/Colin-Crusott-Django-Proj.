# Colin-Crusott-Django-Proj.
# Django Inventory Tracker


## Short Overview
In this repository, you will find a full-stack web application built by Colin Crusott. The web app utilizes Python (Django), HTML, and CSS. It includes all 
functionalitiies of an inventory management application. This includes: menu selections, ingredients, recipes, purchase capabilities, financial tracking, and 
authentication.

## Long Overview
This project allows for a restaurant staff/owner to utilize the following functionalities:
- An inventory of different `Ingredient`s, their available quantity, their units, and their prices per unit
- A list of the restaurant's `MenuItem`s, and the price set for each entry
- A list of the ingredients that each menu item requires (`RecipeRequirement`s) and their availability
- A log of all `Purchase`s made at the restaurant, with a total for Costs(ingredients), Revenue(Sales), and Net Income
- Purchases of menu items are not possible if the required ingredients are out of stock

The user (the restaurant owner/staff) is be able to enter in new recipes along with their recipe requirements, and how much that menu item costs. 
They are also able to add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.

Lastly, they are able to enter in a customer purchase of a menu item. When a customer purchases an item off the menu, 
the inventory is modified to accommodate what happened, as well as recording the time that the purchase was made.
