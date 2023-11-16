import { Component } from '@angular/core';

@Component({
  selector: 'app-practice-ngfor',
  templateUrl: './practice-ngfor.component.html',
  styleUrls: ['./practice-ngfor.component.css']
})
export class PracticeNgforComponent {
  object = Object
  array = [ 1,2,3]
  arrayOfObject = [{name:"aryan",age:"21"},{name:"abhishek",age:"21"}]
  objectOfStudent = {name:"abhishek",age:"21"}
}
