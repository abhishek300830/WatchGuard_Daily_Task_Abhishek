import { Component } from '@angular/core';

import { UserService } from '../app.service';
import { ReimbursementModel, UserDetailModel } from '../app.model';

@Component({
  selector: 'app-display-details',
  templateUrl: './display-details.component.html',
  styleUrls: ['./display-details.component.css'],
})
export class DisplayDetailsComponent {
  userDetails: UserDetailModel = new UserDetailModel();
  userReimbursementArray: Array<ReimbursementModel>;

  constructor(private userService: UserService) {}

  ngOnInit() {
    this.userService.submitClickedSub$.subscribe(() => {
      this.userDetails = Object.assign({}, this.userService.userDetails);

      this.userReimbursementArray =
        this.userService.userDetails.reimbursements.map((currVal) => {
          return Object.assign({}, currVal);
        });
    });
  }
}
