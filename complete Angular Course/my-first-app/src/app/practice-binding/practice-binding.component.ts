import { Component } from '@angular/core';

@Component({
  selector: 'app-practice-binding',
  templateUrl: './practice-binding.component.html',
  styleUrls: ['./practice-binding.component.css']
})
export class PracticeBindingComponent {
  username:string = ""
  usernameIsEmpty = true

  onInputText(event):void{
    if (event.target.value.length > 0){
      this.usernameIsEmpty = false
    }else{
      this.usernameIsEmpty = true
    }
  }

  onBtnClick(){
    this.username = ""
  }
}
