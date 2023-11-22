import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  reactiveForm: FormGroup;
  ngOnInit() {
    this.reactiveForm = new FormGroup({
      projectName: new FormControl(
        null,
        [Validators.required, this.projectNameValidator],
        this.asyncProjectNameValidator
      ),
      email: new FormControl(null, [Validators.required, Validators.email]),
      projectStatus: new FormControl('choose', Validators.required),
    });
  }

  onSubmit() {
    console.log(this.reactiveForm.value);
  }

  projectNameValidator(control: FormControl): { [s: string]: boolean } {
    if (control.value === 'test') {
      return { InvalidName: true };
    } else {
      return null;
    }
  }

  asyncProjectNameValidator(control: FormControl): Promise<any> {
    const promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        if (control.value === 'async') {
          resolve({ InvalidName: true });
        } else {
          resolve(null);
        }
      }, 1500);
    });
    return promise;
  }
}
