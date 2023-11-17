import { Component, ElementRef, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('f') signUpForm: NgForm;
  defaultQuestion = 'pet';
  answer = '';
  genders = ['male', 'female'];
  user = {
    username: '',
    email: '',
    secretQuestion: '',
    answer: '',
    gender: '',
  };
  dataSubmitted: boolean = false;

  suggestUserName() {
    const suggestedName = 'Superuser';
    this.signUpForm.form.patchValue({ userData: { username: suggestedName } });
  }

  // onSubmit(form: NgForm) {
  //   console.log(form);
  //   console.log('form submitted');
  // }

  onSubmit() {
    console.log(this.signUpForm);
    this.dataSubmitted = true;
    this.user.username = this.signUpForm.form.value.userData.username;
    this.user.email = this.signUpForm.form.value.userData.email;
    this.user.secretQuestion = this.signUpForm.form.value.secret;
    this.user.answer = this.signUpForm.form.value.questionAnswer;
    this.user.gender = this.signUpForm.form.value.gender;

    this.signUpForm.reset();
  }
}
