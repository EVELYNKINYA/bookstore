import recipe
import meal_planner

def main():
    recipe.create_table()
    meal_planner.create_table()
    
    while True:
        print("\nWelcome To our Meal Planner Menu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Find Recipe by ID")
        print("4. Find Recipes by Keyword")
        print("5. Update Recipe")
        print("6. Delete Recipe")
        print("7. Create Meal Plan")
        print("8. View Meal Plans")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (separated by commas): ")
            instructions = input("Enter instructions: ")
            recipe.add_recipe(name, ingredients, instructions)
            print("Recipe added successfully!")
        elif choice == '2':
            recipes = recipe.view_recipes()
            for recipe_item in recipes:  
                print(recipe_item)
        elif choice == '3':
            recipe_id = input("Enter recipe ID: ")
            recipe_item = recipe.find_recipe_by_id(recipe_id) 
            print(recipe_item)
        elif choice == '4':
            keyword = input("Enter keyword: ")
            recipes = recipe.find_recipes_by_keyword(keyword)
            for recipe_item in recipes:
                print(recipe_item)
        elif choice == '5':
            recipe_id = input("Enter recipe ID to update: ")
            name = input("Enter new recipe name: ")
            ingredients = input("Enter new ingredients (separated by commas): ")
            instructions = input("Enter new instructions: ")
            recipe.update_recipe(recipe_id, name, ingredients, instructions)
            print("Recipe updated successfully!")
        elif choice == '6':
            recipe_id = input("Enter recipe ID to delete: ")
            recipe.delete_recipe(recipe_id)
            print("Recipe deleted successfully!")
        elif choice == '7':
            name = input("Enter meal plan name: ")
            day = input("Enter day of the week: ")
            recipe_id = input("Enter recipe ID to add to the meal plan: ")
            meal_planner.create_meal_plan(name, day, recipe_id)
            print("Meal plan created successfully!")
        elif choice == '8':
            meal_plans = meal_planner.view_meal_plans()
            for meal_plan in meal_plans:
                print(meal_plan)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
