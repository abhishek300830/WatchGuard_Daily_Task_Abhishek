import { Component } from '@angular/core';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.css']
})
export class ServersComponent {

  allowNewServer:boolean = false
  serverCreationStatus : string = "No server was created"
  serverName:string = ''

  constructor(){
    setTimeout(() => {
      this.allowNewServer = true
    }, 2000);
  }

  onCreateServer(): void {
    this.serverCreationStatus = "Server was Created! Name is "+ this.serverName;
  }

  onUpdateServerName(event){
    this.serverName = event.target.value

  }
  
}
