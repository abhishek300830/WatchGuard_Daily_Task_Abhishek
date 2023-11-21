import { Component, EventEmitter, Output, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  @ViewChild('f') reimbursementForm: NgForm;
  @Output() userForm = new EventEmitter<NgForm>();

  @Output() formSubmitted = new EventEmitter<Boolean>();

  inputGroupRef = ['inputForm1'];

  constructor() {}

  onSubmit() {
    this.userForm.emit(this.reimbursementForm);
    this.formSubmitted.emit(true);
  }

  addNewInputGroup() {
    let formRef = 'inputForm' + (this.inputGroupRef.length + 1);
    this.inputGroupRef.push(formRef);
  }

  deleteInputGroup(inputFormName) {
    let idx = this.inputGroupRef.indexOf(inputFormName);
    this.inputGroupRef.splice(idx, 1);
  }
}
