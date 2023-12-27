import { TestBed } from '@angular/core/testing';
import { CalculatorService } from './calculator.service';
import { LoggerService } from '../Logger/logger.service';

describe('CalculatorService', () => {
  let mockLoggerService: any;
  let calculator: CalculatorService;

  beforeEach(() => {
    mockLoggerService = jasmine.createSpyObj('LoggerService', ['log']);

    TestBed.configureTestingModule({
      providers: [
        CalculatorService,
        {
          provide: LoggerService,
          useValue: mockLoggerService,
        },
      ],
    });
    // calculator = new CalculatorService(mockLoggerService);
    calculator = TestBed.inject(CalculatorService);
  });

  it('should add two two number', () => {
    // let loggerService = new LoggerService();
    // spyOn(loggerService, 'log');

    const result = calculator.add(1, 2);

    expect(result).toBe(3);
    expect(mockLoggerService.log).toHaveBeenCalledTimes(1);
  });

  it('should subtract two two number', () => {
    const result = calculator.subtract(1, 2);

    expect(result).toBe(-1);
    expect(mockLoggerService.log).toHaveBeenCalledTimes(1);
  });
});
