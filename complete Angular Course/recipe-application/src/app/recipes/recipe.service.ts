import { EventEmitter, Injectable } from '@angular/core';
import { Recipe } from './recipe.model';
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';

@Injectable()
export class RecipeService {
  recipeSelected = new EventEmitter<Recipe>();

  private recipes: Recipe[] = [
    new Recipe(
      'Burgers',
      'A burger is a patty of ground beef grilled and placed between two halves of a bun.',
      'https://www.tastingtable.com/img/gallery/17-celebrity-chefs-and-their-favorite-fast-food-restaurants/l-intro-1674674335.jpg',
      [new Ingredient('raw onion', 1), new Ingredient('mayonnaise', 1)]
    ),
    new Recipe(
      'Noodles',
      'Noodles are commonly used to add flavour to broth soups. They are commonly boiled or sautéed and served with sauces',
      'https://assets.gqindia.com/photos/6213cbed18140d747a9b0a6e/16:9/w_1920,h_1080,c_limit/new%20restaurant%20menus%20in%20Mumbai.jpg',
      [new Ingredient('raw onion', 1), new Ingredient('mayonnaise', 1)]
    ),
    new Recipe(
      'buttermilk crepes',
      'Buttermilk crepes are a thin type of pancake made of buttermilk, eggs, melted butter, and flour.',
      'https://hips.hearstapps.com/hmg-prod/images/crepes-index-64347419e3c7a.jpg?crop=0.888888888888889xw:1xh;center,top&resize=1200:*',
      [new Ingredient('raw onion', 1), new Ingredient('mayonnaise', 1)]
    ),
  ];

  constructor(private shoppingListService: ShoppingListService) {}

  getRecipes() {
    return this.recipes.slice();
  }
  getRecipe(index: number) {
    return this.recipes[index];
  }
  addIngredientsToShoppingList(ingredients: Ingredient[]) {
    this.shoppingListService.addIngredients(ingredients);
  }
}
