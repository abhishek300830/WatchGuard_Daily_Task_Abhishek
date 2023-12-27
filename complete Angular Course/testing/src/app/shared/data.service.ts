import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class DataService {
  Data: string = 'hello';
  constructor() {}

  getDetails() {
    const resultPromise = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('Data');
      }, 1500);
    });
    return resultPromise;
  }
}
