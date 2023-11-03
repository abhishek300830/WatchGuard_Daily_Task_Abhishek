import { Component} from "@angular/core"

@Component({
    selector:"app-server",
    templateUrl:"./server.component.html",
    styleUrls:["./server.component.css"]
})
export class serverComponent{
    serverId : number = 123456789
    status:string

    constructor(){
        this.status= Math.random() > 0.5 ? "online" : "offline" 
    }

    getColor(){
        return this.status === "online"? "green":"red"
    }
}