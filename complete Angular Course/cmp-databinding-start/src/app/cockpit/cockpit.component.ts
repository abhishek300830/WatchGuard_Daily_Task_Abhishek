import { Component, EventEmitter, OnInit,Output,ViewChild,ElementRef } from '@angular/core';

@Component({
  selector: 'app-cockpit',
  templateUrl: './cockpit.component.html',
  styleUrls: ['./cockpit.component.css']
})
export class CockpitComponent implements OnInit {

  @Output() serverCreated = new EventEmitter<{serverName:string,serverContent:string}>;
  @Output('bpCreated') blueprintCreated = new EventEmitter<{serverName:string,serverContent:string}>;

  // newServerName = '';
  // newServerContent = '';
  @ViewChild('serverContentInput',{static:true}) serverContentInput:ElementRef;

  constructor() { }

  ngOnInit(): void {
  }
  onAddServer(nameInput:HTMLInputElement) {
    // console.log(this.serverContentInput)
    // console.log(nameInput.value)
    this.serverCreated.emit({
      serverName:nameInput.value,
      serverContent:this.serverContentInput.nativeElement.value
    })
    // this.serverElements.push({
    //   type: 'server',
    //   name: this.newServerName,
    //   content: this.newServerContent
    // });
  }

  onAddBlueprint(nameInput:HTMLInputElement) {
    this.blueprintCreated.emit({
      serverName:nameInput.value,
      serverContent:this.serverContentInput.nativeElement.value
    })
    // this.serverElements.push({
    //   type: 'blueprint',
    //   name: this.newServerName,
    //   content: this.newServerContent
    // });
  }

}
