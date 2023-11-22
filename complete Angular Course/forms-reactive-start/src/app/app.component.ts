import { Component, OnInit } from '@angular/core';
import {
  FormArray,
  FormBuilder,
  FormControl,
  FormGroup,
  Validators,
} from '@angular/forms';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  genders = ['male', 'female'];
  signUpForm: FormGroup;
  forBiddenUserNames = ['chris', 'anna'];

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit(): void {
    this.signUpForm = new FormGroup({
      userData: new FormGroup({
        username: new FormControl(null, [
          Validators.required,
          this.forBiddenNames.bind(this),
        ]),
        email: new FormControl(
          null,
          [Validators.required, Validators.email],
          this.forBiddenEmails
        ),
      }),
      gender: new FormControl('male'),
      hobbies: new FormArray([]),
    });
    this.signUpForm.valueChanges.subscribe((value) => {
      console.log('value', value);
    });
    this.signUpForm.statusChanges.subscribe((status) => {
      console.log('status', status);
    });
    //  set complete value of form
    this.signUpForm.setValue({
      userData: {
        username: 'abhishek',
        email: 'example@gmail.com',
      },
      gender: 'male',
      hobbies: [],
    });
    // set specific value
    this.signUpForm.patchValue({
      userData: {
        username: 'abhi',
      },
    });
  }

  onSubmit() {
    console.log(this.signUpForm);
    this.signUpForm.reset();
  }

  onAddHobby() {
    const control: FormControl = new FormControl(null);
    (this.signUpForm.get('hobbies') as FormArray).push(control);
  }

  getControls() {
    return (this.signUpForm.get('hobbies') as FormArray).controls;
  }

  forBiddenNames(control: FormControl): { [s: string]: boolean } {
    if (this.forBiddenUserNames.indexOf(control.value) !== -1) {
      return { nameIsForbidden: true };
    }
    return null;
  }

  forBiddenEmails(control: FormControl): Promise<any> | Observable<any> {
    const promise = new Promise<any>((resolve, reject) => {
      setTimeout(() => {
        if (control.value === 'test@test.com') {
          resolve({ emailIsForbidden: true });
        } else {
          resolve(null);
        }
      }, 1500);
    });
    return promise;
  }
}
