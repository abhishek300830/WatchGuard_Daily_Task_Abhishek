import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DisplayDetailsComponent } from './display-details/display-details.component';
import { InputDetailsComponent } from './user-details/user-details.component';

@NgModule({
  declarations: [AppComponent, DisplayDetailsComponent, InputDetailsComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
