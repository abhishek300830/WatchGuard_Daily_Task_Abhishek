import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { serverComponent } from './server/server.component';
import { ServersComponent } from './servers/servers.component';
import { warningAlert } from './warning-alert/warning-alert.component';
import { successAlert } from './success-alert/success-alert.component';
import { PracticeBindingComponent } from './practice-binding/practice-binding.component';
import { PracticeDirectiveComponent } from './practice-directive/practice-directive.component';
import { PracticeNgforComponent } from './practice-ngfor/practice-ngfor.component';
import { DirectiveDeepComponent } from './directive-deep/directive-deep.component';
import { BasicHighlightDirective } from './directive-deep/basic-highlight/basic-highlight.directive';
import { BetterHighlightDirective } from './directive-deep/better-highlight/better-highlight.directive';
import { UnlessDirective } from './directive-deep/unless.directive';

@NgModule({
  declarations: [
    AppComponent,
    serverComponent,
    ServersComponent,
    warningAlert,
    successAlert,
    PracticeBindingComponent,
    PracticeDirectiveComponent,
    PracticeNgforComponent,
    DirectiveDeepComponent,
    BasicHighlightDirective,
    BetterHighlightDirective,
    UnlessDirective,
  ],
  imports: [BrowserModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
