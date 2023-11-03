import { Component } from '@angular/core'

@Component({
    selector:"app-practice-directive",
    templateUrl:"./practice-directive.component.html",
    styleUrls:["./practice-directive.component.css"]
})
export class PracticeDirectiveComponent{
    showDetails:boolean = false
    showDetailsClickLogger = []
    idx = 0

    toggleShowDetails(){
        this.idx++;
        this.showDetailsClickLogger.push({"idx":this.idx,"date":Date()});
        this.showDetails = !this.showDetails;
    }
   
}