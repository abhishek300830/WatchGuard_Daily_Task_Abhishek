import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FormsModule} from "@angular/forms"

import { AppComponent } from './app.component';
import { serverComponent } from './server/server.component';
import { ServersComponent } from './servers/servers.component';
import { warningAlert } from './warning-alert/warning-alert.component';
import { successAlert } from './success-alert/success-alert.component';
import { PracticeBindingComponent } from './practice-binding/practice-binding.component'
import { PracticeDirectiveComponent } from './practice-directive/practice-directive.component';

@NgModule({
  declarations: [
    AppComponent,
    serverComponent,
    ServersComponent,
    warningAlert,
    successAlert,
    PracticeBindingComponent,
    PracticeDirectiveComponent

  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
