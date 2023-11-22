import {
  Component,
  ViewChild,
  ElementRef,
  EventEmitter,
  Output,
  OnInit,
  OnDestroy,
} from '@angular/core';
import { Ingredient } from 'src/app/shared/ingredient.model';
import { ShoppingListService } from '../shopping-list.service';
import { NgForm } from '@angular/forms';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-shopping-edit',
  templateUrl: './shopping-edit.component.html',
  styleUrls: ['./shopping-edit.component.css'],
})
export class ShoppingEditComponent implements OnInit, OnDestroy {
  @ViewChild('f', { static: false }) slForm: NgForm;
  subscription: Subscription;
  editMode = false;
  editedItemIndex: number;
  editedItem: Ingredient;
  // @ViewChild('nameInput') nameInputRef: ElementRef;
  // @ViewChild('amountInput') amountInputRef: ElementRef;

  // @Output() ingredientAdded = new EventEmitter<Ingredient>();
  constructor(private shoppingListSevice: ShoppingListService) {}

  ngOnInit() {
    this.subscription = this.shoppingListSevice.startedEditing.subscribe(
      (index: number) => {
        this.editedItemIndex = index;
        this.editMode = true;
        this.editedItem = this.shoppingListSevice.getIngredient(index);
        this.slForm.setValue({
          name: this.editedItem.name,
          amount: this.editedItem.amount,
        });
      }
    );
  }

  onSubmit(form: NgForm) {
    const value = form.value;
    // const ingName = this.nameInputRef.nativeElement.value;
    // const ingAmount = this.amountInputRef.nativeElement.value;
    const newIngredient = new Ingredient(value.name, value.amount);

    if (this.editMode) {
      this.shoppingListSevice.updateIngredient(
        this.editedItemIndex,
        newIngredient
      );
    } else {
      this.shoppingListSevice.addIngredient(newIngredient);
    }
    this.editMode = false;
    form.reset();
    // this.ingredientAdded.emit(newIngredient);
  }
  onDelete() {
    this.shoppingListSevice.deleteIngredient(this.editedItemIndex);
    this.onClear();
  }
  onClear() {
    this.slForm.reset();
    this.editMode = false;
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
