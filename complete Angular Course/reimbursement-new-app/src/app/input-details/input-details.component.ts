import { Component } from '@angular/core';

import { UserService } from './../app.service';
import { UserDetailModel } from '../app.model';

@Component({
  selector: 'app-input-details',
  templateUrl: './input-details.component.html',
  styleUrls: ['./input-details.component.css'],
})
export class InputDetailsComponent {
  userDetails: UserDetailModel;

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.userDetails = this.userService.userDetails;
  }

  addNewInputGroup() {
    this.userService.userDetails.reimbursements.push({
      id: null,
      name: '',
      amount: null,
      type: '',
    });
  }

  deleteInputGroup(index: number) {
    this.userService.userDetails.reimbursements.splice(index, 1);
  }

  onFormSubmit() {
    this.userService.submitClickedSub$.next(true);
  }
}
