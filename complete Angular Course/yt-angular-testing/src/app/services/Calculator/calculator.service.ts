import { Injectable } from '@angular/core';
import { LoggerService } from '../Logger/logger.service';

@Injectable({
  providedIn: 'root',
})
export class CalculatorService {
  constructor(private logger: LoggerService) {}

  add(a: number, b: number): number {
    this.logger.log(`Adding ${a} + ${b}`);
    return a + b;
  }

  subtract(a: number, b: number): number {
    this.logger.log(`Subtracting ${a} - ${b}`);
    return a - b;
  }
}
