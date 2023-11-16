import { Component } from '@angular/core';

@Component({
  selector: 'app-directive-deep',
  templateUrl: './directive-deep.component.html',
  styleUrls: ['./directive-deep.component.css'],
})
export class DirectiveDeepComponent {
  onlyOdd: boolean = false;
  oddNumbers = [1, 3, 5];
  evenNumbers = [2, 4];

  value = 1;
}
