import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LoggerService {
  messages: string[] = [];
  constructor() {}

  log(msg: string) {
    this.messages.push(msg);
    console.log(msg);
  }
  clear() {
    this.messages = [];
  }
}
