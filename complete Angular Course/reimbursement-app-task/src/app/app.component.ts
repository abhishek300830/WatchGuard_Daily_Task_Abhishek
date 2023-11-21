import { NgForm } from '@angular/forms';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'reimbursement-app-task';
  formValue: any;
  isFormSubmitted: any;

  getUserForm(ngform: NgForm) {
    this.formValue = ngform.form.value;
    console.log(this.formValue);
  }
  onFormSubmitted(isSubmitted) {
    this.isFormSubmitted = isSubmitted;
  }
}
