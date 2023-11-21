import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-display-reimbursement',
  templateUrl: './display-reimbursement.component.html',
  styleUrls: ['./display-reimbursement.component.css'],
})
export class DisplayReimbursementComponent {
  @Input() ReimbursementData: Object;
  @Input() onFormSubmitted: Boolean;
  Object = Object;

  submitted = false;
  // Object: any;
}
