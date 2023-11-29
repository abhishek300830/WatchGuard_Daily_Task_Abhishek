import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RecipeService } from '../recipes/recipe.service';
import { Recipe } from '../recipes/recipe.model';
import { map } from 'rxjs/operators';
import { AuthService } from '../auth/auth.service';

@Injectable({ providedIn: 'root' })
export class DataStorageService {
  constructor(
    private http: HttpClient,
    private recipeService: RecipeService,
    private authService: AuthService
  ) {}
  k;

  storeRecipes() {
    const recipes = this.recipeService.getRecipes();
    return this.http.put(
      'https://ng-course-recipe-book-9269f-default-rtdb.asia-southeast1.firebasedatabase.app/recipes.json',
      recipes
    );
  }

  fetchRecipies() {
    return this.http
      .get<Recipe[]>(
        'https://ng-course-recipe-book-9269f-default-rtdb.asia-southeast1.firebasedatabase.app/recipes.json'
      )
      .pipe(
        map((recipes) => {
          return recipes.map((recipe) => {
            return {
              ...recipe,
              ingredients: recipe.ingredients ? recipe.ingredients : [],
            };
          });
        })
      );
  }
}
