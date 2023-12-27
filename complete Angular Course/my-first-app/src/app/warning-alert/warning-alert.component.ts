import { Component } from '@angular/core';

@Component({
  selector: 'app-warning-alert',
  template: ` <div>this is warning alert</div> `,
  styles: [
    `
      div {
        color: red;
      }
    `,
  ],
})
export class warningAlert {}
